"""
Ada Bubble Tea needs help creating drink_summary for their online order display. Each drink has three options: tea flavor, milk, and boba. The tea flavor options are oolong ($4.50), jasmine ($4.50), and silver needle ($5.00). The milk options are none ($0.00), dairy ($0.50), oat ($0.75), and soy ($0.50). The boba options are yes ($0.50), and no ($0.00).
Create the helper function calculate_total. It takes in parameters representing the order, and calculates the total to be used in drink_summary.
"""

def calculate_total(flavor, milk, boba):
    total = 0
    if flavor == "oolong" or flavor == "jasmine":
        total += 4.50
    else: total += 5

    if milk == 'dairy' or milk == "soy":
        total += 0.50
    elif milk == 'oat':
        total += 0.75
    
    if boba == 'yes':
        total += 0.50
    
    return total

def drink_summary(flavor, milk, boba):
    total = calculate_total(flavor, milk, boba)

    print('*** Drink Summary ***')
    drink_display = flavor.capitalize()
    if milk != 'none' or boba != 'no':
        drink_display = drink_display + ' with '
    if milk != 'none':
        drink_display = drink_display + milk + ' milk'
    if milk != 'none' and boba != 'no':
        drink_display = drink_display + ' and '
    if boba != 'no':
        drink_display = drink_display + 'boba'
    
    print(drink_display)
    print(f'Drink total: {total}')

drink_summary('silver needle', 'oat', 'yes')