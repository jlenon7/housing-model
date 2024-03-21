import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow.keras.models as keras

from os.path import exists
from typing import Optional
from tensorflow.keras.layers import Dense

class Path:
  def plots(self, path: Optional[str]):
    path = self.clean_path(path)

    return f'storage/plots/{path}'

  def storage(self, path: Optional[str]):    
    path = self.clean_path(path) 

    return f'storage{path}'

  def resources(self, path: Optional[str]):    
    path = self.clean_path(path) 

    return f'resources{path}'

  def clean_path(self, path: Optional[str]):
    if path is None:
      return ''

    if path.endswith('/') is True:
      path = path[:-1]

    if path.startswith('/') is True:
      return path 

    return f'/{path}'

path = Path()

def load_model():
  model_exists = exists('storage/housing-model.keras')

  if (model_exists):
    return keras.load_model('storage/housing-model.keras')

  model = keras.Sequential()

  model.add(Dense(19, activation='relu'))
  model.add(Dense(19, activation='relu'))
  model.add(Dense(19, activation='relu'))
  model.add(Dense(19, activation='relu'))
  model.add(Dense(1))

  model.compile(optimizer='adam', loss='mse')

  return model

def create_df(file_path: str, with_plots = True):
  df = pd.read_csv(file_path) 

  df['date'] = pd.to_datetime(df['date'])
  df['year'] = df['date'].apply(lambda date: date.year)
  df['month'] = df['date'].apply(lambda date: date.month)

  df = df.sort_values('price', ascending=False) \
    .iloc[216:] \
    .drop('id', axis=1) \
    .drop('date', axis=1) \
    .drop('zipcode', axis=1)

  if (with_plots is True):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='bedrooms', data=df) \
      .figure \
      .savefig(path.plots('dataframe/c-bedrooms.png')) 

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='bedrooms', y='price', data=df) \
      .figure \
      .savefig(path.plots('dataframe/pd-per-bedrooms.png')) 

    plt.figure(figsize=(12, 8))
    sns.scatterplot(
      x='long', 
      y='lat', 
      data=df, 
      hue='price', 
      edgecolor=None, 
      alpha=0.2, 
      palette='RdYlGn'
    ).figure.savefig(path.plots('dataframe/pd-king-county.png'))

    plt.figure(figsize=(12, 8))
    sns.boxplot(x='waterfront', y='price', data=df) \
      .figure \
      .savefig(path.plots('dataframe/pd-per-waterfront.png'))

    plt.figure(figsize=(10, 6))
    df.groupby('month') \
      .mean()['price'] \
      .plot() \
      .figure \
      .savefig(path.plots('dataframe/pd-per-month.png'))

    plt.figure(figsize=(10, 6))
    df.groupby('year') \
      .mean()['price'] \
      .plot() \
      .figure \
      .savefig(path.plots('dataframe/pd-per-year.png'))

  return df
