from flask import Flask, request, jsonify
import pickle
import numpy as np
from pymongo import MongoClient
import datetime

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "postpartum_db"
COLLECTION_NAME = "patient_records"

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    print("Connection Successful!")
except Exception as e:
    print(f"Error to connect to database: {e}")
    exit()

try:
    model = pickle.load(open('random_forest_model.pkl', 'rb'))
    features = ['Overeating or loss of appetite', 'Feeling of guilt', 'Problems of bonding with baby',
                'Problems concentrating or making decision']
    print(f"Model Successfully Loaded. Features expect : {features}")
    print(f"Type of loaded model: {type(model)}")
except FileNotFoundError:
    print("Error: File 'random_forest_model' not found .")
    exit()
except Exception as e:
    print(f"Error to load: {e}")
    exit()

app = Flask(__name__)

@app.route('/')
def home():
    return 'We are just getting started'

@app.route('/predict_depression', methods=['POST'])
def predict():
    try:

        data = request.get_json(force=True)

        print("Data Received:", data)

        patient_name = data.get('patient_name')

        input_features = [data[feature] for feature in features]

        final_features = np.array(input_features).reshape(1, -1)

        prediction = model.predict(final_features)

        result_text = "Anxious" if prediction[0] == 1 else "Not Anxious"

        record_to_save = {   # data added to mongoDb
        "patient_name": patient_name,
        "input_data": data,
        "prediction_result": result_text,
        "timestamp": datetime.datetime.now()
                                  }
        inserted_id = collection.insert_one(record_to_save).inserted_id

        return jsonify({    # return to POSTMAN
        'patient_name': patient_name,
        'prediction': result_text,
        'patient_record_id': str(inserted_id)
                               })
    except Exception as e:
        print(f"Error to load: {e}")
        exit()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
