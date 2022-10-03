a = 1
b = 2
#print(a, b)


def person(old):
    name = input("Please enter your name---> ")
    print("Hello, " + name + "!")
    age = input("Enter age---> ")
    print(old + age)

#person("Age---> ")


#CALCUTA
def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is---> ", result)
    return result

number1 = 5.4
number2 = 4.5
#result = add_numbers(number1, number2)
#print("The sum is---> ", result)

def find_avg(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    avg_marks = sum_of_marks / total_subjects
    return avg_marks

def compute_grade(avg_marks):
    if avg_marks >= 80:
        grade = 'A'
    elif avg_marks >= 60:
        grade = 'B'
    elif avg_marks >= 40:
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = [55, 64 ,54 ,34 ,65]
avg_marks = find_avg(marks)
print("Average mark is---> ", avg_marks)

grade = compute_grade(avg_marks)
print("Your grade is ---> ", grade)
#legth = len(marks)
#print("Length is---> ", legth)

#marks_sum = sum(marks)
#print("Sum of marks---> ",marks_sum)


delay = input()
# https://youtu.be/-Bkupx9gX0o?list=PL98qAXLA6afuh50qD2MdAj3ofYjZR_Phn - Фани индиан гай
