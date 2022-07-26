#quiz assignment

#score
score = 0


#question number 1
question1 =input("My favorite animal? ")
if question1 == "monkey":
    print("Question 2 answer: monkey")
    print("correct")
    score = score + 1
else:
    print("Question 2 answer: monkey")
    print("Incorrect")

#question number 2
question2 = input("My least favroite subject in school? ")
if question2 == "la" or question2 == "english" or question2 == "langauage arts":
    print("Question 2  answers: la, english, language arts")
    print("Correct")
    
    score = score + 1
else:
    print("Question 2  answers: la, english, language arts")
    print("incorrect")
#question number 3


question3 = input("What is my age?  ")
if question3 == "16" or question3 =="sixteen":
    print("question 3 answers: 16, sixteen")
    print("correct")
    score = score + 1
else:
    print("question 3 answers: 16, sixteen")
    print("Incorrect")
#question number 4


question4 = input("My favorite soccer player? ")
if question4 == "messi" or question4 == "ronaldo" or question4 == "cristiano ronaldo":
    print("question 4 answers: messi, ronaldo, cristiano ronaldo ")
    print("correct")
    score = score + 1
else:
     print("question 4 answers: messi, ronaldo, cristiano ronaldo ")
     print("incorrect")

     
#score and output your results
percentage = (score/4) *100
print("Your Score is " +str(score) + "/4 " + "- " + (str(percentage) + "%"))
if score == 4:
    print("GOOD JOB")
elif score == 3:
    print("Nice")
elif score == 2:
    print("Intersting")
elif score == 1:
    print("YIKES!!")
else:
    print("BRUH!!!")
