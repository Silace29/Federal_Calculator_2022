def joint_calculation(income, donation):
    if donation <= 599:
        total_donation = donation

    elif donation >= 600:
        total_donation = 600

    if income <= 25900:
        initial_tax = 0

    elif income <= 46450:
        initial_tax = (income - 25900) * .1

    elif income <= 109450:
        initial_tax = ((income - 46450) * .12) + 2055.00

    elif income <= 204050:
        initial_tax = ((income - 109450) * .22) + 9615.00

    elif income <= 314200:
        initial_tax = ((income - 204050) * .24) + 30427.00

    elif income <= 457800:
        initial_tax = ((income - 314200) * .32) + 56863.00

    elif income <= 673750:
        initial_tax = ((income - 457800) * .35) + 102815.00

    elif income >= 673751:
        initial_tax = ((income - 673750) * .37) + 178397.5

    else:
        print("Error")

    return initial_tax - total_donation
