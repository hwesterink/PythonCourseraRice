# template for "Stopwatch: The Game"

import simplegui

# define and initialize global variables
time_count = 0
stop_count = 0
zero_count = 0

# helper function format that converts time in
# tenths of seconds into formatted string A:BC.D
def format(t):
    if ( time_count / 600 ) == 10 :
        ten_minutes()
    minutes = time_count / 600
    seconds = ( time_count - minutes * 600 ) / 10
    tenths = time_count % 10
    string = str(minutes) + ":"
    if seconds < 10 :
        string += "0" + str(seconds) + "." + str(tenths)
    else :
        string += str(seconds) + "." + str(tenths)
    return string    

# helper function ten_minutes that resets the timer but
# not the counters and continues
def ten_minutes() :
    global time_count
    timer.stop()
    time_count = 0
    timer.start()

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button() :
    timer.start()
    
def stop_button() :
    global time_count, stop_count, zero_count
    running = timer.is_running()
    timer.stop()
    if running :
        stop_count += 1
        if (time_count % 10) == 0 :
            zero_count += 1
    
def reset_button() :
    global time_count, stop_count, zero_count
    timer.stop()
    time_count = 0
    stop_count = 0
    zero_count = 0

# define event handler for timer with 0.1 sec interval
def time_handler() :
    global time_count
    time_count += 1

# define draw handler
def draw(canvas) :
    canvas.draw_text(format(time_count), [90, 115], 48, "White")    
    canvas.draw_text((str(stop_count) + "/" + str(zero_count)), [240, 25], 24, "Orange")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

# register event handlers
timer = simplegui.create_timer(100, time_handler)
frame.set_draw_handler(draw)
frame.add_button("Start", start_button, 100)
frame.add_button("Stop", stop_button, 100)
frame.add_button("Reset", reset_button, 100)

# start frame and timer
frame.start()

# Please remember to review the grading rubric
