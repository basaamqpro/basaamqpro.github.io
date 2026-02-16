"""
TensorFlow Core Learning Algorithms
Linear Classification with the Titanic Dataset

Author: Khalid Umar
Description:
This script demonstrates a linear classification model using TensorFlow
to predict passenger survival on the Titanic dataset.
"""

from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from IPython.display import clear_output
import tensorflow as tf
import tensorflow.compat.v2.feature_column as fc

# ===============================
# 1. Check TensorFlow Version
# ===============================
print("TensorFlow version:", tf.__version__)
print("-" * 60)

# ===============================
# 2. Load Dataset
# ===============================
dftrain = pd.read_csv(
    "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
)
dfeval = pd.read_csv(
    "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"
)

y_train = dftrain.pop("survived")
y_eval = dfeval.pop("survived")

print("Training shape:", dftrain.shape)
print("Evaluation shape:", dfeval.shape)
print("-" * 60)

# ===============================
# 3. Explore Data (Optional)
# ===============================
dftrain["age"].hist(bins=20)
plt.title("Age Distribution")
plt.show()

dftrain["sex"].value_counts().plot(kind="barh")
plt.title("Passenger Gender")
plt.show()

# ===============================
# 4. Feature Columns
# ===============================
CATEGORICAL_COLUMNS = [
    "sex", "n_siblings_spouses", "parch",
    "class", "deck", "embark_town", "alone"
]

NUMERIC_COLUMNS = ["age", "fare"]

feature_columns = []

for feature_name in CATEGORICAL_COLUMNS:
    vocabulary = dftrain[feature_name].unique()
    feature_columns.append(
        tf.feature_column.categorical_column_with_vocabulary_list(
            feature_name, vocabulary
        )
    )

for feature_name in NUMERIC_COLUMNS:
    feature_columns.append(
        tf.feature_column.numeric_column(
            feature_name, dtype=tf.float32
        )
    )

# ===============================
# 5. Input Function
# ===============================
def make_input_fn(data_df, label_df,
                  num_epochs=10,
                  shuffle=True,
                  batch_size=32):

    def input_function():
        ds = tf.data.Dataset.from_tensor_slices(
            (dict(data_df), label_df)
        )
        if shuffle:
            ds = ds.shuffle(1000)
        ds = ds.batch(batch_size).repeat(num_epochs)
        return ds

    return input_function


train_input_fn = make_input_fn(dftrain, y_train)
eval_input_fn = make_input_fn(
    dfeval, y_eval,
    num_epochs=1,
    shuffle=False
)

# ===============================
# 6. Create Model
# ===============================
linear_estimator = tf.estimator.LinearClassifier(
    feature_columns=feature_columns
)

# ===============================
# 7. Train Model
# ===============================
linear_estimator.train(train_input_fn)

# ===============================
# 8. Evaluate Model
# ===============================
result = linear_estimator.evaluate(eval_input_fn)

clear_output()
print("Model Accuracy:", result["accuracy"])
print("-" * 60)

# ===============================
# 9. Make Predictions
# ===============================
predictions = list(
    linear_estimator.predict(eval_input_fn)
)

probabilities = pd.Series(
    [pred["probabilities"][1] for pred in predictions]
)

probabilities.plot(
    kind="hist",
    bins=20,
    title="Predicted Survival Probabilities"
)

plt.show()

print("End of program.")
