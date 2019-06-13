##CS127
##September 18 2018
##Justin Guerrero

#import numpy
import math
import statistics

print("Welcome to the grade machine brought to you in part by Justin Guerrero:")

myString = ("Enter your letter grade seperated by a comma:")

myString = 0
sentence = 0

##here we must define values for the grades you enter in,  here is where `  we will translate letters into numbers
def translate(grade):
    
    if grade == "a" or grade == "A":
        return   4.0
        
    elif grade == "a-" or grade == "A-":
        return   3.7
    
    elif grade == "b+" or grade == "B+":
        return  3.3
    elif grade == "b" or grade == "B":
        return  3.0
    elif grade == "b-" or grade == "B-":
        return  2.7
    elif grade == "c+" or grade == "C+":
        return  2.3
    elif grade == "c" or grade == "C":
        return  2.0
    elif grade == "c-" or grade == "C-":
        return 1.7
    elif grade == "d+" or grade =="D+":
        return  1.3
    elif grade == "d" or grade == "D":
        return  1.0
    elif grade == "f" or grade == "F":
        return  0.0

    
    
    print(translate)



def main():


    #below we write a split function (shout out to the coding help center for teaching me that) to format to a list
    #also we write a for loop to call grades from above, and to add them together
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        count = 0
        sentence_zero = 0
        sentence = 0
        x = 0
        total = 0
        
        sentence_2 = 0
        sentence_zero = input("Please enter the number of classes you are taking: ")

        sentence_2 = 0
        sentence = input("Please enter grades you received in each class seperated by a comma" + '\n')
        sentence_2 = input("How many credit hours are each class worth? Enter seperated by comma: ")
        x = sentence.split(",")
        

        for j in x:
                red = translate(j)
                total = total + red
        #next we will do a little bit of math to average out the grade point average
        gpa = total/len(x)
        
        #gpa = round(gpa,2)
        print("Your GPA is  = %.2f congrats!" %gpa) 

        #next we write an answer input to either continue the program or terminate
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------
#and there you have it, your GPA, for better or worse.

main()
