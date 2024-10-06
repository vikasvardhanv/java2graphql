from flask import Flask, render_template, request, jsonify
from json_to_graphql import json_to_schema

app = Flask(__name__)

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle JSON to GraphQL conversion
@app.route('/convert', methods=['POST'])
def convert():
    try:
        json_input = request.json.get('jsonInput')
        if not json_input:
            return jsonify({'error': 'No JSON input provided'}), 400

        # Convert JSON to GraphQL schema
        graphql_output = json_to_schema(json_input)
        return jsonify({'graphqlOutput': graphql_output}), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
