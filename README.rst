A simple format checker
=======================

A simple utility library that can check if data has a certain format and clean it up.
Used for checking API input formats and cleaning up output formats.

Example
```
import dataformat as f
import json

spec = {
    "number": int,
    "boolean": bool,
    "string": str,
    "numberlist": [int]
    "dict":{
        "number": int,
        "boolean": bool,
        "string": str,
        "numberlist": [int]
    }
}

data = {
    "number": 1,
    "boolean": False,
    "string": "test",
    "numberlist": [1,2,3],
    "dict": {
        "number": 1,
        "boolean": False,
        "string": "test",
        "numberlist": [1,2,3]
    }
}

f.mandatory(spec, data)
f.optional(spec, data)

spec = {"number":int}
f.clean(spec, data)
assert(data == {"number":1})
json.dumps(data, indent=2)
```
