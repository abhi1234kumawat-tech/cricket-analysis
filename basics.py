# name = "Abhishek Kumawat"
# age = 18
# college = "uem jaipur"
# team = "RCB"
# print(name,age,college,team)

# players = ["virat", "patidar", "venky","jitesh"]
# for player in players:
#     print(f"{player} is a gretest batsman!")
# def calculate_average(runs,matches):
#     return runs / matches

# virat_avg = calculate_average(850,10)
# print(f"virat average:{virat_avg}")

# player  = {
#     "name" : "virat kohli",
#     "runs" : 973,
#     "TEAM" : "RCB",
#     "year" : 2016,
# }
# print(player["name"])
# print(player["runs"])
# print(player["TEAM"])
# # print(player["year"])

# player_data = "Virat Kohli | RCB | 973 RUNS"
# with open("player.txt", "w") as f:
#     f.write(player_data)
# print("file save ho gyi!")

# with open("player.txt", "r") as f:
#     data  = f.read()
# #     print("file mein h:", data)

# players = {
#     "kohli" : {"runs" : 973,"matches" :14},
#     "patidar" : {"runs":500,"matches" : 14},
#     "jitesh" : {"runs" :465,"matches" : 14},
# }
# for player , stats in players.items():
#     avg= stats["runs"] / stats["matches"]
#     print(f"{player}, Runs: {stats['runs']}, Average: {avg}")

subjects = ["maths", "science", "physics","chemistry"]
for subject in subjects:
    print(f"{subject} is the best sub.")

def calculate_average(marks):
    return sum(marks) / len(marks)
marks = [97,96,93,90]
avg = calculate_average(marks)
print(f"Average:{avg}")