# NetShield AI

This project is a Machine Learning system for detecting network security threats using classification models.

## Features

- Data ingestion from MongoDB
- Data validation and preprocessing
- Model training with multiple ML algorithms
- MLflow tracking for experiments
- FastAPI backend for prediction
- Simple HTML frontend dashboard

Critical Setup Flow (Train Before Predict)

Because the web dashboard relies on serialized model artifacts, you **must train the model first** before uploading a file for testing/prediction.

### Step 1: Run the Training Pipeline
Before making any predictions, trigger the model training endpoint to fetch data from MongoDB, train the classifiers, log metrics to MLflow, and save the final pipeline models.
Open your browser and go to:
    https://netshield-ai.onrender.com/train
    Expected Output:
    { "message": "Training completed successfully" }

### Step 2: Test Data & Run Predictions
Once the training step finishes successfully, your application is ready to predict network threats.

Go to the home dashboard: https://netshield-ai.onrender.com

    Select your testing data CSV file.

    Click the Predict button.

    The application will render a formatted HTML table displaying your data alongside the new live predictions.