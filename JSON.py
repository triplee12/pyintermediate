import json
from json import JSONEncoder

__author__ = "Ejie Emmanuel Ebuka"

# JSON

"""
Json: Javascript object notatation, for data sharing between applications
"""


# Serialization / encode
person = {"name": "John", "age": 28, "gender": "male", "city": "Awka", "hasChildren": False, "title": ["developer", "engineer", "Programmer"]}
personJson = json.dumps(person, indent=4, sort_keys=True)
print(f"Person: {personJson}")

with open("json/person.json", "w") as f:
    json.dump(person, f, indent=4, sort_keys=True)

# Deserialization / Decode
person_decode = json.loads(personJson)
print(person_decode)

with open("json/person.json", "r") as f:
    person_decode_2 = json.load(f)
    print(person_decode_2)

# Let's wrk with custom object

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Encode: custom encoder
def encode_user(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: obj.__class__.__name__}
    else:
        raise TypeError("Object of type User is not JSON serializable")

# We can use JSONEncoder imported from json
class UserEncoder(JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, User):
            return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: obj.__class__.__name__}
        return JSONEncoder.default(self, obj)

user = User("Chris", 28)
userJson = json.dumps(user, default=encode_user)
print(userJson)

user_2 = User("Jane", 28)
user_2Json = json.dumps(user_2, cls=UserEncoder)
# user_2Json = UserEncoder().encode(user_2) # This will also work
print(user_2Json)

# Decode
user_2 = json.loads(user_2Json)
print(user_2)

# Custom decode object
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct

user_2 = json.loads(user_2Json, object_hook=decode_user)
print(user_2.name, user_2.age)
