def add_time(start, duration, day_arg=''):
    AM_PM = start[-2:]
    bracket_string = ''
    days_later = 0
    days_array = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
    start_time = [start.split(":")[0],start.split(":")[1].split(" ")[0]]
    duration_time = duration.split(":")
    new_minutes = int(start_time[1]) + int(duration_time[1])
    new_hours = int(start_time[0]) + int(duration_time[0])
    if new_minutes>59:
        mins = new_minutes % 60
        hrs = new_minutes//60
        new_minutes = mins
        new_hours = new_hours + hrs
    if new_hours >= 12:
        mod_hours = new_hours % 12
        quot = new_hours // 12
        new_hours = mod_hours
        if AM_PM == "PM":
            days_later = int((quot+1)/2)
        elif AM_PM == "AM" and quot>1:
            days_later = int((quot+1)/2)
        else:
            days_later = 0
        if days_later > 0:
            if days_later != 1:
                bracket_string = " "+"("+str(days_later)+" "+"days later"+")"
            else:
                bracket_string = " "+"(next day)"
        if ((mod_hours == 0) or(quot % 2) != 0):
            if AM_PM == "PM":
                AM_PM = "AM"
            else:
                AM_PM = "PM"  
            if new_hours == 0:
                new_hours = 12
    if day_arg == "":
        new_day = day_arg.upper()
        new_time = str(new_hours)+":"+str(f"{new_minutes:02d}")+" "+AM_PM+bracket_string
    else:
        new_day = days_array[(days_array.index(day_arg.upper()) + days_later) % 7]
        new_time = str(new_hours)+":"+str(f"{new_minutes:02d}")+" "+AM_PM+","+" "+new_day.capitalize()+bracket_string

    return new_time