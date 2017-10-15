# commons.py
# by James Fulford

# Common functions and variables used across the project.
# Ideally, this script would be linked to (see "ln" command in Unix)
# in other places. However, that is not how it turned out.
# So, every "commons.py" is similar, but not necessarily the same.


import json
import os
import datetime as dt

# Path Configurations

def project_path():
    return r"/Users/jamesfulford/Documents/Math Capstone"

def error_path():
    return project_path() + r"/Error Logs"

def dataset_path():
    return project_path() + r"/Data/Full Data Set.json"


commons = filter(lambda x: "__" not in x and x not in ["os", "json", "dt"], locals())

locale = locals()  # scope problems with lambda! who knew!
fails = filter(lambda defin: not os.path.exists(locale[defin]()), commons)
if(len(fails) > 0):
    print("Invalid paths provided by: " + str(fails))


# dumping dictionaries

def dump(dictionary, path):
    def json_serial(obj):
        """JSON serializer for dates"""
        if isinstance(obj, dt.date):
            serial = obj.strftime("%m/%d/%Y")
            return serial
        raise TypeError("Type not serializable")
    with open(path, 'wb') as f:
        f.write(json.dumps(dictionary, indent=4, default=json_serial))


# loading dictionaries from file

def load_file(path):
    """Uses json to create a dictionary from given file.
    Handles dates in form of %Y-%m-%d"""
    def date_hook(json_dict):
        for(key, value) in json_dict.items():
            try:
                json_dict[key] = dt.strptime(value, '%Y-%m-%d').date()
            except:
                pass
        return json_dict
    # Actual loading of file
    with open(path) as f:
        data = json.load(f, object_hook=date_hook)
        return data


def dataset():
    return load_file(project_path() + r"/Data/Full Data Set.json")


# logging errors
def log(errors, path="test log"):
    if(len(errors) > 0):  # does not write if there are no errors!
        dump(errors, error_path() + "/" + path + '.json')
