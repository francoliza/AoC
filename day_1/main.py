#!/usr/bin/python3

def day_1_part_1():
    file1 = open('day1_input.txt', 'r')
    lines = file1.readlines()
    count = 0
    
    last_number = -1

    for line in lines:
        current_number = int(line)
        if last_number != -1:
            if last_number < current_number:
                count += 1
        last_number = current_number

    return count

def day_1_part_2():
    file1 = open('day1_input.txt', 'r')
    lines = file1.readlines()
    counter = 0
    tmp_array = [0, 0, 0]
    sum_array = []
    
    for line in lines:
        current_number = int(line)
        tmp_array[counter % 3] = line

        # Primero obtenemos los sumados
        counter += 1
        if (counter >= 3):
            sum_numbers = 0
            for number in tmp_array:
                sum_numbers += int(number)
            sum_array.append(sum_numbers)

        # Luego hacemos lo mismo que en la parte uno pero con los array sumados 

    count = 0
    last_number = -1

    for current_number in sum_array:
        if last_number != -1:
            if last_number < current_number:
                count += 1
        last_number = current_number
    
    return count

def main():
    result = day_1_part_1()
    print("part 1: ", result)
    result = day_1_part_2()
    print("part 2: ", result)

if __name__ == "__main__":
    main()
