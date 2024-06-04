from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

# Load the model
model = joblib.load("credit_model.pkl")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    df = pd.DataFrame([data])

    # Convert numerical features to numeric types
    df["Age"] = pd.to_numeric(df["Age"])
    df["Job"] = pd.to_numeric(df["Job"])
    df["Credit amount"] = pd.to_numeric(df["Credit amount"])
    df["Duration"] = pd.to_numeric(df["Duration"])

    prediction = model.predict(df)
    return render_template('index.html', prediction=int(prediction[0]))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
