#! python3
# calcProd.py to calculate run time of program

import time
def calcProd():
    #Calculate the product of the  first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

start_time = time.time()
prod = calcProd()
end_time = time.time()

print('the number is %s long' % (len(str(prod))))
print('the run time is %s seconds' % (end_time - start_time))
