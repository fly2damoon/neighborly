# neighborly


Assumptions: 

1. user input will be a valid json format, with all required fields populated.
2. all rules are expected to be a valid json format, with valid rule properties

Test:
1. test the endpoint "/validate_profile" first, with password length of 2. Validation should pass, returning success.
2. then add a new rule via API endpoing "/new_rule", with "password" rule found in rules folder.
3. then re-run the "/validate_profile" with same input. Validation should now fail for password length.
