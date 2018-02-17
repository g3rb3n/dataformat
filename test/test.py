import dataformat as f

import json

data_dir = 'data/'

def get_data():
    with open(data_dir + 'data.json') as f:
        return json.load(f)

def get_data2():
    with open(data_dir + 'data2.json') as f:
        return json.load(f)

def get_spec2():
    return {
        "float": float,
        "integer": int,
        "boolean": bool,
        "true": bool,
        "false": bool,
        "string": str
    }

def get_spec2b():
    return {
        "float": float,
        "integer": float,
        "boolean": bool,
        "true": bool,
        "false": bool,
        "string": str
    }

def get_spec():
    point = {
        'latitude': float,
        'longitude': float,
        'elevation': float,
        'distance': float
    }
    spec = {
        'routes':[{
            'distance':float,
            'error':float,
            'instructions':[{
                'start': point,
                'end': point,
                'sign': str,
                'text': str
            }],
            'points':[point]
        }]
    }
    return spec

def get_select():
    select = {
        'routes':[{
            'instructions':[{
                'text': str
            }]
        }]
    }
    return select

def test_mandatory():
    data = get_data()
    spec = get_spec()
    f.mandatory(spec, data)

def test_mandatory_fail():
    data = get_data()
    spec = get_spec()
    del data['routes'][0]['distance']
    try:
        f.mandatory(spec, data)
        raise Exception('KeyNotFoundException should have been raised, but call was succesful')
    except f.KeyNotFoundException as e:
        pass
    except:
        raise Exception('KeyNotFoundException should have been raised, not %s' % str(e))

def test_optional_fail():
    data = get_data()
    spec = get_spec()
    #del spec['routes'][0]['distance']
    try:
        f.optional(spec, data)
        raise Exception('SpuriousKeyException should have been raised, but call was succesful')
    except f.SpuriousKeyException as e:
        pass
    except:
        raise Exception('SpuriousKeyException should have been raised, not %s' % str(e))

def test_clean():
    data = get_data()
    spec = get_spec()
    f.clean({}, data)
    if data:
        raise Exception('All data should have been cleaned')

def test_select():
    data = get_data()
    spec = get_select()
    f.clean(spec, data)
    f.mandatory(spec, data)
    f.optional(spec, data)

def test_types():
    data = get_data2()
    spec = get_spec2()
    f.mandatory(spec, data)
    f.optional(spec, data)

def test_types_int_bay_be_float():
    data = get_data2()
    spec = get_spec2()
    spec['integer'] = float
    f.mandatory(spec, data)
    f.optional(spec, data)

def test_list():
    spec = {
        "number": int,
        "boolean": bool,
        "string": str,
        "numberlist": [int],
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

if __name__ == '__main__':
    data = get_data2()
    spec = get_spec2()
    f.mandatory(spec, data)
    f.optional(spec, data)

    data = get_data()
    spec = get_spec()
    select = get_select()
    f.mandatory(spec, data)
    f.clean(spec, data)
    f.optional(spec, data)
    f.clean(select, data)
    print(json.dumps(data, indent=2))
