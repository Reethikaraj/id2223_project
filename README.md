# id2223_PROJECT

# S&P 500 Stock Price Prediction

## Contributors

Reethika Ambatipudi
Deepak Shankar

## Overview

This project aims to predict the closing value of the S&P 500 stock using machine learning, specifically employing Linear Regression as the chosen algorithm. The prediction model is built on the Yahoo Finance dataset. The project is organized into different pipelines, each serving a specific purpose.

## Pipelines

### 1. EDA and Backfill

In this pipeline, Exploratory Data Analysis (EDA) is performed to understand the characteristics of the dataset.

1. We have removed the irrelevant columns - Dividends and Stock splits.
2. Considered the data only from 1990.
3. Checked for any missing data and found none.
4. Though there was high correlation between the columns, all those were important and let them be in the data.
5. Stored the features in Hopsworks FeatureGroup.

### 2. Training

The Training pipeline focuses on building the prediction model. We have tried Linear Regression and RandomForestRegression models. Also did Hyper parameter tuning for both the models.

Linear Regression was identified as the most suitable algorithm based on evaluation metrics, with Mean Squared Error (MSE) being the primary metric. The trained model is ready for deployment.

Linear Regression - MSE - Before Hyperparameter Tuning - 46.9413
After Hyperparameter Tuning - 46.9513

Random Forest Regression - Before Hyperparameter Tuning - 85.4987
After Hyperparameter Tuning - 84.42946

We saved the Linear Regression model to Hopsworks and used it.

### 3. Batch Inference

The Batch Inference pipeline is responsible for making predictions on a batch of data. It utilizes the trained Linear Regression model to generate predictions for the closing values of the S&P 500 stock.

### 4. Feature Pipeline Daily

This pipeline deals with the daily extraction and processing of features required for model training and inference. It ensures that the model stays up-to-date with the latest data. We used Github actions and MOdal to trigger the action daily.

## Model Evaluation

The performance of the Linear Regression model is evaluated using Mean Squared Error (MSE), with a resulting MSE value of 46.9413. This metric provides insights into how well the model is performing in terms of predicting the closing values.

Hugging face URL for the monitor - https://huggingface.co/spaces/Reethika23/sp500
