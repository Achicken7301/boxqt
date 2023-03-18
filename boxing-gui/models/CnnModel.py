import pandas as pd
from sklearn.preprocessing import StandardScaler


class CnnModel:
    def __init__(self) -> None:
        import tensorflow as tf

        self.classified_model = tf.keras.models.load_model(
            "D:\laragon\www/boxqt\CNN\classified_model"
        )
        self.regresstion_model = tf.keras.models.load_model(
            "D:/laragon/www/boxqt/CNN/regression_model"
        )

    def classification_prediction(self, data: pd.DataFrame) -> list:
        X_scaled = StandardScaler().fit_transform(data)
        X_test = X_scaled.reshape(1, 20, 6, 1)
        return self.classified_model.predict(X_test)
