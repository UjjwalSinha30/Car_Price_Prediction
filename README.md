# Car Price Prediction

A Machine Learning web application that predicts the selling price of used cars based on various features such as fuel type, kilometers driven, transmission type, and ownership details.

## Features
- Predicts used car selling price
- Machine Learning regression model
- User-friendly web interface
- Real-time prediction using Flask

## Tech Stack
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy

## Machine Learning Workflow
1. Data collection and preprocessing
2. Handling categorical data using one-hot encoding
3. Feature engineering
4. Model training using Random Forest Regression
5. Model serialization using Pickle
6. Prediction through Flask web application

## Project Structure

```bash
├── app.py
├── train_model.py
├── random_forest_regression_model.pkl
├── car data.csv
├── templates/
├── requirements.txt
├── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run Project

```bash
python app.py
```

## Machine Learning Concepts Used
- Regression
- Random Forest Regressor
- Feature Engineering
- One-Hot Encoding
- Model Serialization
- Flask Integration

## Dataset
The dataset contains information about used cars including:
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Ownership
- Manufacturing Year

## Future Improvements
- Improve UI design
- Deploy application online
- Add more regression models for comparison
- Improve prediction accuracy