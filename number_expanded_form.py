# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    expand = str(num)  # convert to string
    len_str = len(expand)
    temp = '' # create empty string
    for i in range(len_str):
        if expand[i] != "0": # skipping zero
            zero = (len_str-i-1) * "0" # create numberof zero
            step = expand[i] + zero # add zeros to digit
            temp += step
        if i == len_str-1: # if we are on last digit just break
            break
        if expand[i+1] != "0": # if next dig is not the zero
            temp += " + "
    return temp
