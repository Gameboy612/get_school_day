import json

from datetime import date


f = open('day.json', encoding='utf-8')

data = json.load(f)

f.close()

def get_start_day():
    if date.today().month >= 9:
        return date(date.today().year, 9, 1)
    else:
        return date(date.today().year - 1, 9, 1)


# https://stackoverflow.com/questions/43692340/how-to-find-number-of-mondays-or-any-other-weekday-between-two-dates-in-python
# https://www.geeksforgeeks.org/weekday-function-of-datetime-date-class-in-python/
def num_days_between( start, end, week_day):
    num_weeks, remainder = divmod( (end-start).days, 7)
    if ( week_day - start.weekday() ) % 7 < remainder:
       return num_weeks + 1
    else:
       return num_weeks


def getDaysFrom9_1(year, month, date):
    d0 = get_start_day()
    d1 = date(year, month, date)
    delta = d1 - d0
    return delta.days


def getHolidays(year, month, day):
    total = 0
    if month >= 9:
        d0 = date(year, 9, 1)
        # Holidays in before Last Month
        for i in range(9, month):
            for x in data['holidays'][str(d0.year)][str(i)]:
                total += 1
        if str(month) in data['holidays'][str(d0.year)].keys():
            for x in data['holidays'][str(d0.year)][str(month)]:
                if x <= day:
                    total += 1
                else:
                    return total
    else:
        d0 = date(year - 1, 9, 1)
        # Holidays in before Last Month
        for i in range(9, 13):
            for x in data['holidays'][str(d0.year)][str(i)]:
                total += 1
        for i in range(1, month):
            for x in data['holidays'][str(d0.year + 1)][str(i)]:
                total += 1
        if str(month) in data['holidays'][str(d0.year + 1)].keys():
            for x in data['holidays'][str(d0.year + 1)][str(month)]:
                if x <= day:
                    total += 1
                else:
                    return total
    return total


def getEvents(year, month, day):
    total = 0
    if month >= 9:
        d0 = date(year, 9, 1)
        # Events in before Last Month
        for i in range(9, month):
            if str(i) in data['events'][str(d0.year)].keys():
                for x in data['events'][str(d0.year)][str(i)]:
                    total += 1
        if str(month) in data['events'][str(d0.year)].keys():
            for x in data['events'][str(d0.year)][str(month)]:
                if x['date'] <= day:
                    total += 1
                else:
                    return total
    else:
        d0 = date(year - 1, 9, 1)
        # Events in before Last Month
        for i in range(9, 13):
            if str(i) in data['events'][str(d0.year)].keys():
                for x in data['events'][str(d0.year)][str(i)]:
                    total += 1
        for i in range(1, month):
            if str(i) in data['events'][str(d0.year + 1)].keys():
                for x in data['events'][str(d0.year + 1)][str(i)]:
                    total += 1
        if str(month) in data['events'][str(d0.year + 1)].keys():
            for x in data['events'][str(d0.year + 1)][str(month)]:
                if x['date'] <= day:
                    total += 1
                else:
                    return total
    return total

def getSkips(year, month, day):
    total = 0
    if month >= 9:
        d0 = date(year, 9, 1)
        # Skips in before Last Month
        for i in range(9, month):
            if str(i) in data['skips'][str(d0.year)].keys():
                for x in data['skips'][str(d0.year)][str(i)]:
                    total += 1
        if str(month) in data['skips'][str(d0.year)].keys():
            for x in data['skips'][str(d0.year)][str(month)]:
                if x <= day:
                    total += 1
                else:
                    return total
    else:
        d0 = date(year - 1, 9, 1)
        # Skips in before Last Month
        for i in range(9, 13):
            if str(i) in data['skips'][str(d0.year)].keys():
                for x in data['skips'][str(d0.year)][str(i)]:
                    total += 1
        for i in range(1, month):
            if str(i) in data['skips'][str(d0.year + 1)].keys():
                for x in data['skips'][str(d0.year + 1)][str(i)]:
                    total += 1
        if str(month) in data['skips'][str(d0.year + 1)].keys():
            for x in data['skips'][str(d0.year + 1)][str(month)]:
                if x <= day:
                    total += 1
                else:
                    return total
    return total



def getWeekends(year, month, day):
    d0 = get_start_day()
    return num_days_between(d0, date(year, month, day), 5) + num_days_between(d0, date(year, month, day), 6)


def getHoliday(year, month, day):
    try:
        for x in data['holidays'][str(year)][str(month)]:
            if x == day:
                return 1
    except:
        pass
    return -1

def getEvent(year, month, day):
    try:
        for x in data['events'][str(year)][str(month)]:
            if x["date"] == day:
                return x["event"]
    except:
        pass
    return -1

def getExtra(year, month, day):
    try:
        for x in data['extra'][str(year)][str(month)]:
            if x["date"] == day:
                return x["event"]
    except:
        pass    
    return -1

            
            



def getDay(year, month, day):
    no_count = getHolidays(year, month, day) + getEvents(year, month, day) + getWeekends(year, month, day) - getSkips(year, month, day)

    in_between_days = (date(year, month, day) - get_start_day()).days

    days = in_between_days - no_count

    monthnames = {1: "Janurary", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

    daynames = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth", 7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelveth", 13: "thirteenth", 14: "fourteenth", 15: "fifteenth", 16: "sixteenth", 17: "seventeenth", 18: "eighteenth", 19: "nineteenth", 20: "twentieth", 21: "twenty-first", 22: "twenty-second", 23: "twenty-third", 24: "twenty-fourth", 25: "twenty-fifth", 26: "twenty-sixth", 27: "twenty-seventh", 28: "twenty-eighth", 29: "twenty-ninth", 30: "thirtieth", 31: "thirty-first"}

    if (event := getEvent(year, month, day)) != -1:
        return f"the {daynames.get(day)} of {monthnames.get(month)}, {year}, is {event}."
        
    if getHoliday(year, month, day) != -1:
        return f"the {daynames.get(day)} of {monthnames.get(month)}, {year}, is a holiday."

    if date(year, month, day).weekday() == 5:
        return f"the {daynames.get(day)} of {monthnames.get(month)}, {year}, is Saturday."
    if date(year, month, day).weekday() == 6:
        return f"the {daynames.get(day)} of {monthnames.get(month)}, {year}, is Sunday."

    return f"the {daynames.get(day)} of {monthnames.get(month)}, {year}, is day {days % 6 + 1}."



def loadDay(date):
    year = date.year
    month = date.month
    day = date.day
    print(getDay(year, month, day))
    if (event := getExtra(year, month, day)) != -1:
        print(f"As an extra remark, that day is {event}.")

loadDay(date.today())
loadDay(date(2022, 10, 19))