# This is just a thread for the loading screen while the program finishes scrapping results.

import sys
import time


def run(stop_event):
    print("Loading",end='')
    sys.stdout.flush()
    dots = "...."
    while not stop_event.is_set():
        for i in dots:
            time.sleep(0.5)
            print(i,end='')
            sys.stdout.flush() 
        line_len = len("Loading" + dots)
        print('\r' + ' ' * line_len + '\r', end='')
        sys.stdout.flush()
    
