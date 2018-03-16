

# from February 8 2017 to
# Malibu, California
# San Diego, California

# source patent US 6980655

# receiving rolling code
# reverse order of binary digits -> zero the most significant digit -> set initial trinary
# rolling code to zero -> subtract next highest power of three from rolling code ->
# result is bigger than zero -> increment next most significant digit of binary rolling code
# result is smaller or equal to zero -> add next highest power of three to rolling code ->
# next highest power of three

# making the rolling code
#

# Python 3.5 code


import numpy as np
import random
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from numpy import *


def run(total_bit):
    each_digit = 0
    rolling_code = []
    for i in range(total_bit):
        if random.random() > 0.5:
            each_digit = random.randint(65, 91)
        else:
            each_digit = random.randint(97, 123)
        rolling_code.append(chr(each_digit))
    return rolling_code


def main():
    total_bit = 40;
    total_num = 40;
    rolling_code = run(total_bit)
    # print("The rolling code is %s" % rolling_code)
    group = [run(total_bit) for i in range(total_num)]
    # print(type(group), len(group), len(group[0]))
    group_2D = np.asarray(group).reshape(total_bit, total_num)
    print(group_2D)
    print(type(group_2D[0, 0]))


if __name__ == '__main__':
    main()