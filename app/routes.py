from flask import Blueprint, request, jsonify, render_template, send_from_directory
import pickle

main = Blueprint('main', __name__)

# Model va vektorizerni yuklash
with open('models/sentiment_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('models/vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

@main.route('/predict', methods=['POST'])
def predict():
    # Foydalanuvchi tomonidan yuborilgan matnni olish
    data = request.get_json()
    
    if 'text' not in data:
        return jsonify({'error': 'No text provided!'}), 400

    text = data['text']
    
    # Matnni vektorlashtirish
    text_vectorized = vectorizer.transform([text])
    
    # Sentimentni bashorat qilish
    prediction = model.predict(text_vectorized)[0]
    sentiment = 'Positive' if prediction == 1 else 'Negative'

    # Javobni yuborish
    return jsonify({'text': text, 'sentiment': sentiment})
