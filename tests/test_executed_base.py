import json
import tempfile
from src.function import executed_base

test_json = json.dumps([
  {"id": 1, "state": "EXECUTED"},
  {"id": 2, "state": "CANCELED"},
  {"id": 3, "state": "EXECUTED"},
  {"id": 4, "state": "FAILED"}
])

test_true =  [
  {"id": 1, "state": "EXECUTED"},
  {"id": 3, "state": "EXECUTED"}
]

def test_executed_base():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as temp_json_file:
        temp_json_file.write(test_json)
        temp_json_file.flush()
    assert executed_base(temp_json_file.name) == test_true

