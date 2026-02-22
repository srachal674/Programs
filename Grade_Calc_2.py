#This gets the total number of tests from the user.
begin = int(input("How many test do you need to enter? "))

#This stores the number of test the user set so they can be used to control the test loop and calculate the test averge.
num_scores = begin

#This stores the input test scores.
test_scores = []

#This gets the weighted test percent from the user. 
test_weight = float(input("Enter max point value for tests: ")) / 100

#This gets the weighted project percent from the user.
project_weight = float(input("Enter max points for project: ")) / 100

#This gets the weighted test percent from the user. 
homework_weight = float(input("Enter max point value for homework: ")) / 100

#This gathers the tests scores from the user based on their input number.
for g in range (num_scores):
    grade = int(input(f"Enter test grade {g+1}: "))
    test_scores.append(grade)

#This calculates their average test score using the number of test they set and the scores they entered.
test_ave = sum(test_scores)/num_scores

#This takes in the project score from the user.
project = int(input(f"Enter project grade: "))

homework_ave = int(input(f"Enter homework grade: "))

# Calculate the total weighted grade
test_points = test_ave * test_weight
project_points = project * project_weight
homework_points = homework_ave * homework_weight

total_score = test_points + project_points + homework_points

# determine letter grade
if total_score >= 90:
    letter = "A"
elif total_score >= 80:
    letter = "B"
elif total_score >= 70:
    letter = "C"
elif total_score >= 60:
    letter = "D"
else:
    letter = "F"

# print both together
print(f"Final Grade: {round(total_score)}% ({letter})")