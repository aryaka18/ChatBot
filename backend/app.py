# backend/app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from utils.text_processor import TextProcessor
from utils.constants import KEYWORDS, RESPONSES
import os

app = Flask(__name__)
CORS(app)

# Add static folder for images
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/images')

text_processor = TextProcessor()

@app.route('/static/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question', '')
    
    tokens = text_processor.preprocess_text(question)
    corrected_tokens = [text_processor.auto_correct(token) for token in tokens]
    
    response_type = None
    for token in corrected_tokens:
        if token in KEYWORDS:
            response_type = KEYWORDS[token]
            break
    
    response_data = RESPONSES.get(response_type, {'text': 'Maaf, saya tidak mengerti pertanyaan Anda.'})
    
    # Return both text and image if available
    return jsonify({
        'response': response_data.get('text'),
        'image': response_data.get('image')
    })
if __name__ == '__main__':
    app.run(debug=True)
    

a = 1
b = "string"
c = 1.9

tambah = a + c
print (tambah)
