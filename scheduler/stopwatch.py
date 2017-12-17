#! python3
# stopwatch.py to print time elapsed between presses of enter key

now_time = time.time()

print('the time at press is %s' % (now_time))

def time_track():
    input()
    start_time = time.time()
    input()
    end_time = time.time()
    
    lap_number = 1
    start_time =
