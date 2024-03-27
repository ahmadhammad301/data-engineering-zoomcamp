import sys
import pandas as pd
import time

print(sys.argv)

if len(sys.argv)>1:
    day = sys.argv[1]
else:  
    day = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


print(f"the job finished successfully for day {day}")