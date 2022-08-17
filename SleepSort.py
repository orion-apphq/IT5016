# https://gist.github.com/armorasha/47c7236cdfe25a928080692324d7f035
# This program sorts a list of integers by running and sleeping multiple threads by the int amount of time then printing the int

import _thread #imports the threading API module so we can work with multiple threads at once
from time import sleep #imports the sleep function from the time module

items = [2, 4, 5, 2.5, 1, 7] # define list of integers to be sorted

def sleep_sort(n): # define sleep_sort to be a function with parameter n where n is an int from the list to be sorted
        sleep(n) # pauses the function for n amount of time
        print(n) # prints n to the screen

for i in items: # loops over each item in the list
        arg_tuple = (i,)
        _thread.start_new_thread(sleep_sort, arg_tuple) # starts a new thread for each item in list then runs the sleep_sort function on it
