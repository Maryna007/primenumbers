import time
from math import sqrt

start_time = time.time()  # clock start


def array(bottom_value, top_value):
    number_array = []  # create an array
    while bottom_value != top_value + 1:
        number_array.append(bottom_value)
        bottom_value += 1
    return number_array


def sieve(top_value):
    sq = int(sqrt(top_value))  # top checked value
    current_value = 1  # start value
    tab = array(1, top_value)  # create an array
    while True:
        if current_value > sq:  # final condition
            return tab

        for i in tab:  # loop for the whole array
            if (not (i % current_value) and not (current_value == i)) and current_value != 1:
                tab.remove  # array cell delete

        i = tab.index(current_value) + 1
        current_value = tab[i]


n = 1000
prime_number_array = sieve(n)  # create prime number array
for prime_number in prime_number_array:  # printing loop
    print(prime_number)  # print results

print("--- %s seconds ---" % (time.time() - start_time))  # clock stop and print clock time