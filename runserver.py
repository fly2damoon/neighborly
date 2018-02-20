
from src.api import app

def test_rules():
    # user_input_path = os.path.join(os.getcwd(), 'src/user_input')
    # user_input_json_files = [os.path.join(user_input_path,pos_json) for pos_json in os.listdir(user_input_path) if pos_json.endswith('.json')]
    # user_input_json_file = user_input_json_files[0]
    # user_input_json = get_json(user_input_json_file)

    # rule_files_path = os.path.join(os.getcwd(), 'src/rules')
    # rules_json_files= [os.path.join(rule_files_path,pos_json) for pos_json in os.listdir(rule_files_path) if pos_json.endswith('.json')]
    #
    # rules = []
    # results = {"result": "", "rules": []}
    # for rule_file in rules_json_files:
    #     rules.append(Rule(get_json(rule_file)))
    #
    # if False in rule.evaluate():
    #         results['result'] = "failure"
    #         results.get('rules').append(rule.name)
    pass

if __name__ == "__main__":


    app.run(host='127.0.0.1', port=5000)



