from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory

from werkzeug.utils import secure_filename
import os
from model import predict_image, load_model_hybrid

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

model, scaler = load_model_hybrid()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Perform prediction
        prediction = predict_image(filepath, model, scaler)
        class_labels = {
            0: 'WPW', 1: 'SVTA', 2: 'APB', 3: 'RBBBB', 4: 'IVR', 
            5: 'AFIB', 6: 'PVC', 7: 'NSR', 8: 'Fusion', 9: 'Trigeminy',
            10: 'AFL', 11: 'VFL', 12: 'LBBBB', 13: 'SDHB', 
            14: 'Bigeminy', 15: 'PR', 16: 'VT'
        }
        
        return render_template('result.html', prediction=class_labels[prediction], image_url=url_for('uploaded_file', filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
