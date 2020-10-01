# -*- coding: utf-8 -*-


def fertilizer_calculator():
    """Python program for determining fertalizer needed for a given square foot area and a known NPK ratio"""
    while True:
        """Get Input from the user, error handling in case something other than a number is entered)
        Inputs are assigned variables for use in the calculations. """
        try:
            sq_feet = float(input("How many square feet?: "))
            n = float(input("How much nitrogen?: "))
            p = float(input("How much phosphorus?: "))
            k = float(input("How much potassium?: " ))
            
            break
        except ValueError:
            # Error handling if something besides a number is entered
            print("Please enter a number.")
            
    """ Math, rounded to the second decimal with error handling for trying to divide by zero"""
    """Square Feet Divided by 1000"""
    per_thousand = sq_feet/1000
    try:
        """Our Square Feet Divided by 1000 times (1 divided by the percentage of nitrogen)"""
        n_per_sq_ft = float("{:.2f}".format(per_thousand * (1/(n*.01))))
    except ZeroDivisionError:
        # Error handling if 0 is entered as dividing by zero is not possible
        n_per_sq_ft = 0
    try:
        """Our Square Feet Divided by 1000 times (1 divided by the percentage of phosphorus)"""
        p_per_sq_ft = float("{:.2f}".format(per_thousand * (1/(p*.01))))
    except ZeroDivisionError:
        # Error handling if 0 is entered as dividing by zero is not possible
        p_per_sq_ft = 0
    try:
        """Our Square Feet Divided by 1000 times (1 divided by the percentage of potassium)"""
        k_per_sq_ft = float("{:.2f}".format(per_thousand * (1/(k*.01))))
    except ZeroDivisionError:
        # Error handling if 0 is entered as dividing by zero is not possible
        k_per_sq_ft = 0
    # Storing our answer as a sentence in a variable called ans    
    ans = (f"You will need {n_per_sq_ft} pounds of Nitrogen, {p_per_sq_ft} pounds of Phosphorus, and {k_per_sq_ft} pounds of Potassium")
    return ans
    


print(fertilizer_calculator())
