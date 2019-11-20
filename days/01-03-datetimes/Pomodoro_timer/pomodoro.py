from datetime import datetime
from datetime import timedelta
import time
import sys
import os
import winsound
from pathlib import Path

this_file = Path(__file__).resolve()
app_path = this_file.parent
sys.path.insert(0, str(app_path))

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def pomodoro_time(num_mins, t_step=1):
    '''
    Tomoato timer for 
    '''
    start_time = time.time()
    end_time = start_time + round(60*num_mins)
    current_time = start_time
    number_of_loops = round((end_time - start_time) / t_step)

    while current_time <= end_time:
        current_time = time.time()
        progress = round((current_time - start_time) / t_step)
        time_elapsed = (current_time - start_time)/60
        printProgressBar(progress, number_of_loops, length=25)
        time.sleep(t_step)
    
    print('Timer Finished!!!!!')

def get_num_mins():
    input_mins = input("\nHow many minutes? \n")
    try: 
        mins = float(input_mins)
    except:
        print('input must be a number')

    print('\n')
    return mins

def pomodoro_datetime(t_step = 1):
    num_mins = get_num_mins()
    start_time = datetime.now()
    end_time = start_time + timedelta(0,round(num_mins*60))
    current_time = start_time
    number_of_loops = round((end_time - start_time).seconds / t_step)

    while current_time <= end_time:
        current_time = datetime.now()
        elapsed_time = (current_time - start_time)
        progress = round(elapsed_time.total_seconds() / t_step)
        printProgressBar(progress,
                         number_of_loops,
                         length=25,
                         decimals = 0, 
                         printEnd='{:02}:{:02}:{:02}'.format(progress // 3600,
                                                             progress % 3600 // 60, 
                                                             progress % 60))
        time.sleep(t_step)
    
    print('\n\nTimer Finished!!!!!')



pomodoro_datetime()