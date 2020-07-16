def add_time(start, duration, dayofWeek=''):
    # Calculates the end time by adding duration to start time and returns this as new_time
    dayofWeek = dayofWeek.lower()
    # Extracting hours and minutes from start
    timeofday = start[-2:]
    temp = start.split(':')
    StartHour = temp[0]
    temp = temp[1]
    StartMinutes = temp[0:2]
    # Extracting hours and minutes from duration
    temp = duration.split(':')
    Hours = temp[0]
    Minutes = duration[-2:]
    # Cast to int
    StartHour = int(StartHour)
    StartMinutes = int(StartMinutes)
    Hours = int(Hours)
    Minutes = int(Minutes)
    WeekDays = {0:'monday', 1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday'}
    # Convert StartHour to 24 hour clock
    if timeofday == 'PM':
        StartHour = StartHour + 12
     # Add minutes
    calc_minutes = StartMinutes + Minutes
    new_minutes = calc_minutes%60
    extra_hours = int(calc_minutes/60)
    # Add hours
    new_hours = StartHour + Hours + extra_hours
    num_days = 0
    if new_hours > 24:
        #print('Next day')
        num_days = int(new_hours/24)
        #print("Num days: "+str(num_days))
        new_hours =  new_hours%24
        #print("Num days: " +str(num_days))
    if new_hours > 12:
        # Need to convert back to 12 hour time
        #print("Convert back")
        timeofday = 'PM'
        new_hours = new_hours - 12 
    elif new_hours == 12:
        # Need to convert back to 12 hour time
        #print("Convert back")
        timeofday = 'PM'
    elif new_hours == 0:
        new_hours = 12
        timeofday = 'AM'
    else:
        timeofday = 'AM'
    # Calculate the new_day
    day = ''
    new_day_num = None
    new_day = None
    for key,value in WeekDays.items():
        if dayofWeek == value:
            day = key
    #print(day)
    if day != '':
        new_day_num = int(day) + num_days
        #print(str(new_day_num))
        new_day_num = new_day_num%7
        #print(str(new_day_num))
        new_day = WeekDays.get(new_day_num)
        new_day = new_day.capitalize()
 
    # Construct the new_time
    new_time = str(new_hours)+':'+str(new_minutes).zfill(2)+' '+timeofday
    # Add day of week
    if new_day != None:
        new_time += ", "+new_day
    if num_days == 1:
        new_time += ' (next day)'
    elif num_days > 1:
        new_time += ' ('+str(num_days)+' days later)'
    else:
        new_time = new_time
    #print(new_time)
    return new_time