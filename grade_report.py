'''
Laurel Lynn
IS 303 - A03

Grade Report
Collects student scores and produces a grade summary

Inputs:
- Number of Students (int)
- For each student: score out of 100 (int)

Processes:
- Collect  data into a list of dictionaries
- Accumulator: divide total score by number of students for average
- Min/Max: find the highest scoring student and lowest scoring student
- Filter: students with scores 93 or above are "A" students and count

Outputs:
- Print number of students
- Print average score
- Print highest and lowest scoring students and scores
- Print number of "A" students
'''

number_of_students = int(input("Total number of students: "))
scores = []

for i in range(number_of_students):
    scores.append(int(input(f"Score of Student {i+1}: ")))

#accumulator
total = 0
for score in scores:
    total += int(score)
average = total/number_of_students

#min/max loop: find lowest and hightest score
top_student = scores[0]
for score in scores:
    if score > top_student:
        top_student = score

#filter students with score above 93
a_grade = []
for score in scores:
    if score > 93:
        a_grade.append(score)



print(f"--- Grade Report Summary ---")

print(f"Average Score: {average}")
print(f"Top Student Score: {top_student}")
print(f"Number of A Students: {len(a_grade)}")