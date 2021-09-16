# Task 1: Convert a dictionary object to JSON and then convert it back to dictionary. 
# The ductuinary to convert:
a_dict = [
    {
        "name": "gara",
        "power": "some sand related jutsu",
        "powerlevel": 199,
        "frieds": [
            {
                "name": "Naruto",
                "friend_points": 28,
                "enemies": ["Saitama"] 
            },
            {
                "name": "Boruto",
                "friend_points": 18,
                "enemies": ["Saitama"]
            }
        ]
    },
    {
        "name": "Alex",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Soniya",
            "friend_points": 128,
            "enemies": ["Saitama"] 
            }
        ]
    },
    {
        "name": "King",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Saitama",
            "friend_points": 128,
            "enemies": ["Naruto", "gara", "boruto"] 
            }
        ]
    }
]

# JSON (JavaScript Object Notation), is a lightweight data interchange format inspired by JavaScript object literal syntax.
# JSON is used for storing it or sending it around between programs.

#Importing JSON Package in Python
import json

# json.dumps() - This method allows you to convert a python object into a serialized JSON object.
# json.dump() - This method allows you to convert a python object into JSON and additionally allows you to store the information into a file (text file)
def convert_dict_json(a_dict):
    return json.dumps(a_dict, indent=4)


# json.loads() - Deserializes a JSON object to a standard python object.
# json.load() - Deserializes a JSON file object into a standard python object.
def convert_json_dict(my_json):
    return json.loads(my_json, )

new_json = convert_dict_json(a_dict)
print(f"Result of converting a dictionary to JSON:\n{new_json}\nType of the result is a JSON string format: {type(new_json)}\n")

new_dict = convert_json_dict(new_json)
print(f"Result of converting a JSON to dictionary:\n{json.dumps(new_dict, indent=4)}\nType of the result is a dictionary: {type(new_dict)}")

# Convert a dictionary object to XML and then convert it back to dictionary. 


