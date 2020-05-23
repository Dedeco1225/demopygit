import time
import webbrowser


time.sleep(10)

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(10)    
    webbrowser.open("https://www.youtube.com/watch?v=1_9RSD8-ENs")
    break_count = total_break + 1 
