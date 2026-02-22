import tkinter as tk
import math
import random
from collections import defaultdict

# -----------------------------
# Parameters
# -----------------------------
parent_radius = 250
child_radius = 5
step_size = 6
update_ms = 30

WIDTH = HEIGHT = parent_radius * 2
CENTER = parent_radius

# Red obstacles (x, y, r)
red_circles = [
    (CENTER, CENTER, 120),
    (CENTER + 90, CENTER - 40, 40),
    (CENTER - 110, CENTER + 70, 35),
]

# Q-learning
alpha = 0.1
gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.999
min_epsilon = 0.05

ACTIONS = [
    -math.pi/4, 0, math.pi/4,
    math.pi/2, 3*math.pi/4,
    math.pi, -3*math.pi/4,
    -math.pi/2
]

Q = defaultdict(lambda: [0.0] * len(ACTIONS))

# -----------------------------
# Geometry helpers
# -----------------------------
def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def inside_green(pos):
    return distance(pos, (CENTER, CENTER)) <= parent_radius - child_radius

def outside_all_red(pos):
    for rx, ry, rr in red_circles:
        if distance(pos, (rx, ry)) <= rr + child_radius:
            return False
    return True

def valid(pos):
    return inside_green(pos) and outside_all_red(pos)

# -----------------------------
# State encoding
# -----------------------------
def angle_bucket(agent, target):
    if not target:
        return 0
    dx = target[0] - agent[0]
    dy = target[1] - agent[1]
    angle = math.atan2(dy, dx)
    return int(((angle + math.pi) / (2 * math.pi)) * 8) % 8

def obstacle_bucket(agent):
    min_d = min(distance(agent, (rx, ry)) - rr for rx, ry, rr in red_circles)
    if min_d < 20:
        return 0
    elif min_d < 50:
        return 1
    return 2

def get_state(agent, target):
    return (angle_bucket(agent, target), obstacle_bucket(agent))

# -----------------------------
# App
# -----------------------------
class App:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.canvas.create_oval(0, 0, WIDTH, HEIGHT, fill="green")

        for rx, ry, rr in red_circles:
            self.canvas.create_oval(
                rx - rr, ry - rr,
                rx + rr, ry + rr,
                fill="red"
            )

        self.agent = self.random_pos()
        self.agent_id = self.canvas.create_oval(0,0,0,0, fill="blue")
        self.update_agent()

        self.target = None
        self.target_id = None
        self.canvas.bind("<Button-1>", self.place_target)

        self.angle = random.uniform(0, 2*math.pi)
        self.loop()

    def random_pos(self):
        while True:
            p = [random.uniform(0, WIDTH), random.uniform(0, HEIGHT)]
            if valid(p):
                return p

    def place_target(self, e):
        pos = [e.x, e.y]
        if valid(pos):
            self.target = pos
            if self.target_id:
                self.canvas.delete(self.target_id)
            self.target_id = self.canvas.create_oval(
                pos[0]-5, pos[1]-5, pos[0]+5, pos[1]+5,
                fill="orange"
            )

    def update_agent(self):
        x, y = self.agent
        self.canvas.coords(
            self.agent_id,
            x-child_radius, y-child_radius,
            x+child_radius, y+child_radius
        )

    def step(self):
        global epsilon

        state = get_state(self.agent, self.target)

        if random.random() < epsilon:
            action = random.randint(0, len(ACTIONS)-1)
        else:
            action = max(range(len(ACTIONS)), key=lambda a: Q[state][a])

        self.angle += ACTIONS[action]

        nx = self.agent[0] + math.cos(self.angle) * step_size
        ny = self.agent[1] + math.sin(self.angle) * step_size
        new_pos = [nx, ny]

        reward = -0.1

        if not valid(new_pos):
            reward = -20
            new_pos = self.agent
        elif self.target:
            if distance(new_pos, self.target) < step_size:
                reward = 50
                self.canvas.delete(self.target_id)
                self.target = None
                self.target_id = None
            else:
                reward = 1

        next_state = get_state(new_pos, self.target)

        Q[state][action] += alpha * (
            reward + gamma * max(Q[next_state]) - Q[state][action]
        )

        self.agent = new_pos
        self.update_agent()

        epsilon = max(min_epsilon, epsilon * epsilon_decay)

    def loop(self):
        self.step()
        self.root.after(update_ms, self.loop)

# -----------------------------
# Run
# -----------------------------
root = tk.Tk()
root.title("Q-Learning Agent with Obstacles")
App(root)
root.mainloop()
