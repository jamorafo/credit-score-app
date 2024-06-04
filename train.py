import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier

# Load dataset from local file
file_path = "german_credit_risk.csv"
data = pd.read_csv(file_path)

# Print column names for debugging
print(data.columns)

# Update the column names based on the new dataset
# 'Risk' is the target column
target_column = "Risk"

# Separate features and target
X = data.drop(target_column, axis=1)
y = data[target_column].apply(lambda x: 1 if x == 'good' else 0)

# Update these lists based on the actual feature names in your dataset
numerical_features = ["Age", "Job", "Credit amount", "Duration"]
categorical_features = ["Sex", "Housing",
                        "Saving accounts", "Checking account", "Purpose"]

numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create and train the model
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))])

model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "credit_model.pkl")

print("Model training completed and saved as credit_model.pkl")
