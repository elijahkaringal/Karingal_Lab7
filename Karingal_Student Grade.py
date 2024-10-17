name = input ("Enter your name:")
section = input ("Enter your section:")
prelim = float (input ("Enter your prelim grade:"))
if (prelim < 40 or prelim > 100): #for invalid input
    print ("Invalid Input, Must be between 40-100")
    exit ()
midterm = float (input ("Enter your midterm grade:"))
if (midterm < 40 or midterm > 100): #for invalid input
    print ("Invalid Input, Must be between 40-100")
    exit ()
final = float (input ("Enter your final grade:"))
if (final < 40 or final > 100): #for invalid input
    print ("Invalid Input, Must be between 40-100")
    exit ()

#final grade
final_grade = (prelim * 0.3333) + (midterm * 0.3333) + (final * 0.3333)
print(f"Hi {name} from {section}, Your final grade is {final_grade:.0f}")

#grade points & description
if (final_grade == 99 or final_grade == 100):
    print ("Your GPA is equal to 1.00, which is Excellent")
elif (final_grade >= 96 and final_grade <= 98):
    print ("Your GPA is equal to 1.25, which is Outstanding")
elif (final_grade >= 93 and final_grade <= 95):
    print ("Your GPA is equal to 1.50, which is Superior")
elif (final_grade >= 90 and final_grade <= 92):
    print ("Your GPA is equal to 1.75, which is Very Good")
elif (final_grade >= 87 and final_grade <= 89):
    print ("Your GPA is equal to 2.00, which is Good")
elif (final_grade >= 84 and final_grade <= 86):
    print ("Your GPA is equal to 2.25, which is Satisfactory")
elif (final_grade >= 81 and final_grade <= 83):
    print ("Your GPA is equal to 2.50, which is Fairly Satisfactory")
elif (final_grade >= 78 and final_grade <= 80):
    print ("Your GPA is equal to 2.75, which is Fair")
elif (final_grade >= 75 and final_grade <= 77):
    print ("Your GPA is equal to 3.00, which is considered a Passing Grade")
elif final_grade < 75:
    print ("Your GPA is equal to 5.0, which is considered a Failing Grade")
    
