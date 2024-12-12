from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__)
# Set to False in production
app.config['DEBUG'] = False
# Add secret key for session security
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Stock configuration with probabilities
STOCKS = {
    'tesla': {
        'name': 'Tesla',
        'probability': 0.45,
        'image': 'tesla.jpg',
        'search_url': 'https://www.google.com/search?q=Tesla+stock'
    },
    'absci': {
        'name': 'ABSCI',
        'probability': 0.45,
        'image': 'absci.jpg',
        'search_url': 'https://www.google.com/search?q=ABSCI+stock'
    },
    'secret': {
        'name': '?',
        'probability': 0.1,
        'image': 'surprise.jpg',
        'search_url': 'https://blog.naver.com/daily_life_diary',
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pick_gift')
def pick_gift():
    try:
        choices = []
        probabilities = []
        
        for key, value in STOCKS.items():
            choices.append(key)
            probabilities.append(value['probability'])
        
        selected = random.choices(choices, probabilities)[0]
        return jsonify(STOCKS[selected])
    except Exception as e:
        app.logger.error(f"Error in pick_gift: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

# Add basic health check endpoint
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    # Use production server when running directly
    app.run(host='0.0.0.0', port=8080) 