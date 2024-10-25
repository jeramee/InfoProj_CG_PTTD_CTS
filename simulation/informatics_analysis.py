# informatics_analysis.py

import gseapy as gp
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline

def perform_gsea(expression_data):
    # Convert gene symbols to uppercase
    expression_data.index = expression_data.index.astype(str).str.upper()

    # Define class labels (adjust this based on your data)
    cls = ['Control', 'Control', 'Control', 'Treatment', 'Treatment', 'Treatment']

    # Run GSEA with adjusted min_size and max_size
    try:
        gsea_results = gp.gsea(
            data=expression_data, 
            gene_sets='KEGG_2016', 
            cls=cls, 
            outdir='gsea_results', 
            min_size=2,  # Lowering the min_size to capture more gene sets
            max_size=10000  # Increasing the max_size to allow larger gene sets
        )
        print(gsea_results.res2d.head())
    except LookupError as e:
        print(f"GSEA Error: {e}")

def logistic_regression(X_train, y_train, X_test, y_test):
    """
    Train and test a logistic regression model for binary classification tasks.
    
    Args:
        X_train (DataFrame): Training data features.
        y_train (Series): Training data labels.
        X_test (DataFrame): Testing data features.
        y_test (Series): Testing data labels.
    
    Returns:
        None
    """
    y_train_series = y_train.squeeze()
    if len(y_train_series.unique()) < 2:
        print("Error: Logistic regression requires at least 2 classes in the training set.")
        return
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), X_train.select_dtypes(include=['object']).columns)],
        remainder='passthrough'
    )
    log_model = make_pipeline(preprocessor, LogisticRegression(max_iter=1000))
    log_model.fit(X_train, y_train_series.values.ravel())
    accuracy = log_model.score(X_test, y_test)
    print(f"Logistic Regression Accuracy: {accuracy:.2f}")
