test_scores = []

for g in range (3):
    grade = int(input(f"Enter test grade{g+1}: "))
    test_scores.append(grade)

test_ave = sum(test_scores)/3

project = int(input(f"Enter project grade: "))

homework_ave = int(input(f"Enter homework grade: "))

def test(test_ave):
    test_grade = test_ave * .50
    return(test_grade)

def proj(project):
    project_grade = project * .30
    return(project_grade)

def homework(homework_ave):
    homework_grade = homework_ave * .20
    return(homework_grade)

if test_ave >=90:
    print(f"Test = A {int(test_ave + 0.5)}%")
elif test_ave >=80:
    print(f"Test = B {int(test_ave + 0.5)}%")
elif test_ave >=70:
    print(f"Test = C {int(test_ave + 0.5)}%")
elif test_ave >=60:
    print(f"Test = D {int(test_ave + 0.5)}%")
else:
    print(f"Test = F {int(test_ave + 0.5)}%")

if project >=90:
    print(f"Project = A {int(project + 0.5)}%")
elif project >=80:
    print(f"Project = B {int(project + 0.5)}%")
elif project >=70:
    print(f"Project = C {int(project + 0.5)}%")
elif project >=60:
    print(f"Project = D {int(project + 0.5)}%")
else:
    print(f"Project = F {int(project + 0.5)}%")

if homework_ave >=90:
    print(f"Homework = A {int(homework_ave + 0.5)}%")
elif homework_ave >=80:
    print(f"Homework = B {int(homework_ave + 0.5)}%")
elif homework_ave >=70:
    print(f"Homework = C {int(homework_ave + 0.5)}%")
elif homework_ave >=60:
    print(f"Homework = D {int(homework_ave + 0.5)}%")
else:
    print(f"Homework = F {int(homework_ave + 0.5)}%")