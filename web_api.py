from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import joblib

def return_prediction(model, scaler, sample_json):
    s_len = sample_json['sepal_length']
    s_wid = sample_json['sepal_width']
    p_len = sample_json['petal_length']
    p_wid = sample_json['petal_width']

    flower = [[s_len, s_wid, p_len, p_wid]]
    flower = scaler.transform(flower)
    
    classes = np.array(['setosa', 'versicolor', 'virginica'])
    class_probs = model.predict(flower)
    class_ind = np.argmax(class_probs)
    
    return classes[class_ind]

flower_model = load_model('final_iris_model.h5')
flower_scaler = joblib.load('iris_scaler.pkl') 



app = Flask(__name__) 

# index page
@app.route("/")
def index():
    return "<h1>Hello Soo Flask!</h1>"


@app.route('/api/flower', methods=['POST']) # only accepts http post requests
def flower_prediction():
    content = request.json
    results = return_prediction(flower_model, flower_scaler, content)
    return jsonify(results)


# if this script/file is run directly (its name == __main__), then run app
if __name__ == '__main__': 
    app.run()