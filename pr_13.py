marks = [85, 78, 92, 74, 88]
total_marks = sum(marks)
percentage = (total_marks / 500) * 100


if percentage >= 70:
    classification = "Distinction"
elif percentage >= 60:
    classification = "First Class"
elif percentage >= 50:
    classification = "Second Class"
elif percentage >= 40:
    classification = "Pass Class"
else:
    classification = "Fail"

print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Class of Result:", classification)