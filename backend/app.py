from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load('./model/sentiment_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    prediction = model.predict([text])[0]
    sentiment = "Positive" if prediction == 1 else "Negative"
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
