# income:

# rental income ** Main source = $2,000/mth
# laundry income
# total_mth_income = 2,000

# Expenses:

# Taxes - 150
# Insurance - 100
# Utilities - 0
# 	Electric
# 	water
# 	sewer
# 	gas
# HOA - 0
# Lawncare/Snow - 0
# Vacancy - 100
# repairs - 100
# Capex - 100
# Property Managment - 200
# Mortgage - 860

# Total_expenses = 1610

# Cash_Flow:

# Cash_Flow = income - Expenses
# 390 = 2000 - 1610

# ROI:

# Down_Payment: 40,000
# Closing_Costs: 3,000
# Rehab_Budget: 7,000
# Misc_other: 0

# Total_investment == 50,000


# Annual_Cash_Flow = 4,680 / Total_investment == 50,000 == 9.36%

# cash on Cash ROI == 9.36% 

from cProfile import run
from http.client import CannotSendHeader
from multiprocessing.pool import RUN


class bigger_pockets():


    def __init__(self, rental_income=0.0, expenses=0.0, cash_flow=0.0, ROI=0.0):
        self.rentalincome = rental_income
        self.expensesamt = expenses
        self.cashflow = cash_flow
        self.ROIAMT = ROI
        
    def rental_income(self):
        self.rentalincome = float(input("What is the monthly rental income for the property? "))
        
    def expenses(self):
        taxes = float(input("what is the monthly taxes for the property?: "))
        insurance = float(input(" What is the monthly isurance for this property?: "))
        repairs = float(input(" How much are you saving for repairs monthly?: "))
        capex = float(input(" How much are you saving for CapEx monthly?: "))
        prop_man = float(input(" How much does your property manager cost monthly?: "))
        mortgage = float(input(" How much are you spedning on the mortgage monthly? "))
        self.expensesamt = taxes + insurance + repairs + capex + prop_man + mortgage
        
    def cash_flow(self):
        self.cashflow = self.rentalincome - self.expensesamt
        print("Your cash flow : %s" % (self.cashflow))
        
    def ROI(self):
        self.cashflow = self.cashflow  * 12
        total_investment = float(input("How much total investment did you spend on this property?: "))
        self.ROIAMT = (self.cashflow/total_investment) * 100

        print("The cash on cash ROI is \n")
        print(str(self.ROIAMT) + "%")
    

my_rental_property = bigger_pockets()          
            
def run():
    while True:
        response =  input('1.Quit \n2.Income \n3.Expenses\n4.Cash flow\n5.ROI\n What data would you like to input, please enter number?  ')
        if response.lower() == '1':
            my_rental_property.bigger_pockets()
            print("Day is over")
            break
        elif response.lower() == '2':
            #print("coming")
            my_rental_property.rental_income()
        elif response.lower() == '3':
            my_rental_property.expenses()
        elif response.lower() == '4':
            my_rental_property.cash_flow()
        elif response.lower() == '5':
            my_rental_property.ROI()
        else:
            print("Choose one of the correct commands ")

            
run()




