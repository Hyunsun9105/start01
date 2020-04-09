# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import time
import datetime
import pyautogui
import win32api, win32gui,win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)



start_time = datetime.datetime(2020, 3, 30, 20, 56)
count_time = datetime.datetime.now();
how_long = start_time - datetime.datetime.now()
# datetime.timedelta(300, 42173, 524163)

type(how_long) # <class 'datetime.timedelta'>

count_max = how_long.seconds;

print("count_max=%d"%count_max)

dp=1;

while how_long.seconds <= count_max :
    
    
    x,y=win32api.GetCursorPos();
    dp=dp*-1;
    time.sleep(0.1)
    pyautogui.moveTo(100,100+100*dp,2.0);
    time.sleep(1)
    pyautogui.moveTo(x,y,2.0);
    win32api.keybd_event(0x0d,0,0,0)
 
    how_long = datetime.datetime.now()-count_time;
    
    print(count_max-how_long.seconds,win32api.GetLastInputInfo())
     
    time.sleep(20);

#click(1018,784) #command #1
time.sleep(20);
click(1445, 553) #command #2
#click(1381,554) #start command
time.sleep(20);
#
win32api.keybd_event(0x0d,0,0,0)
#click(3340,520) #command #2

