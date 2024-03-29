import numpy as np
import pandas as pd
import boto3
import os

access_key = os.environ.get("AWS_ACCESS_KEY_ID")
secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
bucket_name = os.environ.get("Bucket_Name")
s3 = boto3.client('s3', aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key,
                      region_name='us-east-1')
obj = s3.get_object(Bucket=bucket_name, Key='airflow-jenkins/rawdata.csv')
data = pd.read_csv(obj['Body'])
#data = pd.read_csv('data.csv')
print(data.info())
print(data.describe())
print("Features in the data:", data.columns)
print(data.isnull().sum())   # finding the missing values
print("No missing Values Found") 
print(data.duplicated().sum())  # finding the duplicate values
# getting the number of unique values in each feature
for column in data.columns:
    print(column,data[column].nunique())
# finding the number of numerical and categorical features
categorical_features = data.select_dtypes("object").columns
numerical_features = data.select_dtypes("number").columns
print("Categorical: ",categorical_features)
print("Numerical: ",numerical_features)
#    return data, numerical_features, categorical_features

#analyse_data()
