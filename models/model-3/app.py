from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract features from the data
    city = data['city']
    movie_type = data['type']
    avg_ticket_price = data['average_ticket_price']
    profit_margin = data['profit_margin']

    # Create a DataFrame for prediction
    input_data = pd.DataFrame({'city': [city], 'type': [movie_type], 'average_ticket_price': [avg_ticket_price], 'profit_margin': [profit_margin]})

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Return the prediction as JSON
    return jsonify({'predicted_seats': prediction})

if __name__ == '__main__':
    app.run(debug=True)
