import json
friends = {
    "Rahul" : {"age":20, "city" :"jaipur"},
    "Amit" : {"age": 21, "city" : "udaipur"},
    "Pawan" : {"age": 19,"city":"mambai"},
    "Abhi" : {"age":18,"city":"pune"}
}
for name , info in friends.items():
    print(f"{name}, Age:{info['age']},City:{info['city']}")
with open("friends.json", "w") as f:
    json.dump(friends,f,indent=4)

print("Friends saved to freinds.json")