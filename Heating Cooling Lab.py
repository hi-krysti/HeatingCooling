def heating_cooling(actual_temp, desired_temp):
    while actual_temp != desired_temp:
        if actual_temp > desired_temp:
            print('Run A/C')
            actual_temp -= 1
            print(actual_temp)
        elif actual_temp < desired_temp:
            print('Run Heat')
            actual_temp += 1
            print(actual_temp)
    else:
        print('Standby')
    return ' '

print(heating_cooling(15,20))
print(heating_cooling(15,15))
print(heating_cooling(25,20))

actual_temp = int(input('What is the actual temperature of the room? \n'))
desired_temp = int(input('What temperature is desired? \n'))
print(heating_cooling(actual_temp, desired_temp))
