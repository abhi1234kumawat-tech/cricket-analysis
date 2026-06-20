name = input("enter a student name :")
n= int(input("enter total subjects  :"))
subjcts  = []
total = 0
for i  in range(n):
    sub_name = input(f"subject{i+1} name :")
    marks = float(input(f"{sub_name} marks :"))
    subjcts.append({"subject": sub_name, "marks" : marks})
    total = total + marks
average = total/n
if average>=90:
    grade =" A"
elif average>=75 and average<90:
    grade= "B"
elif average >=65 and average<75:
    grade= "C"
else:
    "FAIL"
print(f"---Report card:{name}---")
print("Total marks", total)
print("Average:", average)
print("Grade",grade)

       