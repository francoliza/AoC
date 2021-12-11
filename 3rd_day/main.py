#!/usr/bin/python3

from types import new_class

def reverse_binary_string(binary):
    digits = list(binary)

    for index in range(0, len(digits)):
        if digits[index] == '1':
            digits[index] = '0'
        else:
            digits[index] = '1'
            
    return "".join(digits)


def day_3_part_1():
    file1 = open('input_1.txt', 'r')
    lines = file1.readlines()

    first_binary_string = lines[0].strip('\n')
    length_binary = len(first_binary_string)

    gamma_rate = '000000000000'

    for index in range(0, length_binary):
        one_counter = 0
        zero_counter = 0

        for line in lines:
            binary_string = line.strip('\n')
    
            if binary_string[index] == '1':
                one_counter += 1
            else:
                zero_counter += 1
    
        if (one_counter >= zero_counter):
            gamma_rate = gamma_rate[:index] + '1' + gamma_rate[index + 1:]
    
    List = list(reverse_binary_string(gamma_rate))              
    epsilon_rate = int("".join( str(i) for i in List), 2)           # epsilon rate in decimal           
    List = list(gamma_rate)
    gamma_rate = int("".join( str(i) for i in List), 2)             # gamma rate in decimal
 
    return gamma_rate * epsilon_rate

def day_3_part_2():
    return 0

def main():
    result = day_3_part_1()
    print(result)

if __name__ == '__main__':
    main()
