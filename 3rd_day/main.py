#!/usr/bin/python3

from types import new_class
from typing import List

def reverse_binary_string(binary):
    digits = list(binary)

    for index in range(0, len(digits)):
        if digits[index] == '1':
            digits[index] = '0'
        else:
            digits[index] = '1'
            
    return "".join(digits)


def day_3_part_1():
    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    first_binary_string = lines[0].strip('\n')
    length_binary = len(first_binary_string)

    gamma_rate = '000000000000'

    for index in range(0, length_binary):
        ones_counter = 0
        zeros_counter = 0

        for line in lines:
            binary_string = line.strip('\n')
    
            if binary_string[index] == '1':
                ones_counter += 1
            else:
                zeros_counter += 1
    
        if (ones_counter >= zeros_counter):
            gamma_rate = gamma_rate[:index] + '1' + gamma_rate[index + 1:]
    
    List = list(reverse_binary_string(gamma_rate))              
    epsilon_rate = int("".join( str(i) for i in List), 2)           # epsilon rate in decimal           
    List = list(gamma_rate)
    gamma_rate = int("".join( str(i) for i in List), 2)             # gamma rate in decimal
 
    return gamma_rate * epsilon_rate

def get_oxygen_generator_rating():
    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    first_binary_string = lines[0].strip('\n')
    length_binary = len(first_binary_string)

    for index in range(0, length_binary):
        ones_counter = 0
        zeros_counter = 0

        first_filter = []
        second_filter = []

        for line in lines:
            binary_string = line.strip('\n')
    
            if binary_string[index] == '1':
                ones_counter += 1
                first_filter.append(binary_string)
            else:
                zeros_counter += 1
                second_filter.append(binary_string)
    
        if (ones_counter >= zeros_counter):
            lines = first_filter
        else:
            lines = second_filter
        
        if len(lines) == 1:
            break

    List = list(lines[0])

    oxygen_generator_rating = int("".join(str(i) for i in List), 2)
 
    return oxygen_generator_rating

def get_CO2_scubber_rating():
    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    first_binary_string = lines[0].strip('\n')
    length_binary = len(first_binary_string)

    for index in range(0, length_binary):
        ones_counter = 0
        zeros_counter = 0

        first_filter = []
        second_filter = []

        for line in lines:
            binary_string = line.strip('\n')
    
            if binary_string[index] == '1':
                ones_counter += 1
                first_filter.append(binary_string)
            else:
                zeros_counter += 1
                second_filter.append(binary_string)
    
        if (zeros_counter <= ones_counter):
            lines = second_filter
        else:
            lines = first_filter

        if len(lines) == 1:
            break
        
    List = list(lines[0])

    C02_scubber_rating = int("".join(str(i) for i in List), 2)
 
    return C02_scubber_rating

def day_3_part_2():
    oxygen_generator_rating = get_oxygen_generator_rating()
    CO2_scubber_rating = get_CO2_scubber_rating()

    return oxygen_generator_rating * CO2_scubber_rating

def main():
    result = day_3_part_1()
    print("The power consumption for the sumbarine: ", result)
    result = day_3_part_2()
    print("Life support of the submarine: ", result)

if __name__ == '__main__':
    main()
