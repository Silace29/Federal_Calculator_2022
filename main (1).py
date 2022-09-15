print("Welcome to your (Single or Married, standard Deduction) federal tax calculator for the year of 2022!")

Answer = "yes"
while Answer.lower() == "yes" or Answer.lower() == "y" or Answer.lower() == "yeah" or Answer.lower() == "yup" or Answer.lower() == "ye":

    Income = int(input("Please enter the amount of money you wish to calculate (Do not include cents or a comma): $"))

    Donation = int(input("How much money was/will be donated? $"))

    Status = input("Will you be filing as Single/Joint?")


# Joint
    if Status.lower() == "joint" or Status.lower() == "j":
        if Donation <= 599:
            Total_Donation = Donation

        elif Donation >= 600:
            Total_Donation = 600

        if Income <= 25900:
            Initial_Tax = 0

        elif Income <= 46450:
            Initial_Tax = (Income - 25900) * .1

        elif Income <= 109450:
            Initial_Tax = ((Income - 46450) * .12) + 2055.00

        elif Income <= 204050:
            Initial_Tax = ((Income - 109450) * .22) + 9615.00

        elif Income <= 314200:
            Initial_Tax = ((Income - 204050) * .24) + 30427.00

        elif Income <= 457800:
            Initial_Tax = ((Income - 314200) * .32) + 56863.00

        elif Income <= 673750:
            Initial_Tax = ((Income - 457800) * .35) + 102815.00

        elif Income >= 673751:
            Initial_Tax = ((Income - 673750) * .37) + 178397.5

        else:
            print("Error")


# Single Person Calculation:
    elif Status.lower() == "single" or Status.lower() == "s":
        if Donation <= 299:
            Total_Donation = Donation

        elif Donation >= 300:
            Total_Donation = 300

        if Income <= 12950:
            Initial_Tax = 0

        elif Income <= 23225:
            Initial_Tax = (Income - 12950) * .1

        elif Income <= 54725:
            Initial_Tax = ((Income - 23225) * .12) + 1027.5

        elif Income <= 102025:
            Initial_Tax = ((Income - 54725) * .22) + 4807.5

        elif Income <= 183000:
            Initial_Tax = ((Income - 102025) * .24) + 15213.5

        elif Income <= 228900:
            Initial_Tax = ((Income - 183000) * .32) + 34647.5

        elif Income <= 336875:
            Initial_Tax = ((Income - 228900) * .35) + 49335.5

        elif Income >= 336876:
            Initial_Tax = ((Income - 336875) * .37) + 87126.75

    else:
        print("Error")

    Dollar_Output = Initial_Tax - Total_Donation

    print("Your owed taxes will be: $", Dollar_Output)

    Answer = input("Would you like to calculate another value? (Yes/No)")

print("Application closing! Thanks for choosing us!")