# create a program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.
import math

print('''
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⢯⠙⠩⠀⡇⠊⠽⢖⠆⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠱⣠⠀⢁⣄⠔⠁⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⣷⣶⣾⣾⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⢀⡔⠙⠈⢱⡟⣧⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⡠⠊⠀⠀⣀⡀⠀⠘⠕⢄⠀⠀⠀⠀⠀
                        ⠀⠀⠀⢀⠞⠀⠀⢀⣠⣿⣧⣀⠀⠀⢄⠱⡀⠀⠀⠀
                        ⠀⠀⡰⠃⠀⠀⢠⣿⠿⣿⡟⢿⣷⡄⠀⠑⢜⢆⠀⠀
                        ⠀⢰⠁⠀⠀⠀⠸⣿⣦⣿⡇⠀⠛⠋⠀⠨⡐⢍⢆⠀
                        ⠀⡇⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣦⡀⠀⢀⠨⡒⠙⡄
                        ⢠⠁⡀⠀⠀⠀⣤⡀⠀⣿⡇⢈⣿⡷⠀⠠⢕⠢⠁⡇
                        ⠸⠀⡕⠀⠀⠀⢻⣿⣶⣿⣷⣾⡿⠁⠀⠨⣐⠨⢀⠃
                        ⠀⠣⣩⠘⠀⠀⠀⠈⠙⣿⡏⠁⠀⢀⠠⢁⡂⢉⠎⠀
                        ⠀⠀⠈⠓⠬⢀⣀⠀⠀⠈⠀⠀⠀⢐⣬⠴⠒⠁⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
  _                                      _                                        
 |_  o  ._    _.  ._    _  o   _.  |    /    _.  |   _       |   _.  _|_   _   ._ 
 |   |  | |  (_|  | |  (_  |  (_|  |    \_  (_|  |  (_  |_|  |  (_|   |_  (_)  |  
                                                                                 
''')
# The user should be allowed to choose which calculation they want to do.
print("────────────────────────────────────────────────────────────────────────────────────")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("────────────────────────────────────────────────────────────────────────────────────")
# How the user capitalises their selection should not affect how the program proceeds.
calculation_type = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower() 
# If the user doesn’t type in a valid input, show an appropriate error message.
if calculation_type != "investment" and calculation_type != "bond":
        print("Error! You didn't type either 'investment' or 'bond'.")        
# If the user selects investment.
elif calculation_type == "investment":
    # Ask the user how much money they are depositing.
    deposit_amount = float(input("How much money would you like to deposit? "))
    # Ask the user the interest rate (as a percentage). Only the number of the interest rate should be entered.
    interest_pct = float(input("Enter the interest rate (only number): "))
    # Ask the user the number of years they plan on investing.
    years_investing = float(input("How many years do you plan on investing? "))
    # Ask the user to input if they want “simple” or “compound” interest, and store this in a variable called interest. 
    interest = input("Would you like 'simple' or 'compound' interest? ")
    
    # Depending on whether or not they typed “simple” or “compound”, output the appropriate amount that they will get back after the given period, at the specified interest rate. 
    if interest == "simple":
        total_amount = deposit_amount * (1 + (interest_pct/100 * years_investing))
        round_total_amount = round(total_amount,2)
        print("\n----------------------------------------------------------------------------------------------------------------------------")
        print(f"After {years_investing} years you will get back {round_total_amount}, at the {interest_pct}% interest rate.")
        print("----------------------------------------------------------------------------------------------------------------------------")
    elif interest == "compound":
        total_amount_compound = deposit_amount * math.pow((1 + (interest_pct/100)), years_investing)
        rounded_total_amount_compound = round(total_amount_compound, 2)
        print("\n----------------------------------------------------------------------------------------------------------------------------")
        print(f"After {years_investing} years you will get back {rounded_total_amount_compound}, at the {interest_pct}% interest rate.")
        print("----------------------------------------------------------------------------------------------------------------------------")
# If the user selects bond.
elif calculation_type == "bond":
    # Ask the user to input present value of the house.
    house_value = float(input("What is the house value? "))
    # Ask the user to input interest rate (as a percentage). Only the number of the interest rate should be entered.
    interest_pct_bond = float(input("Enter the interest rate (only number): "))
    # Ask the user to input the number of months they plan to take to repay the bond.
    months_repay_bond = float(input("How many months do you plan to take to repay the bond? "))
    # Calculate the amount that a person will have to be repaid on a home loan each month.
    total_monthly_repayment = ((interest_pct_bond/100)/12 * house_value) / (1 - (1 + (interest_pct_bond/100)/12) ** (-months_repay_bond))
    rounded_total_monthly_repayment = round(total_monthly_repayment, 2)
    # Display how much money the user will have to repay each month.
    print(f"You will have to repay {rounded_total_monthly_repayment} each month.")