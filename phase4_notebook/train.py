# train.py
import subprocess
import sys

# Install fsspec package
subprocess.check_call([sys.executable, "-m", "pip", "install", "fsspec"])

import argparse
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

import joblib

def model_fn(model_dir = None):
    """
    Load the scikit-learn model from the `model_dir` directory.
    """
    model = joblib.load(os.path.join(os.environ['SM_MODEL_DIR'], "model.joblib"))
    return model


if __name__ == '__main__':
    # Parse arguments passed to the script
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    args = parser.parse_args()

    # Load data from the specified directory
    data = pd.read_csv(os.path.join(args.train, 'training_dataset.csv'))
    
    # Select relevant features and target variable
    X = data[['reviews', 'price']]
    y = data['isBestSeller']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a logistic regression model
    model = LogisticRegression()

    # Train the model on the training data
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))

    # Save the trained model
    joblib.dump(model, os.path.join(os.environ['SM_MODEL_DIR'], 'model.joblib'))
