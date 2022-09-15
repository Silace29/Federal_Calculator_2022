def single_calculation(income, donation):
    if donation <= 299:
        total_donation = donation

    elif donation >= 300:
        total_donation = 300

    if income <= 12950:
        initial_tax = 0

    elif income <= 23225:
        initial_tax = (income - 12950) * .1

    elif income <= 54725:
        initial_tax = ((income - 23225) * .12) + 1027.5

    elif income <= 102025:
        initial_tax = ((income - 54725) * .22) + 4807.5

    elif income <= 183000:
        initial_tax = ((income - 102025) * .24) + 15213.5

    elif income <= 228900:
        initial_tax = ((income - 183000) * .32) + 34647.5

    elif income <= 336875:
        initial_tax = ((income - 228900) * .35) + 49335.5

    elif income >= 336876:
        initial_tax = ((income - 336875) * .37) + 87126.75

    else:
        print("Error")

    return initial_tax - total_donation
