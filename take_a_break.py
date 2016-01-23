# Lesson 3.2: Use Functions
# Mini-Project: Take a Break

# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.

# Use this space to describe your approach to the problem.
# Step 1: Set loop count to 0
# Step 2: Start timer
# Step 3: Count to two hours
# Step 4: Play break file
# Step 5: Increment loop count and restart loop
# Step 6: Stop loop after third iteration

import time
import webbrowser

def breaktime():
    breaks = 0
    total = 3
    print "This program started on " + time.ctime()
    while breaks < total:
        time.sleep(10)
        webbrowser.open("https://www.youtube.com/watch?v=JNOpKwnAQyw")
        breaks += 1
        print "Break time! Break #" + str(loop) + " started on " + time.ctime()
    else:
        print "No more breaks!"
        raise SystemExit

breaktime()

# abstraction: the hiding of detail in programming
