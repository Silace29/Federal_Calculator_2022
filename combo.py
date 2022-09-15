
def head_of_house_calculation(income, donation):
    if donation <= 299:
        total_donation = donation

    elif donation >= 300:
        total_donation = 600

    if income <= 19400:
        initial_tax = 0

    elif income <= 34050:
        initial_tax = (income - 19400) * .1

    elif income <= 75300:
        initial_tax = ((income - 34050) * .12) + 1465.00

    elif income <= 108450:
        initial_tax = ((income - 75300) * .22) + 6415.00

    elif income <= 189450:
        initial_tax = ((income - 108450) * .24) + 13708.00

    elif income <= 235350:
        initial_tax = ((income - 189450) * .32) + 33148.00

    elif income <= 559300:
        initial_tax = ((income - 235350) * .35) + 47836.00

    elif income >= 559301:
        initial_tax = ((income - 559300) * .37) + 161218.5

    else:
        print("Error")

    return initial_tax - total_donation
