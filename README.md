# Financial Calculator

This program allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.

# How to Use

When the program runs, the user is presented with a menu of options to choose from:

investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan

The user can enter either investment or bond to proceed with the selected calculator. If the user enters an invalid option, an error message is displayed.

~~~
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


────────────────────────────────────────────────────────────────────────────────────
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
────────────────────────────────────────────────────────────────────────────────────

Enter either 'investment' or 'bond' from the menu above to proceed: investment
How much money would you like to deposit? 2000
Enter the interest rate (only number): 8
How many years do you plan on investing? 10
Would you like 'simple' or 'compound' interest? simple

----------------------------------------------------------------------------------------------------------------------------
After 10.0 years you will get back 3600.0, at the 8.0% interest rate.
----------------------------------------------------------------------------------------------------------------------------
~~~  



# Investment Calculator

If the user selects the investment option, the program will ask for the following inputs:

deposit_amount: the amount of money the user is depositing
interest_pct: the interest rate (as a percentage)
years_investing: the number of years the user plans on investing
interest: whether the user wants "simple" or "compound" interest

Based on the user's inputs, the program will calculate and display the total amount that they will get back after the given period, at the specified interest rate.

# Home Loan Repayment Calculator

If the user selects the bond option, the program will ask for the following inputs:

house_value: the present value of the house
interest_pct_bond: the interest rate (as a percentage)
months_repay_bond: the number of months the user plans to take to repay the bond

Based on the user's inputs, the program will calculate and display the amount of money the user will have to repay each month.

# Error Handling
If the user enters an invalid input, the program will display an error message and ask the user to try again.

# Limitations

This program is for educational purposes only and should not be used as a substitute for professional financial advice. It also has some limitations, such as not taking into account taxes or fees.
