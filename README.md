# Credit Score Prediction App

This repository contains a credit score prediction app built with Flask and a machine learning model trained using scikit-learn. The app allows users to input their information and receive a credit score prediction.

## Project Structure

- `app.py`: The Flask web application.
- `train.py`: The script to train the machine learning model.
- `german_credit_risk.csv`: The dataset used for training.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Dockerfile for the Flask app.
- `Dockerfile.train`: Dockerfile for the training script.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory containing CSS files.

## Setup Instructions

### Training the Model

1. Build the Docker image for training:
    ```sh
    docker build -f Dockerfile.train -t credit-score-training .
    ```

2. Run the Docker container for training:
    ```sh
    docker run --rm -v $(pwd):/app credit-score-training
    ```

### Running the Flask App

1. Build the Docker image for the Flask app:
    ```sh
    docker build -t credit-score-app .
    ```

2. Run the Docker container for the Flask app:
    ```sh
    docker run -p 5000:5000 credit-score-app
    ```

3. Open your web browser and navigate to `http://localhost:5000` to access the app.

## Contributing

Feel free to submit issues or pull requests if you find any bugs or want to add new features.
