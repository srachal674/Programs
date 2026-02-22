test_scores = []

for g in range (3):
    grade = int(input(f"Enter test grade{g+1}: "))
    test_scores.append(grade)

test_ave = sum(test_scores)/3

project = int(input(f"Enter project grade: "))

homework_ave = int(input(f"Enter homework grade: "))

#This calculates the weighted test grade.
def test(test_ave):
    test_grade = test_ave * .50
    return(test_grade)

#This calculates the weighted project grade.
def proj(project):
    project_grade = project * .30
    return(project_grade)

#This calculates the weighted homework grade.
def homework(homework_ave):
    homework_grade = homework_ave * .20
    return(homework_grade)

#This is the students weighted grade in the class.
def total(test, proj, homework):
    total_score = test + proj + homework
    return(total_score)

# Calculate the total weighted grade
total_score = total(test(test_ave), proj(project), homework(homework_ave))

#This compares the weighted test average to the given parameter and returns the correct letter grade and number score percent.
if test_ave >=90:
    print(f"Test Average = {int(test_ave + 0.5)}%")
elif test_ave >=80:
    print(f"Test Average = {int(test_ave + 0.5)}%")
elif test_ave >=70:
    print(f"Test Average = {int(test_ave + 0.5)}%")
elif test_ave >=60:
    print(f"Test Average =  {int(test_ave + 0.5)}%")
else:
    print(f"Test Average = {int(test_ave + 0.5)}%")

#This prints the students total weighted grade in the class.
if total_score >=90:
    print(f"Class Grade = A {int(total_score + 0.5)}%")
elif total_score >=80:
    print(f"Class Grade = B {int(total_score + 0.5)}%")
elif total_score >=70:
    print(f"Class Grade = C {int(total_score + 0.5)}%")
elif total_score >=60:
    print(f"Class Grade = D {int(total_score + 0.5)}%")
else:
    print(f"Class Grade = F {int(total_score + 0.5)}%")