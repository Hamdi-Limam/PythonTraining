a_dict = [
    {
        "name": "gara",
        "power": "some sand related jutsu",
        "powerlevel": 199,
        "friends": [
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
        "friends": [
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
        "friends": [
            {
            "name": "Saitama",
            "friend_points": 128,
            "enemies": ["Naruto", "gara", "boruto"] 
            }
        ]
    }  
]

def nested_list(list):
    for l in list:
        for k, v in l.items():
            print("{0} : {1}".format(k, v))

def get_user_values(a_dict):
    count = 0
    for i in a_dict:
        print(f"Printing the user number {count+1}")
        for key, value in i.items():
            if isinstance(value, list):
                print("Friend List:")
                nested_list(value)
            else:
                print(f"{key.title()}: {value}")
        count += 1

get_user_values(a_dict)