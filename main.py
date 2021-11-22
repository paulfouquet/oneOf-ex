import json
import os

import jsonschema_rs

schema_dual = open(os.path.join(os.getcwd(), "data", "schemas", "dual.json"), "r")
schema_dual_conditional = open(os.path.join(os.getcwd(), "data", "schemas", "dual-conditional.json"), "r")
schema_single = open(os.path.join(os.getcwd(), "data", "schemas", "single.json"), "r")
test_file = open(os.path.join(os.getcwd(), "data", "to_validate", "test.json"), "r")
test_dict = json.loads(test_file.read())
validator_dual = jsonschema_rs.JSONSchema.from_str(schema_dual.read())
validator_dual_conditional = jsonschema_rs.JSONSchema.from_str(schema_dual_conditional.read())
validator_single = jsonschema_rs.JSONSchema.from_str(schema_single.read())

errors_single = validator_single.iter_errors(test_dict)
for error in errors_single:
    print("Error for single schema: ", error.message)

errors_dual = validator_dual.iter_errors(test_dict)
for error in errors_dual:
    print("Error for dual schema: ", error.message)

errors_dual_cond = validator_dual_conditional.iter_errors(test_dict)
for error in errors_dual_cond:
    print("Error for dual conditional schema: ", error.message)
