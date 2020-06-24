machine_water = 400
machine_milk = 540
machine_coffee = 120
machine_cups = 9
machine_money = 550

espresso_water = 250
espresso_coffee = 16
espresso_cost = 4

latte_water = 350
latte_milk = 75
latte_coffee = 20
latte_cost = 7

cappuccino_water = 200
cappuccino_milk = 100
cappuccino_coffee = 12
cappuccino_cost = 6

def buy ():
print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu:')
choice = input()

global machine_water
global machine_coffee
global machine_milk
global machine_money
global machine_cups

if choice == '1':
if machine_water < espresso_water:
print('Sorry, not enough water!')
elif machine_cups < 1:
print('Sorry, not enough water!')
elif machine_coffee < espresso_coffee:
print('Sorry, not enough coffee!')
elif machine_milk < 0:
print('Sorry, not enough milk!')
else:
print('I have enough resources, making you a coffee!')
machine_water -= espresso_water
machine_coffee -= espresso_coffee
machine_cups -= 1
machine_money += espresso_cost

elif choice == '2':
if machine_water < latte_water:
print('Sorry, not enough water!')
elif machine_cups < 1:
print('Sorry, not enough water!')
elif machine_coffee < latte_coffee:
print('Sorry, not enough coffee!')
elif machine_milk < latte_milk:
print('Sorry, not enough milk!')
else:
print('I have enough resources, making you a coffee!')

machine_water -= latte_water
machine_coffee -= latte_coffee
machine_milk -= latte_milk
machine_cups -= 1
machine_money += latte_cost

elif choice == '3':
if machine_water < cappuccino_water:
print('Sorry, not enough water!')
elif machine_cups < 1:
print('Sorry, not enough water!')
elif machine_coffee < cappuccino_coffee:
print('Sorry, not enough coffee!')
elif machine_milk < cappuccino_milk:
print('Sorry, not enough milk!')
else:
print('I have enough resources, making you a coffee!')
machine_water -= cappuccino_water
machine_coffee -= cappuccino_coffee
machine_milk -= cappuccino_milk
machine_cups -= 1
machine_money += cappuccino_cost

elif choice == 'back':
coffee_machine()

else:
print('Wrong Choice')

def fill ():
print('Write how many ml of water do you want to add:')
added_water = int(input())

print('Write how many ml of milk do you want to add:')
added_milk = int(input())

print('Write how many grams of coffee beans do you want to add:')
added_coffee = int(input())

print('Write how many disposable cups of coffee do you want to add:')
added_cups = int(input())

global machine_water
global machine_coffee
global machine_milk
global machine_money
global machine_cups

machine_water += added_water
machine_coffee += added_coffee
machine_milk += added_milk
machine_cups += added_cups 

def take ():
global machine_money
print('I gave you ${}'.format(machine_money))
machine_money = 0

def remaining():
print('''The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money'''.format(machine_water, machine_milk, machine_coffee, machine_cups, machine_money))

def coffee_machine():
while True:
print('Write action (buy, fill, take, remaining, exit):')
action = input()
if action == 'buy':
buy()
elif action == 'fill':
fill()
elif action == 'take':
take()
elif action == 'remaining':
remaining()
elif action == 'exit':
exit()

coffee_machine()
