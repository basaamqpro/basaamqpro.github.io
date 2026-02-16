# ============================================================
# Lesson 2 (Part 2): Titanic Survival Prediction (TensorFlow)
# FULL WORKING VERSION — TensorFlow 2.20+
# ============================================================

import tensorflow as tf
import pandas as pd
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "train.csv")

df = pd.read_csv(DATA_PATH)

from sklearn.model_selection import train_test_split

print("TensorFlow version:", tf.__version__)
print("-" * 60)

# ============================================================
# 1. LOAD DATASET
# ============================================================

# IMPORTANT:
# Run this script from:
# gpt/freecodecamp_tutorial/lesson2/
# And ensure the file is located at:
# gpt/freecodecamp_tutorial/lesson2/data/train.csv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "train.csv")

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully")
print("Shape:", df.shape)
print("-" * 60)

# ============================================================
# 2. SELECT FEATURES & LABEL
# ============================================================

FEATURES = [
    "Age",
    "Fare",
    "Pclass",
    "SibSp",
    "Parch",
    "Sex",
    "Embarked"
]

LABEL = "Survived"

df = df[FEATURES + [LABEL]]

# ============================================================
# 3. HANDLE MISSING VALUES (SAFE WAY)
# ============================================================

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("Missing values handled")
print("-" * 60)

# ============================================================
# 4. SPLIT TRAIN / EVALUATION
# ============================================================

train_df, eval_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

train_labels = train_df.pop(LABEL)
eval_labels = eval_df.pop(LABEL)

print(f"Training samples: {len(train_df)}")
print(f"Evaluation samples: {len(eval_df)}")
print("-" * 60)

# ============================================================
# 5. BUILD INPUT PIPELINE (CRITICAL FIX)
# ============================================================

def df_to_dataset(df, labels, shuffle=True, batch_size=32):
    df = df.copy()

    # Ensure correct dtypes
    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            df[col] = df[col].astype("float32")
        else:
            df[col] = df[col].astype(str)

    ds = tf.data.Dataset.from_tensor_slices((dict(df), labels))

    if shuffle:
        ds = ds.shuffle(buffer_size=len(df))

    return ds.batch(batch_size)


train_ds = df_to_dataset(train_df, train_labels, shuffle=True)
eval_ds = df_to_dataset(eval_df, eval_labels, shuffle=False)

# ============================================================
# 6. BUILD PREPROCESSING LAYERS
# ============================================================

inputs = {}

# Numeric features
numeric_features = ["Age", "Fare", "Pclass", "SibSp", "Parch"]
encoded_features = []

for feature in numeric_features:
    inp = tf.keras.Input(shape=(1,), name=feature)
    norm = tf.keras.layers.Normalization()
    norm.adapt(train_df[feature].values.reshape(-1, 1))
    encoded = norm(inp)

    inputs[feature] = inp
    encoded_features.append(encoded)

# Categorical: Sex
sex_input = tf.keras.Input(shape=(1,), name="Sex", dtype=tf.string)
sex_lookup = tf.keras.layers.StringLookup(output_mode="one_hot")
sex_lookup.adapt(train_df["Sex"])
sex_encoded = sex_lookup(sex_input)

inputs["Sex"] = sex_input
encoded_features.append(sex_encoded)

# Categorical: Embarked
emb_input = tf.keras.Input(shape=(1,), name="Embarked", dtype=tf.string)
emb_lookup = tf.keras.layers.StringLookup(output_mode="one_hot")
emb_lookup.adapt(train_df["Embarked"])
emb_encoded = emb_lookup(emb_input)

inputs["Embarked"] = emb_input
encoded_features.append(emb_encoded)

# ============================================================
# 7. BUILD MODEL
# ============================================================

x = tf.keras.layers.Concatenate()(encoded_features)

# Logistic regression (same idea as LinearClassifier)
output = tf.keras.layers.Dense(1, activation="sigmoid")(x)

model = tf.keras.Model(inputs=inputs, outputs=output)

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()
print("-" * 60)

# ============================================================
# 8. TRAIN MODEL (NO DTYPE ERRORS)
# ============================================================

history = model.fit(
    train_ds,
    validation_data=eval_ds,
    epochs=10
)

# ============================================================
# 9. EVALUATION
# ============================================================

loss, accuracy = model.evaluate(eval_ds)
print(f"Evaluation Accuracy: {accuracy:.4f}")
