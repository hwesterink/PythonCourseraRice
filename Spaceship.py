# program template for Spaceship

# IMPORT THE MODULE(S)
import simplegui
import math
import random

# DEFINE AND INITIALIZE GLOBAL VARIABLES FOR USER INTERFACE
WIDTH = 800
HEIGHT = 600
CANVAS_SIZE = (WIDTH, HEIGHT)
score = 0
lives = 3
time = 0

# CREATE A DICTIONARY WITH PARAMETERS FOR THIS GAME
PARMS = { "DIMS": 2, "ACCEL": 0.1, "FRICT": 0.99, "ANG_SPEED": 1.0,
        "VEL_RANGE": (-20,41), "ANG_RANGE": (-10,21), "MISS_VEL_BASE": 20,
        "MISS_POS_DISP": 40, "LIVES_POS": (20,30), "SCORE_POS": (WIDTH-90,30),
        "TEXT_SIZE": 20, "TEXT_COLOR": "orange" }

# DEFINE ImageInfo CLASS USED FOR ART ASSETS
class ImageInfo:
    def __init__(self, center, size, radius = 0,
                 lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

# ART ASSETS: IMAGES AND SOUNDS    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
# soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# DEFINE SHIP AND SPRITE CLASSES
# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self, canvas):
        global splash_image
        if self.thrust :
            canvas.draw_image(self.image, (self.image_center[0]+90, self.image_center[1]),
                           self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                           self.pos, self.image_size, self.angle)

    def update(self):
        update_pos(self.pos, self.vel)
        self.angle += self.angle_vel
        if self.thrust :
            update_vel(self.vel, self.angle)
        friction(self.vel)
        
    def turn(self, angle_vel):
        self.angle_vel = angle_vel / 60
        
    def accelerate(self, thrust):
        self.thrust = thrust
        if thrust :
            ship_thrust_sound.play()
        else :
            ship_thrust_sound.rewind()
    
    def shoot(self):
        global a_missile
        miss_pos = missile_pos(self.pos, self.angle)
        miss_vel = missile_vel(self.vel, self.angle)
        a_missile = Sprite(miss_pos, miss_vel, 0, 0, missile_image, missile_info, missile_sound)
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)
    
    def update(self):
        update_pos(self.pos, self.vel)
        self.angle += self.angle_vel
        

# DEFINE "HELPER" FUNCTIONS
# functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def update_pos(position, velocity):
    for i in range(PARMS["DIMS"]):
        position[i] += velocity[i]
        position[i] = position[i] % CANVAS_SIZE[i]
        
def update_vel(velocity, angle):
    vector = angle_to_vector(angle)
    for i in range(PARMS["DIMS"]):
        velocity[i] += vector[i] * PARMS["ACCEL"]

def friction(velocity):
    for i in range(PARMS["DIMS"]):
        velocity[i] *= PARMS["FRICT"]

def missile_pos(position, angle):
    miss_pos = [0, 0]
    vector = angle_to_vector(angle)
    for i in range(PARMS["DIMS"]):
        miss_pos[i] = position[i] + vector[i] * PARMS["MISS_POS_DISP"]
    return miss_pos
        
def missile_vel(velocity, angle):
    miss_vel = [0, 0]
    vector = angle_to_vector(angle)
    for i in range(PARMS["DIMS"]):
        miss_vel[i] = velocity[i] + vector[i] * PARMS["MISS_VEL_BASE"]
    return miss_vel
        
# DEFINE EVENT HANDLER FUNCTIONS           
# draw handler
def draw(canvas):
    global time
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(),
                      nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size,
                      (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size,
                      (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
    
    # put user output on the canvas
    canvas.draw_text("Lives remaining = " + str(lives), PARMS["LIVES_POS"], 
                     PARMS["TEXT_SIZE"], PARMS["TEXT_COLOR"])
    canvas.draw_text("Score = " + str(score), PARMS["SCORE_POS"], 
                     PARMS["TEXT_SIZE"], PARMS["TEXT_COLOR"])

    
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    vel = [random.randrange(PARMS["VEL_RANGE"][0], PARMS["VEL_RANGE"][1]) / 10.0,
           random.randrange(PARMS["VEL_RANGE"][0], PARMS["VEL_RANGE"][1]) / 10.0]
    ang_vel = random.randrange(PARMS["ANG_RANGE"][0], PARMS["ANG_RANGE"][1]) / 200.0
    a_rock = Sprite(pos, vel, 0, ang_vel, asteroid_image, asteroid_info)

# key handlers
def keydown_handler(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.turn(-PARMS["ANG_SPEED"])
    elif key == simplegui.KEY_MAP['right']:
        my_ship.turn(PARMS["ANG_SPEED"])
    elif key == simplegui.KEY_MAP['up']:
        my_ship.accelerate(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
        
def keyup_handler(key):
    if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['right']:
        my_ship.turn(0.0)
    elif key == simplegui.KEY_MAP['up']:
        my_ship.accelerate(False)
    

# CREATE FRAME
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# INITIALIZE SHIP AND SPRITES
my_ship = Ship([WIDTH / 4, HEIGHT / 2], [0, 0], 1, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.1, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3],
                   [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# REGISTER EVENT HANDLERS
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
timer = simplegui.create_timer(1000.0, rock_spawner)

# START TIMER(S) AND FRAME
timer.start()
frame.start()