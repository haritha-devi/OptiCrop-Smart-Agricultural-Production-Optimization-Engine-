from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = pd.DataFrame({
        "N": [float(request.form["N"])],
        "P": [float(request.form["P"])],
        "K": [float(request.form["K"])],
        "temperature": [float(request.form["temperature"])],
        "humidity": [float(request.form["humidity"])],
        "ph": [float(request.form["ph"])],
        "rainfall": [float(request.form["rainfall"])]
    })

    prediction = model.predict(data)[0]

    return render_template("result.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)