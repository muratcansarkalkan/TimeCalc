def add_time(start, duration, *day):
    # Variables
    new_time = ""
    new_hour = ""
    new_minute = ""
    new_meridiem = ""
    new_day = 0
    day_statement = ""
    days_of_week = [
        "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
    ]

    #rstrip() throws ""s. split(":") splits by :, then it becomes a list. start[1] is the 2nd element of list formed as start.
    start = start.rstrip()
    start = start.split()
    meridiem = start[1]
    meridiem = meridiem.upper()
    time = start[0]
    time = time.split(":")
    start_hour = time[0]
    start_hour = int(start_hour)
    start_minute = time[1]
    start_minute = int(start_minute)
    duration = duration.rstrip()
    duration = duration.split(":")
    dx_hour = duration[0]
    dx_hour = int(dx_hour)
    dx_minute = duration[1]
    dx_minute = int(dx_minute)

    if meridiem == "PM":
      start_hour += 12

    new_hour = start_hour + dx_hour
    new_minute = start_minute + dx_minute

    if new_minute >= 60:
      new_hour += 1
      new_minute -= 60

    if new_hour >= 24:
      new_day = int(new_hour/24)
      new_hour = new_hour % 24

      #day_statement explanation, for new_day being 1 or more.
      if new_day == 1:
        day_statement = "(next day)"
      if new_day > 1:
        day_statement = f"({new_day} days later)"
      
    if new_hour == 0:
      new_hour = 12
      new_meridiem = "AM"
    elif new_hour >= 12:
      new_meridiem = "PM"
      if new_hour > 12:
        new_hour -= 12
    else:
      new_meridiem = "AM"
    
    #we will turn new_minute into a 2 digit integer if it's only a 1 digit int
    new_minute = str(new_minute)
    new_minute = new_minute.zfill(2)

    if day:
        day = day[0]
        # This function is added in order to comply with capitalize property ALL THE TIME
        day = day.capitalize()

        # Match the day to list of days_of_week and pull out the index
        day_index = days_of_week.index(day)
        
        # Total number of days is calulcated above and added into day_statement, allows to cut down on loop or forgo loop while period
        new_day = new_day % 7
        # Return statement with optional arg and same day
        if new_day == 0:
            new_time = f"{new_hour}:{new_minute} {new_meridiem}, {day}"
        # Return statement with optional arg and next day
        elif new_day == 1:
            day_index += 1
            day = days_of_week[day_index]
            new_time = f"{new_hour}:{new_minute} {new_meridiem}, {day} {day_statement}"
        # Logic / Return statement if more than next day and cutting to the next week
        else:
            if new_day + day_index >= 7:
                new_day = day_index - new_day
                day_index = 0
            while new_day > 0:
                new_day -= 1
                day_index += 1
            day = days_of_week[day_index]
            new_time = f"{new_hour}:{new_minute} {new_meridiem}, {day} {day_statement}"

    # Return statement, if it progresses by a day, add the day_statement
    # If *day is included, everything dont above, else complete below
    if day:
        return new_time
    else:
        if day_statement == "":
            new_time = f"{new_hour}:{new_minute} {new_meridiem}"
        else:
            new_time = (
                f"{new_hour}:{new_minute} {new_meridiem} {day_statement}"
            )

    return new_time
