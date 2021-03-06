#! python3
import logging
logging.basicConfig(filename = 'log.txt', level = logging.DEBUG, format ='%(asctime)s- %(levelname)s -%(message)s')
logging.debug('Start of program...')

def factorial(n):
    logging.debug('Start of factorial(%s)...' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('the i value is ' + str(i) + ' and the total is ' + str(total))
    logging.debug('End of factorial(%s)...' % (n))
    return total

print(factorial(5))
logging.debug('End of program...')
