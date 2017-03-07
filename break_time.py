import time
import webbrowser

breaks = 0

print("This program started on "+time.ctime())
while breaks <3:
    time.sleep(5)
    webbrowser.open("http://www.youtube.com")
    breaks = breaks + 1
