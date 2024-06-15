from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": [
    'http://localhost:3000', 
    'https://diamond-dashboard-one.vercel.app',
    'https://dvs-fe-soramyos-projects.vercel.app',
    'https://dvs-be-sooty.vercel.app',
    'https://dvs-fe.vercel.app',
    'https://dvs-fe-git-main-soramyos-projects.vercel.app',
]}})

model = joblib.load('model/linear_regression_model.pkl')

@app.route('/predict', methods=['POST'])
@cross_origin(supports_credentials=True)
def predict():
    data = request.get_json()
    carat = data['carat']
    cut = data['cut']
    color = data['color']
    clarity = data['clarity']
    depth = data['depth']
    table = data['table']
    x = data['x']
    y = data['y']
    z = data['z']

    # Mapping for cut
    cut_mapping = {'Fair': 0, 'Good': 1, 'Very Good': 2, 'Premium': 3, 'Ideal': 4}
    # Mapping for color
    color_mapping = {'J': 0, 'I': 1, 'H': 2, 'G': 3, 'F': 4, 'E': 5, 'D': 6}
    # Mapping for clarity
    clarity_mapping = {'I1': 0, 'SI2': 1, 'SI1': 2, 'VS2': 3, 'VS1': 4, 'VVS2': 5, 'VVS1': 6, 'IF': 7}

    # Convert categorical variables to numerical
    cut = cut_mapping.get(cut, 0)
    color = color_mapping.get(color, 0)
    clarity = clarity_mapping.get(clarity, 0)

    # Predict price using converted variables
    prediction = model.predict(pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]],
                                            columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']))
    return jsonify({'predicted_price': prediction[0]}), 200

if __name__ == '__main__':
    app.run(debug=True)
