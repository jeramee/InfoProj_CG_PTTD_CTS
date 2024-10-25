# random_forest_classifier.py

from Bio import SeqIO
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Example: Extract sequence length from a FASTA file
fasta_file = "example.fasta"
sequence_lengths = []
for record in SeqIO.parse(fasta_file, "fasta"):
    sequence_lengths.append(len(record.seq))

# Create a dataset from the sequence lengths
X = pd.DataFrame({'seq_length': sequence_lengths})
y = [0, 1, 0, 1]  # Replace with actual labels

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
