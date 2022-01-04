# 100DaysOfCode Day 2 - Tip Calculator

print('Welcome to the tip calculator!')

bill = float(input('What was the total bill? $'))
people = int(input('How many people split the bill? '))
tip = int(input('What percentage tip would you like to give? 10, 12 or 15? '))

result = (bill * (tip / 100 + 1)) / people

print(f'Each person should pay: ${result:.2f}')
