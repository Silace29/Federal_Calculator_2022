print("Welcome to your (Standard Deduction) federal tax calculator for the year of 2022!")
#setting up for loops:
import re
Answer = "yes"
donation_answer = True
status_answer = True
# Beginning of the program loop
while Answer.lower() == "yes":

    income = (input("Please enter the amount of money you wish to calculate (Do not include cents or a comma): $"))
    if re.search("[a-z,A-Z,,,.]", income):
        print("Error: Please make sure you read the prompt carefully")
        continue

    # Beginning of donation loop
    while donation_answer == True:
        donation = (input("How much money was/will be donated? $"))
        if re.search("[a-z,A-Z,,,.]", donation):
            print("Error: Please make sure you read the prompt carefully")
            continue
        else:
            break

    # Beginning of status loop
    while status_answer == True:
        status = input("Will you be filing as Single, Joint, M. Separate, or Head of House?")
        # Checks to make sure no numbers are used / might be redundent because of next line
        if bool(re.search(r"-?\d+", status)):
            print("Error: Please make sure you read the prompt carefully")
            continue
        # Checks to make sure they typed in only what the prompt asks or it starts over
        elif status.lower() == "joint" or status.lower() == "j" or\
            status.lower() == "single" or status.lower() == "s" or status.lower()\
            == "m. separate" or status.lower() == "separate" or status.lower() == "m separate"\
            or status.lower() == "head of house" or  status.lower() == "head of household" or status.lower() == "h" or \
            status.lower() == "head":
                break
        # Says everything besides the prompt gets rejected
        else:
            print("Error: Please make sure you read the prompt carefully, and check your spelling")
            continue

    # Segmenting our project into the path that creats proper calculation using our now known inputs

    # Joint
    if status.lower() == "joint" or status.lower() == "j":
        from Joint import *
        dollar_output = joint_calculation(int(income), int(donation))


    # Single or Married filing jointly Calculation:
    elif status.lower() == "single" or status.lower() == "s" or status.lower()\
    == "m. separate" or status.lower() == "separate" or status.lower() == "m separate":
        from Single import *
        dollar_output = single_calculation(int(income), int(donation))

    # Head of Houshold Calculation:
    elif status.lower() == "head of house" or  status.lower() == "head of household" or status.lower() == "h" or \
    status.lower() == "head":
        from combo import *
        dollar_output = head_of_house_calculation(int(income), int(donation))

    else:
        print("Error: Please make sure you followed the prompt correctly")
        Answer = "yes"
        continue

    # Output answer:

    print("Your owed taxes will be: $", dollar_output)

    # Checking to see if they want to run another calculation:
    check_answer = input("Would you like to calculate another value? (Yes/No)")
    if check_answer.lower() == "yes" or check_answer.lower() == "y" or check_answer.lower() == "ye":
        Answer = "yes"
    else:
        Answer = "no"

# Closing the Program
print("Application closing! Thank you for using this program.")