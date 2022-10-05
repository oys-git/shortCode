#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#TODO-1: Create an empty dictionary called student_grades.


#TODO-2: Write your code below to add the grades to student_grades.👇

# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for score in student_scores:
  #print(score)
  #print(student_scores[score])
  if 100 > student_scores[score] >= 91:
    student_scores[score] = "Outstanding"
    #print(student_scores[score])
    student_grades[score] = student_scores[score]
  
  elif 91 > student_scores[score] >= 81:
    student_scores[score] = "Exceeds Expectations"
    #print(student_scores[score])
    student_grades[score] = student_scores[score]

  elif 81 > student_scores[score] >= 71:
    student_scores[score] = "Acceptable"
    #print(student_scores[score])
    student_grades[score] = student_scores[score]  
    
  else: #student_scores[score] >= 70:
    student_scores[score] = "Fail"
    #print(student_scores[score])
    student_grades[score] = student_scores[score]
    

# 🚨 Don't change the code below 👇
#print(student_grades)


#🚨 Don't change the code below 👇
print(student_grades)
