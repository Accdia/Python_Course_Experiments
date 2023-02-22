import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    data = pd.read_csv("income.csv")

    y_test = data.Income
    x_test = data.Education

    color = np.arctan2(x_test, y_test)
    plt.scatter(x_test, y_test, c=color)
    plt.show()

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(1, input_shape=(1,)))
    model.compile(
        optimizer="adam",
        loss="mse"
    )

    history = model.fit(x_test, y_test, epochs=5000)
    print(model.predict([[20]]))
