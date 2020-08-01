from datetime import datetime
import csv

# calculate the number of hours between start and end times


def timeDifference(start, end):
    return round((end - start).seconds / 3600, 2)


# Calculate amount earned (Rate=5)
def getAmountEarned(timeDifference):
    return round(timeDifference*5, 2)


# get start time, end time(with date) and timeDifference, total amount to the csv file
def addToFile(start, end, timeDifference, totalAmount):
    toAdd = [[start, end, timeDifference, timeDifference, totalAmount]]
    with open('calc.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(toAdd)


# start Date and Time
def getDateAndTimeInput(endOrStart):
    Date = input(f'Enter {endOrStart} date in YYYY-MM-DD: ')
    year, month, day = map(int, Date.split('-'))
    Time = input(f'Enter {endOrStart} time in HH:MM 24hr ')
    hour, minute = map(int, Time.split(':'))
    return datetime(year, month, day, hour, minute)


# append new rows to csv files
def addToFile(start, end, timeDifference, totalAmount):
    toAdd = [[start, end, timeDifference, totalAmount]]
    with open('calc.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(toAdd)

# print start, end, time worked and amount earned


def printStatsScreen(start, end, timeDifference, totalAmount):
    print('Start: ', start)
    print('End: ', end)
    print('Hours worked: ', timeDifference)
    print('Amount earned: ', totalAmount)


# error handlers for invalid input
class Error(Exception):
    pass


class InvalidError(Error):
    pass


try:
    choice = input(
        'Do you want to(Enter 1, 2, or 3):\n1) Check-in \n2) Check amount earned on task \n3) View all past tasks\n')
    if (choice != '1' and choice != '2' and choice != '3'):
        raise InvalidError
    choice = int(choice)
    if choice == 1:
        start = datetime.now().replace(microsecond=0)
        end = getDateAndTimeInput('end')
        try:
            if end < start:
                raise DateError
        except DateError:
            print('End time cannot before start time')
        timeDifference = timeDifference(start, end)
        totalAmount = getAmountEarned(timeDifference)
        printStatsScreen(start, end, timeDifference, round(totalAmount, 2))
        addToFile(start, end, timeDifference, totalAmount)
    elif choice == 2:
        start = getDateAndTimeInput('start')
        end = getDateAndTimeInput('end')
        timeDifference = timeDifference(start, end)
        totalAmount = getAmountEarned(timeDifference)
        printStatsScreen(start, end, timeDifference, round(totalAmount, 2))
        addToFile(start, end, timeDifference, totalAmount)
    elif choice == 3:
        with open('calc.csv') as file:
            reader = csv.reader(file)
            totalAmount = 0

            if len(list(reader)) != 0:
                print(len(list(reader)))
                print(
                    '------------------------------------------------------------------------')
                print(
                    """|   Start            |   End             |Hours worked|Amount Earned    |""")
                print(
                    '------------------------------------------------------------------------')
                for row in reader:
                    totalHours += float(row[2])
                    totalAmount += float(row[3])
                    if row[2][-2] == '.':
                        print('| '+row[0] + '|' + row[1] + '|   ' +
                              row[2] + '      |' + row[3]+'             |')
                    else:
                        print('| '+row[0] + '|' + row[1] + '|   ' +
                              row[2] + '     |' + row[3]+'             |')
                    print(
                        '------------------------------------------------------------------------')
                    print()
                    print(
                        f'You have worked a total of  {totalHours} hours  and earned ${totalAmount} ')
                    print()
            else:
                print('You have no past data')

    print()
    print('Exiting now')
    print()
except InvalidError:
    print('Wrong input... exiting')
