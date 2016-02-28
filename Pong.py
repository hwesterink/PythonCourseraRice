# Implementation of classic arcade game Pong

# IMPORT THE MODULE(S)
import simplegui
import random

# DEFINE AND INITIALIZE GLOBAL VARIABLES
# pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [0, 0]
ball_vel = [0, 0]

# DEFINE "HELPER" FUNCTIONS
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [300, 200]
    ball_vel[0] = random.randrange(120, 240) / 60
    ball_vel[1] = - random.randrange(60, 180) / 60
    if not direction :
        ball_vel[0] = -ball_vel[0]

# compute the corners of the two paddles
def compute_paddles() :
    global paddle_l_pos, paddle_r_pos  # these are the input variables
    global r_l_top, r_r_top, r_r_bottom, r_l_bottom  # output for the right paddle
    global l_l_top, l_r_top, l_r_bottom, l_l_bottom  # output for the left paddle
    
    l_l_top = [0, paddle_l_pos[1] - HALF_PAD_HEIGHT]
    l_r_top = [PAD_WIDTH, paddle_l_pos[1] - HALF_PAD_HEIGHT]
    l_r_bottom = [PAD_WIDTH, paddle_l_pos[1] + HALF_PAD_HEIGHT]
    l_l_bottom = [0, paddle_l_pos[1] + HALF_PAD_HEIGHT]
    
    r_l_top = [WIDTH - PAD_WIDTH, paddle_r_pos[1] - HALF_PAD_HEIGHT]
    r_r_top = [WIDTH, paddle_r_pos[1] - HALF_PAD_HEIGHT]
    r_r_bottom = [WIDTH, paddle_r_pos[1] + HALF_PAD_HEIGHT]
    r_l_bottom = [WIDTH - PAD_WIDTH, paddle_r_pos[1] + HALF_PAD_HEIGHT]    

# DEFINE EVENT HANDLER FUNCTIONS
def new_game():
    global paddle_l_pos, paddle_r_pos, paddle_l_vel, paddle_r_vel  # these are numbers
    global score_l, score_r  # these are ints

    paddle_l_pos = [4, 200]
    paddle_r_pos = [596, 200]
    paddle_l_vel = [0, 0]
    paddle_r_vel = [0, 0]
    score_l = 0
    score_r = 0
    
    spawn_ball(RIGHT)

def draw(canvas):
    global HEIGHT, HALF_PAD_HEIGHT
    global score_l, score_r, paddle_l_pos, paddle_r_pos, ball_pos, ball_vel
    global r_l_top, r_r_top, r_r_bottom, r_l_bottom  # corners for the right paddle
    global l_l_top, l_r_top, l_r_bottom, l_l_bottom  # corners for the left paddle
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 5, "White", "White")
    
    # compute the next position of the ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]    
    
    # let the ball bounce against the top and bottom of the canvas
    if ball_pos[1] <  BALL_RADIUS or ball_pos[1] > HEIGHT - BALL_RADIUS :
        ball_vel[1] = - ball_vel[1]
        ball_pos[1] += ball_vel[1]
    
    # draw paddles
    compute_paddles()
    canvas.draw_polygon([r_l_top, r_r_top, r_r_bottom, r_l_bottom], 1, "White", "White")
    canvas.draw_polygon([l_l_top, l_r_top, l_r_bottom, l_l_bottom], 1, "White", "White")

    # reflect the ball if it hits a paddle or
    # spawn a new ball when it reaches one of the gutters
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS :
        if ball_pos[1] >= (paddle_l_pos[1] - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle_l_pos[1] + HALF_PAD_HEIGHT) :
            ball_vel[0] = -ball_vel[0] * 1.1
        else :
            spawn_ball(RIGHT)
            score_r += 1
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS) :
        if ball_pos[1] >= (paddle_r_pos[1] - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle_r_pos[1] + HALF_PAD_HEIGHT) :
            ball_vel[0] = -ball_vel[0] * 1.1
        else :
            spawn_ball(LEFT)
            score_l += 1

    # update paddle's vertical position, keep paddle on the screen
    if (paddle_r_pos[1] + paddle_r_vel[1]) > HALF_PAD_HEIGHT and (paddle_r_pos[1] + paddle_r_vel[1]) < (HEIGHT - HALF_PAD_HEIGHT):
        paddle_r_pos[1] += paddle_r_vel[1]
    if (paddle_l_pos[1] + paddle_l_vel[1]) > HALF_PAD_HEIGHT and (paddle_l_pos[1] + paddle_l_vel[1]) < (HEIGHT - HALF_PAD_HEIGHT) :
        paddle_l_pos[1] += paddle_l_vel[1]
        
    # draw scores
    canvas.draw_text(str(score_l), ((WIDTH / 2 - 160), 60), 40, "Green")
    canvas.draw_text(str(score_r), ((WIDTH / 2 + 130), 60), 40, "Green")
    
def keydown(key):
    global paddle_l_vel, paddle_r_vel
    if key == simplegui.KEY_MAP["w"] :
        paddle_l_vel = [0, -5]
    elif key == simplegui.KEY_MAP["s"] :
        paddle_l_vel = [0, 5]
    if key == simplegui.KEY_MAP["up"] :
        paddle_r_vel = [0, -5]
    elif key == simplegui.KEY_MAP["down"] :
        paddle_r_vel = [0, 5]
   
def keyup(key):
    global paddle_l_vel, paddle_r_vel
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle_l_vel = [0, 0]
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"] :
        paddle_r_vel = [0, 0]

# CREATE FRAME
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

# REGISTER EVENT HANDLERS
frame.set_draw_handler(draw)
frame.add_button("Reset", new_game, 50)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# START FRAME AND TIMERS
new_game()
frame.start()
