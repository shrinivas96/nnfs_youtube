from num2words import num2words
import threading
import datetime

time_check = (0, 0)


def display_time():
    global time_check
    current_time = datetime.datetime.now().strftime("%I %M")
    hour = int(current_time.split()[0])
    minutes = int(current_time.split()[1])
    if (hour, minutes) != time_check:
        time_check = (hour, minutes)
        if 60 - minutes <= 10:
            minutes = 60 - minutes
            hour += 1
            if minutes == 1:
                print("It's {0} minute to {1}".format(num2words(minutes), num2words(hour)))
            else:
                print("It's {0} minutes to {1}".format(num2words(minutes), num2words(hour)))

        elif minutes < 10:
            if minutes == 0:
                print("It's {0} o'clock".format(num2words(hour)))
            else:
                print("It's {0} Oh {1}".format(num2words(hour), num2words(minutes)))

        else:
            print("It's {0} {1}".format(num2words(hour), num2words(minutes)))
    threading.Timer(1, display_time).start()


display_time()