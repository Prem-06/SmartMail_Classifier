from flask import Flask, request, jsonify
from waitress import serve
import joblib
import re
import nltk
from flask_cors import CORS
import numpy as np
nltk.download('stopwords')
from nltk.corpus import stopwords
def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    stop_words = set(stopwords.words('english'))
    words = text.split()
    text = ' '.join([word for word in words if word not in stop_words])
    return text

model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def predict_category(model, vectorizer, text):
    processed_text = preprocess_text(text)
    text_vector = vectorizer.transform([processed_text])
    return model.predict(text_vector)[0]

app = Flask(__name__)
CORS(app)
@app.route('/process', methods=['POST'])
def process_input():
    try:
        data = request.json['texts']
        if not isinstance(data, list):
            return jsonify({'error': 'Input should be a list of texts'}), 400
        res = []
        for text in data:
            category = predict_category(model, vectorizer, text)
            res.append(category)
        return jsonify({'category': res})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
