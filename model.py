import scipy.io
import numpy as np
import tensorflow as tf
from joblib import load

def load_model_hybrid():
    loaded_model = tf.keras.models.load_model("D:/MPPPPP/bilstm_cnn_attention/best_model.keras")
    scaler = load("D:/MPPPPP/bilstm_cnn_attention/ecg_scaler.joblib")
    return loaded_model, scaler


def predict_image(image_path, model, scaler):
    mat_data = scipy.io.loadmat(image_path)
    ecg_scaled = scaler.transform(mat_data['val'][0].reshape(1, -1))
    processed_signal = ecg_scaled.reshape(1, 3600, 1)
    predictions = model.predict(processed_signal)
    predicted_class_idx = np.argmax(predictions)
    return predicted_class_idx

if __name__ == "__main__":
    # Load the model
    loaded_model, scaler = load_model_hybrid()
    
    image_path = "D:/MLII/7 PVC/105m (5).mat"


    predicted_class_index = predict_image(image_path, loaded_model, scaler)
    
    class_labels = {
            0: 'WPW', 1: 'SVTA', 2: 'APB', 3: 'RBBBB', 4: 'IVR', 
            5: 'AFIB', 6: 'PVC', 7: 'NSR', 8: 'Fusion', 9: 'Trigeminy',
            10: 'AFL', 11: 'VFL', 12: 'LBBBB', 13: 'SDHB', 
            14: 'Bigeminy', 15: 'PR', 16: 'VT'
        }


    print("Predicted Class:", class_labels[predicted_class_index])
