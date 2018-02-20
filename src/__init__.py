import json
from src.rule import Rule
import os


def get_json(json_file):
    result = json.load(open(json_file))
    return result

rule_files_path = os.path.join(os.getcwd(), 'src/rules')
rules_json_files= [os.path.join(rule_files_path,pos_json) for pos_json in os.listdir(rule_files_path) if pos_json.endswith('.json')]

rules = []

for rule_file in rules_json_files:
    rules.append(Rule(get_json(rule_file)))
