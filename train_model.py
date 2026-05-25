import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

car_dataset = pd.read_csv('car data.csv')

# Creating new feature
car_dataset['Current_Year'] = 2026
car_dataset['no_year'] = car_dataset['Current_Year'] - car_dataset['Year']

# Drop unused columns
final_dataset = car_dataset.drop(['Car_Name','Year','Current_Year'], axis=1)

# Convert categorical data
final_dataset = pd.get_dummies(final_dataset, drop_first=True)

# Features and target
X = final_dataset.drop(['Selling_Price'], axis=1)
y = final_dataset['Selling_Price']

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
pickle.dump(model, open('random_forest_regression_model.pkl', 'wb'))

print("Model trained successfully")