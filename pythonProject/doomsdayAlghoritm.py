def isInt(value):
    if value is None:
        return False
    try:
        int(value)
        return True
    except:
        return False


def yearIntoList(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums


def getYearInCentury(listNumber):
    if len(listNumber) > 1:
        yearInCentury = 10 * listNumber[1] + listNumber[0]
    else:
        yearInCentury = listNumber[0]

    return yearInCentury


def isLeapYear(year):
    if year % 4 == 0:
        return True
    else:
        return False


def isMonthValid(month: int) -> bool:
    if 1 > month or month > 12:
        return False
    else:
        return True


def isDayValid(day: int, month: int, leap: bool) -> bool:
    monthRange = {
        1: 31,
        2: 29 if leap else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if day > monthRange[month] or day < 1:
        return False
    else:
        return True


def findCentury(year: int) -> int:
    k = year // 400
    year_in_cycle = year % 400

    if 0 <= year_in_cycle <= 99:
        century = 2
    elif 100 <= year_in_cycle <= 199:
        century = 0
    elif 200 <= year_in_cycle <= 299:
        century = 5
    elif 300 <= year_in_cycle <= 399:
        century = 3
    else:
        raise ValueError("Year is out of expected range")

    return century


def findYear(year):
    numPos = yearIntoList(year)
    yearInCentury = getYearInCentury(numPos)
    foundYear = False
    k: int = 0
    while not foundYear:
        if 0 + 12 * k <= yearInCentury < 12 + 12 * k:
            foundYear = True
            # print("Year in century: " + str(yearInCentury) + ", value: " + str(k))
            return k
        else:
            k = k + 1


def findRemainder(year):
    listOfNumbers = yearIntoList(year)
    yearInCentury = getYearInCentury(listOfNumbers)

    remainder = yearInCentury % 12
    leapYears = remainder // 4
    result = remainder + leapYears

    # print("Year in century: " + str(yearInCentury) + ", remaining years: " + str(remainder) + ", leap years in that: " + str(leapYears) + ", sum: " + str(result))
    return result


def findDoomsday(year):
    century = findCentury(year)
    yearInCentury = findYear(year)
    remainder = findRemainder(year)
    result = century + yearInCentury + remainder
    dayOfTheWeek = result % 7
    return dayOfTheWeek


def calcDay(specialDay, day, doomsday):
    if day > specialDay:
        result = (doomsday + (day - specialDay)) % 7
    else:
        result = (doomsday + (day - specialDay)) % 7
        # print(str(result) + " = " + "(" + str(doomsday) + " + (" + str(day) + " - " + str(specialDay) + ")) % 7")
    return result


def finalDay(month, day, doomsday, leap):
    doomsdays = {
        1: 4 if leap else 3,
        2: 29 if leap else 28,
        3: 14,
        4: 4,
        5: 9,
        6: 6,
        7: 11,
        8: 8,
        9: 5,
        10: 10,
        11: 7,
        12: 12
    }

    if month in doomsdays:
        return calcDay(doomsdays[month], day, doomsday)
    else:
        raise ValueError("Invalid month")


fin = False
while not fin:
    print("Please provide a date (day.month.year)")

    inputSuccess = False
    while not inputSuccess:
        value1 = input("Day: ")
        value2 = input("Month: ")
        value3 = input("Year: ")

        if isInt(value1) and isInt(value2) and isInt(value3):
            day = int(value1)
            month = int(value2)
            year = int(value3)

            if year > 0:
                isLeap = isLeapYear(year)

                if isMonthValid(month):
                    if isDayValid(day, month, isLeap):
                        inputSuccess = True
                        print(f"Date accepted: {day}.{month}.{year}")
                    else:
                        print(f"Invalid day for the given month: {day} is not valid for month {month}")
                else:
                    print(f"Invalid month: {month}. Please enter a month between 1 and 12.")
            else:
                print(f"Invalid year: {year}. Please enter a year greater than 0.")
        else:
            print("Day, month, and year must be valid integers.")

    dayList = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    doomsday = findDoomsday(year)
    doomsdayOfChosenYear = dayList[doomsday]

    leap = isLeapYear(year)
    yesOrNo = None
    if leap:
        yesOrNo = "a leap year."
    else:
        yesOrNo = "not a leap year."

    print("Doomsday of year " + str(year) + " is " + doomsdayOfChosenYear + " and it is " + yesOrNo)

    result = finalDay(month, day, doomsday, leap)

    weekdayOfChosenDate = dayList[result]

    print("The chosen date: " + str(day) + "." + str(month) + "." + str(year) + " is a " + str(weekdayOfChosenDate))

    end = False
    while not end:
        goOn = input("Do you want to do another calculation? yes or no: ")
        if goOn == "yes" or goOn == "y":
            end = True
        elif goOn == "no" or goOn == "n":
            fin = True
            end = True
            print("Thank you, have a nice day!")
        else:
            end = False
