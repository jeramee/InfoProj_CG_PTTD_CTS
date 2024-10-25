# genome_cancer_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_chip_seq_data(filepath):
    """
    Load and visualize ChIP-Seq data from a CSV file. The function plots the coverage
    of peaks across different chromosomes.
    
    Args:
        filepath (str): Path to the ChIP-Seq data file.
    """
    chip_seq_data = pd.read_csv(filepath)
    chip_seq_data['chromosome'].value_counts().plot(kind='bar')
    plt.title('ChIP-Seq Peak Coverage by Chromosome')
    plt.show()

def process_genomic_sequences(filepath):
    """
    Parse genomic sequences from a FASTA file and print the chromosome ID and sequence length.
    
    Args:
        filepath (str): Path to the FASTA file containing genomic sequences.
    """
    for seq_record in SeqIO.parse(filepath, "fasta"):
        print(f"Chromosome: {seq_record.id}, Length: {len(seq_record)}")

def random_forest_classifier(X_train, y_train, X_test, y_test):
    """
    Train a Random Forest classifier on genomic data and evaluate its accuracy.
    
    Args:
        X_train (DataFrame): Training data features.
        y_train (Series): Training data labels.
        X_test (DataFrame): Testing data features.
        y_test (Series): Testing data labels.
    
    Returns:
        RandomForestClassifier: Trained Random Forest model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    return model
