import tensorflow as tf
from sklearn.preprocessing import StandardScaler

classified_model = tf.keras.models.load_model("D:\laragon\www/boxqt\CNN\classified_model")
# regresstion_model = tf.keras.models.load_model("D:\laragon\www/boxqt\CNN/regression_model")

raw_data = [['0.33,1.10,-9.45,-0.01,0.00,-0.00'], ['0.38,0.98,-9.49,-0.01,0.00,-0.00'], ['0.29,1.07,-9.54,-0.01,0.00,-0.01'], ['0.33,1.07,-9.52,-0.01,-0.00,-0.01'], ['0.25,1.05,-9.51,-0.01,-0.01,-0.00'], ['0.48,1.00,-9.55,-0.00,-0.00,-0.01'], ['0.37,1.17,-9.51,-0.01,-0.00,-0.01'], ['0.24,1.14,-9.60,-0.02,0.00,-0.01'], ['0.42,1.12,-9.49,-0.01,0.00,-0.00'], ['0.34,0.98,-9.54,0.00,-0.00,-0.00'], ['0.39,1.03,-9.46,-0.01,0.00,0.00'], ['0.31,1.01,-9.43,-0.01,0.00,-0.00'], ['0.34,1.11,-9.48,-0.00,0.00,-0.01'], ['0.35,1.10,-9.41,-0.01,0.00,-0.00'], ['0.33,1.04,-9.50,-0.01,-0.00,-0.00'], ['0.38,1.06,-9.50,-0.00,-0.01,-0.01'], ['0.39,1.19,-9.58,-0.01,-0.01,-0.00'], ['0.31,1.06,-9.58,0.00,-0.01,-0.00'], ['0.33,1.00,-9.63,0.00,-0.00,-0.00'], ['0.36,1.07,-9.47,-0.01,-0.01,-0.01'], ['0.25,1.07,-9.58,-0.01,-0.00,-0.00'], ['0.26,1.13,-9.51,-0.01,0.00,-0.00'], ['0.37,1.05,-9.42,0.00,0.00,-0.00'], ['0.36,1.18,-9.50,-0.01,0.00,-0.00'], ['0.33,1.14,-9.49,-0.01,0.00,-0.00'], ['0.32,1.00,-9.52,-0.00,-0.00,0.00'], ['0.27,1.05,-9.54,-0.01,-0.00,-0.01'], ['0.25,1.03,-9.61,-0.01,-0.00,-0.00'], ['0.37,1.16,-9.50,-0.01,-0.00,-0.01'], ['0.43,0.99,-9.56,-0.00,0.00,-0.01'], ['0.32,1.05,-9.47,-0.00,0.00,-0.00'], ['0.37,1.06,-9.50,-0.00,0.00,-0.00'], ['0.29,1.03,-9.36,-0.00,-0.00,-0.00'], ['0.30,1.00,-9.49,-0.01,0.00,-0.01'], ['0.33,1.13,-9.49,-0.01,0.00,-0.01'], ['0.41,1.17,-9.53,-0.01,-0.00,-0.00'], ['0.33,1.13,-9.49,0.00,-0.00,-0.01'], ['0.35,1.09,-9.52,-0.00,-0.00,-0.01'], ['0.27,1.09,-9.45,-0.00,-0.00,-0.01'], ['0.37,1.06,-9.54,-0.01,-0.00,-0.01']]

X_test_scaled = StandardScaler().fit_transform(raw_data)
X_test = X_test_scaled.reshape(2, 20, 6, 1)

classified_model.predict(X_test)

