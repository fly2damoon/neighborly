from src import Rule
from src import get_json
from src import rules
from flask import Flask
from flask import jsonify
from flask import request



app = Flask(__name__)

@app.route('/')
def home():
    return 'test'

@app.route('/new_rule', methods=['POST'])
def add_new_rules():
    try:
        new_rule = request.json
        rules.append(Rule(new_rule))
        return jsonify('new rule added')
    except Exception as e:
        return jsonify(e)

@app.route('/validate_profile', methods=['POST'])
def validate_user_input():
    try:
        profile = request.json
        results = {"result": "success", "rules": []}

        for rule in rules:
            if False in rule.evaluate(profile):
                results['result'] = "failure"
                results.get('rules').append(rule.name)

        response = jsonify(results)
        if(results.get('result') == 'success'):
            response.status_code = 200
        else:
            response.status_code = 400

        return response
    except Exception as e:
        return jsonify(e)
