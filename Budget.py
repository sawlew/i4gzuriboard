class Budget:
    def __init__(self, deposit, withdrawal, balance):

        self.deposit = deposit
        self.withdrawal = withdrawal
        self.balance = deposit + withdrawal
    
 


budget_food = Budget(0, 0, {})
budget_clothing = Budget(0, 0, {})
budget_entertainment = Budget(0, 0, {})

print('food===>', budget_food.__dict__)

print('clothing===>', budget_clothing.__dict__)

print('entertainment===>', budget_entertainment.__dict__)

print('''FUND ALL CATEGORIES:
1. food
2. clothing
3. entertainment''')


food_deposit = int(input('Enter budget for food:\n'))
if food_deposit > 0:
    budget_food.balance = budget_food.deposit + food_deposit + budget_food.withdrawal
    print('food===>', (budget_food.deposit + food_deposit, budget_food.withdrawal, budget_food.balance))

clothing_deposit = int(input('Enter budget for clothing:\n'))
if clothing_deposit > 0:
    budget_clothing.balance = budget_clothing.deposit + clothing_deposit + budget_clothing.withdrawal
    print('clothing===>', (budget_clothing.deposit + clothing_deposit, budget_clothing.withdrawal, budget_clothing.balance))

entertainment_deposit = int(input('Enter budget for entertainment:\n'))
if entertainment_deposit > 0:
    budget_entertainment.balance = budget_entertainment.deposit + entertainment_deposit + budget_entertainment.withdrawal
    print('entertainment===>', (budget_entertainment.deposit + entertainment_deposit, budget_entertainment.withdrawal, budget_entertainment.balance))


print('Here is your budget:')
print('1. food===>', (budget_food.deposit + food_deposit, budget_food.withdrawal, budget_food.balance))
print('2. clothing===>', (budget_clothing.deposit + clothing_deposit, budget_clothing.withdrawal, budget_clothing.balance))
print('3. entertainment===>', (budget_entertainment.deposit + entertainment_deposit, budget_entertainment.withdrawal, budget_entertainment.balance))




selectedOption = int(input('Please select a category to withdraw from:\n'))

if (selectedOption == 1) :
    food_withdrawal = int(input('How much do you want to withdraw?\n'))
    if food_withdrawal <= budget_food.balance:
        new_foodBalance = budget_food.balance - food_withdrawal
        print('food===>', (budget_food.deposit + food_deposit, food_withdrawal, new_foodBalance))
    else:
        print("You don't have enough balance, reduce the amount or select another category!")
elif (selectedOption == 2) :
    clothing_withdrawal = int(input('How much do you want to withdraw?\n'))
    if clothing_withdrawal <= budget_clothing.balance:
        new_clothingBalance = budget_clothing.balance - clothing_withdrawal
        print('clothing===>', (budget_clothing.deposit + clothing_deposit, clothing_withdrawal, new_clothingBalance))
    else:
        print("You don't have enough balance, reduce the amount or select another category!")
elif (selectedOption == 3) :
    entertainment_withdrawal = int(input('How much do you want to withdraw?\n'))
    if entertainment_withdrawal <= budget_entertainment.balance:
        new_entertainmentBalance = budget_entertainment.balance - entertainment_withdrawal
        print('entertainment===>', (budget_entertainment.deposit + entertainment_deposit, entertainment_withdrawal, new_entertainmentBalance))
    else:
        print("You don't have enough balance, reduce the amount or select another category!")
else:
    print('You have made an invalid selection! Please try again!')


# I find it really difficult to include the transfer option and the whole program is not satisfying.
