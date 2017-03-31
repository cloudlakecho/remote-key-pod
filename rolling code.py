

# from February 8 2017 to
# Malibu and Burbank in California
# Woon Ho "Cloud" Cho
# Cyber security project: hacking remote key pod signal

# source patent US 6980655

# receiving rolling code
# (1) reverse order of binary digits
# -> (2) zero the most significant digit

# -> (3) set initial trinary rolling code to zero
# (3 explanation) -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          (in other way, there could be noise in the first three codes)
# (3 my thought) - (something like power of three)

# -> (4) subtract next highest power of three from rolling code
# (4 my thought) - (if rolling code is 011, next highest bit is 1 and 3**2 would be substracted
#   from the rooling code. For example in this case 011 = 3, 3 - 3**2)
# -> (4-1) if result is bigger than zero
# -> (4-1-1) increment next most significant digit of binary rolling code
# (4-1-1 my thought) - (the next most significant digit is 1 at 011 -> 100)
# -> (4-2) if result is smaller or equal to zero
# -> (4-2-1) add next highest power of three to rolling code
# (4-2-1 my thought) - (011 + 3**1 because the next highest digit is 1)
# -> (4-2-2) next highest power of three
# (4-2-2 my thought) - (011 there is no more next highest digit)

# making the rolling code
#
# issue
#   'str' object does not support item assignment - February 22, 2017


from numpy import *
import random
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def fabricate(total_bit):
    rolling_code = "" # if " ", it will be space at the for front
    for i in range(total_bit):
        each_digit = random.random()
        #float (each_digit = random.random())
        rolling_code += chr( round(each_digit)+48 )
    return rolling_code

def char_to_decimal(rolling_code):
    rolling_code_converted = 0
    for i in range(len(rolling_code)):
        if (rolling_code[i] == '1'):
            rolling_code_converted += 2**(len(rolling_code)-i-1)
    return rolling_code_converted
    
def read(rolling_code):
    # (1)
    rolling_code = rolling_code[::-1]
    print (rolling_code)

    # (2)
    rolling_code_decimal = char_to_decimal(rolling_code)
    print("Rolling code in decimal: %d" % rolling_code_decimal) 
    for i in range(len(rolling_code)):
        if (rolling_code[i] == '1'):
            rolling_code = rolling_code[:i] + '0' + rolling_code[i+1:]
            #rolling_code[i] = '0' ## error spot: 'str' object does not support item assignment
            print("At the step 2, location is %d" % i)
            print("The rolling code: %s" % rolling_code)
            break
        elif ( (i==len(rolling_code)-1) and (rolling_code[i] != '1') ):
            print ("the rolling code is all zero.")

    # (3) skipped because not sure

    # (4)
    rolling_code_decimal = char_to_decimal(rolling_code)
    for j in range(i+1,len(rolling_code)): # it should start from i because next
        if (rolling_code[j] == '1'):
            n_h_p_o_t = 3**(len(rolling_code)-j)
            output_4 = rolling_code_decimal - n_h_p_o_t 
            print("At the step 4, location is %d" % j)
            print("The rolling code: %d, next highest power of three: %d" % (rolling_code_decimal, n_h_p_o_t) )

            if (output_4 > 0):
                print("The result of step four is %d, so it is case 4-1" % output_4)
            else:
                print("The result of step four is %d, so it is case 4-2" % output_4)
            break
                    
            
            
    
if __name__ == '__main__':
    total_bit = 5;
    rolling_code = fabricate(total_bit)
    print("The rolling code is %s" % rolling_code)
##    for i in range(len(rolling_code)):
##        print(i, ": ", rolling_code[i])
    rolling_code_read = read(rolling_code)
    
