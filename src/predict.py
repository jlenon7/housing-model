from helpers import path, create_df, load_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

df = create_df(path.resources('housing.csv'), with_plots=False)

X = df.drop('price', axis=1).values
y = df['price'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = load_model()

original_house = df.sample()
scaled_house = scaler.transform(original_house.drop('price', axis=1).values.reshape(-1, 19))
single_house_prediction = model.predict(scaled_house)

print()
print('Single house sold price:     ', original_house['price'].iloc[0])
print('Single house predicted price:', single_house_prediction[0][0])
