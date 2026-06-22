import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
df = pd.read_csv("data/StudentsPerformance.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nPerformance Distribution:")
print(df["performance"].value_counts())

# Features
X = df.drop(["student_id", "performance"], axis=1)

# Target
y = df["performance"]

# Encode Labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

# Train Model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save Model
with open("models/trained_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

# Save Encoder
with open("models/encoder.pkl", "wb") as encoder_file:
    pickle.dump(encoder, encoder_file)

print("\nModel trained and saved successfully!")