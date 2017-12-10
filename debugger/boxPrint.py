#! python3
# test code to illustrate the raise Exception
# , try and except statements.

def boxPrint(symbol, width, height):
       if len(symbol) != 1:
         raise Exception('Symbol must be a single character string.')
       if width <= 2:
         raise Exception('Width must be greater than 2.')
       if height <= 2:
         raise Exception('Height must be greater than 2.')
       print(symbol * width)
       for i in range(height - 2):
           print(symbol + (' ' * (width - 2)) + symbol)
       print(symbol * width)

for sym,w,h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym,w,h)
    except Exception as err:
        print('Error has occured...' + str(err))
