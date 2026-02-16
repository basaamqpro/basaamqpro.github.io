import tkinter as tk
import random
import torch
import torch.nn as nn
import torch.optim as optim

# -----------------------------
# CONFIG
# -----------------------------
GRID_SIZE = 14

WHITE_MIN = 2
WHITE_MAX = 11          # inclusive → 10x10 white area

RED_COUNT = 5
CELL_SIZE = 40

ACTIONS = {
    0: (-1, 0),  # UP
    1: (1, 0),   # DOWN
    2: (0, -1),  # LEFT
    3: (0, 1),   # RIGHT
}

# -----------------------------
# Q NETWORK
# -----------------------------
class QNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(5, 128),
            nn.ReLU(),
            nn.Linear(128, 4)
        )

    def forward(self, x):
        return self.net(x)

model = QNet()
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.SmoothL1Loss()   # Huber loss is usually nicer than MSE

gamma = 0.90
epsilon = 0.30

# -----------------------------
# ENVIRONMENT
# -----------------------------
class GameEnv:
    def reset(self):
        self.agent = [
            random.randint(WHITE_MIN, WHITE_MAX),
            random.randint(WHITE_MIN, WHITE_MAX)
        ]

        self.current_target = 1
        self.reds = {}
        positions = set()

        # 🔴 Reds STRICTLY inside 10x10 white area
        for i in range(1, RED_COUNT + 1):
            while True:
                x = random.randint(WHITE_MIN, WHITE_MAX)
                y = random.randint(WHITE_MIN, WHITE_MAX)
                if (x, y) not in positions:
                    positions.add((x, y))
                    self.reds[(x, y)] = i
                    break

        return self.get_state()

    def get_next_target_pos(self):
        # find the (x,y) of the red square with label == current_target
        for (x, y), num in self.reds.items():
            if num == self.current_target:
                return x, y
        # if not found (should only happen at end), just return agent position
        return self.agent[0], self.agent[1]

    def get_state(self):
        tx, ty = self.get_next_target_pos()
        return torch.tensor(
            [self.agent[0], self.agent[1], tx, ty, self.current_target],
            dtype=torch.float32
        )

    def step(self, action):
        dx, dy = ACTIONS[action]
        nx = self.agent[0] + dx
        ny = self.agent[1] + dy

        reward = -0.1  # smaller step penalty helps learning

        # 🔒 Restrict movement to white area only (your rule)
        if WHITE_MIN <= nx <= WHITE_MAX and WHITE_MIN <= ny <= WHITE_MAX:
            self.agent = [nx, ny]

        pos = tuple(self.agent)

        # correct red square
        if pos in self.reds and self.reds[pos] == self.current_target:
            reward = 10.0
            del self.reds[pos]
            self.current_target += 1

        # wrong red square
        elif pos in self.reds:
            reward = -5.0

        done = self.current_target > RED_COUNT
        return self.get_state(), reward, done

# -----------------------------
# TKINTER UI
# -----------------------------
root = tk.Tk()
root.title("Q-Learning Grid (14x14)")

canvas = tk.Canvas(
    root,
    width=GRID_SIZE * CELL_SIZE,
    height=GRID_SIZE * CELL_SIZE
)
canvas.pack()

info_label = tk.Label(root, text="", font=("Arial", 14))
info_label.pack()

def draw(env):
    canvas.delete("all")

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x1, y1 = j * CELL_SIZE, i * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE

            if WHITE_MIN <= i <= WHITE_MAX and WHITE_MIN <= j <= WHITE_MAX:
                color = "white"
            else:
                color = "black"

            canvas.create_rectangle(
                x1, y1, x2, y2,
                fill=color, outline="gray"
            )

    # red squares
    for (x, y), num in env.reds.items():
        canvas.create_rectangle(
            y * CELL_SIZE,
            x * CELL_SIZE,
            (y + 1) * CELL_SIZE,
            (x + 1) * CELL_SIZE,
            fill="red"
        )
        canvas.create_text(
            y * CELL_SIZE + CELL_SIZE // 2,
            x * CELL_SIZE + CELL_SIZE // 2,
            text=str(num),
            fill="white",
            font=("Arial", 16, "bold")
        )

    # blue agent
    ax, ay = env.agent
    canvas.create_rectangle(
        ay * CELL_SIZE,
        ax * CELL_SIZE,
        (ay + 1) * CELL_SIZE,
        (ax + 1) * CELL_SIZE,
        fill="blue"
    )

    tx, ty = env.get_next_target_pos()
    info_label.config(
        text=f"Current target: {env.current_target} | Next target at: ({tx},{ty})"
    )

# -----------------------------
# TRAINING LOOP (Tkinter-friendly)
# -----------------------------
env = GameEnv()
episode = 0

# episode state
state = env.reset()
done = False

def train_step():
    global episode, state, done

    if done:
        episode += 1
        print(f"Episode {episode} finished")
        state = env.reset()
        done = False

    draw(env)

    # epsilon-greedy
    if random.random() < epsilon:
        action = random.randint(0, 3)
    else:
        with torch.no_grad():
            action = torch.argmax(model(state)).item()

    next_state, reward, done = env.step(action)

    # Q-learning update
    qvals = model(state)
    q_val = qvals[action]

    with torch.no_grad():
        q_next = torch.max(model(next_state))
        target = torch.tensor(reward, dtype=torch.float32) + gamma * q_next * (0.0 if done else 1.0)

    loss = loss_fn(q_val, target)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    state = next_state

    # schedule next step
    root.after(60, train_step)

# start
train_step()
root.mainloop()
