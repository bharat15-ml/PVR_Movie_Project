from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
with open('gradient_boost.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('pvr_proj/gradient_boost/predict', methods=['POST'])
def predict():
    data = request.get_json() 

    # Extract features from the data
    total_seats = data['total_seats']
    no_screens = data['no_screens']

    # Create a DataFrame for prediction
    input_data = pd.DataFrame({'total_seats': [total_seats], 'no_screens': [no_screens]})

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Return the prediction as JSON
    return jsonify({'ticket_sold': prediction})

if __name__ == '__main__':
    app.run(debug=True)
