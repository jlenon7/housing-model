import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from helpers import path, create_df, load_model
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import mean_absolute_error, mean_squared_error, explained_variance_score

df = create_df(path.resources('housing.csv'))

X = df.drop('price', axis=1).values
y = df['price'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = load_model()

model.fit(
  x=X_train,
  y=y_train,
  validation_data=(X_test,y_test),
  batch_size=128,
  epochs=2000,
  callbacks=[
    EarlyStopping(
      monitor='val_loss',
      mode='min',
      verbose=1,
      patience=25
    )
  ]
)

pd.DataFrame(model.history.history) \
  .plot() \
  .figure \
  .savefig(path.plots('model/is-overfitting-train-test-data.png'))

predictions = model.predict(X_test)

print()
print('Mean Absolute Error:', mean_absolute_error(y_test, predictions))
print('Mean Squared Error:', mean_squared_error(y_test, predictions))
print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, predictions)))
print('Explained Variance Regression Score:', explained_variance_score(y_test, predictions))

plt.figure(figsize=(12,6))
plt.scatter(y_test, predictions)
plt.plot(y_test, y_test, 'r')
plt.savefig(path.plots('model/predictions.png'))

print()
print('Saving the model at', path.storage('housing-model.keras'))
model.save(path.storage('housing-model.keras'))
