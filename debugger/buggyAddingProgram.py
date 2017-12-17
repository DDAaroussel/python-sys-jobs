#! python3
# buggy number adding code to illustrate use of debugger

print('Enter the first number in the sum:')
first = input()
print('first is type:' + str(type(first)))

print('Enter the second number to be added:')
second = input()
print('second is type:' + str(type(second)))

print('Enter the third number to be added:')
third = input()
print('third is type:' + str(type(third)))

total = sum([first, second, third])

print('The sum is: ' + str(total))
