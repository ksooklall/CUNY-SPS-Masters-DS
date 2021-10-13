def black_board():
    employees = 1
    hr_rate =[(int(i.split(',')[0]),int(i.split(',')[1])) for i in [input('How many hours did you work and at what rate ex(20,15): ') for i in range(employees)]]

    pays = [20 * rate + (hours - 20) * 1.5 * rate if hours > 20 else hours * rate for hours,rate in hr_rate]
    print(pays)

def slack():
    roomDict = {602: 4444, 605: 5555, 621: 6666}
    teachDict = {602: 'NS', 605: 'LF', 621: 'NK'}
    timeDict = {602: 'Wed. 6pm - 7pm', 605: 'Thurs. 8pm - 9pm', 621: 'Wed. 8pm - 9pm'}
    course = int(input('What is your course number: '))

    if course in roomDict:
        print('Course {} is in room {} taught by {} on {}'.format(course, roomDict[course], teachDict[course], timeDict[course]))
    else:
        print('Sorry course {} could not be found'.format(course))

def calculatePay( hours, rate ):
    return rate * hours + max(0,  rate * (hours - 20) / 2)

black_board()
print(calculatePay(30, 15))
