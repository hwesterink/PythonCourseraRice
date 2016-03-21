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
started = False
highscore = 0

# CREATE A DICTIONARY WITH PARAMETERS FOR THIS GAME
# The dictionary PARMS contains the following parameters:
#	- DIMS =				2 for the two dimensions of the positions and velocities in the game.
#	- ACCEL =				Acceleration factor for the spaceship used when the push button is
#							pushed.
#	- FRICT =				Friction factor for the spaceship that slows down the spaceship.
#	- ANG_SPEED =			Angular velocity factor for spaceship used when the right or left button
#							are pushed.
#	- VEL_RANGE =			Range used by random.randrange for the velocity of a rock at creation.
#	- ANG_RANGE =			Range used by random.randrange for the angular velocity of a rock at
#							creation.
#	- MISS_VEL_BASE =		Velocity factor for a missile at creation.
#	- MISS_POS_DISP =		Forward displacement of the missile creation position compared to the
#							center of the spaceship.
#	- LIVES_POS =			Starting position of the lives remaining text.
#	- LIVES_POS2 =			Starting position of the ship representing the remaining lives.
#	- RED_SIZE =			Reduced size of the ships image to represent remaining lives.
#	- SCORE_POS =			Starting position of the score text.
#   - SCORE_POS2 =			Starting position of the score number.
#	- TEXT_SIZE =			Size of the texts in pixels.
#	- TEXT_COLOR =			Color of the text.
#	- MISSILE_LIFE =		Lifetime of a missile.
#	- MIN_DIST =			Minimum distance from the spaceship to spawn a rock.
#	- EXPL_ANIM =			Boolean that tells whether an explosion should be animated.
#	- ROCK_ANIM =			Boolean that tells whether an asteroid should be animated.
#	- SOUND_CHOICE =		Choice of the background soundtrack:
#								1: Standard soundtrack as used in the template.
#								2: Alternate soundtrack.
#	- HIGH_SCORE_POS =		Start position for the highest score text.
#	- HIGH_SCORE_COLOR =	Color of the highest score text.
PARMS = { "DIMS": 2, "ACCEL": 0.1, "FRICT": 0.99, "ANG_SPEED": 1.0,
        "VEL_RANGE": [(-10,21), (-20,41), (-40,81)], "ANG_RANGE": (-10,21),
        "MISS_VEL_BASE": 5, "MISS_POS_DISP": 40, "LIVES_POS": (20,30),
        "LIVES_POS2": (180,25), "RED_SIZE": (30,30), "SCORE_POS": (WIDTH-80,30),
        "SCORE_POS2": (WIDTH-80,50), "TEXT_SIZE": 20, "TEXT_COLOR": "orange",
        "MISSILE_LIFE": 120, "MIN_DIST": 175, "EXPL_ANIM": True, "ROCK_ANIM": True,
        "SOUND_CHOICE": 2, "HIGH_SCORE_POS": (325,400), "HIGH_SCORE_COLOR": "yellow"}

# DEFINE ImageInfo CLASS USED FOR ART ASSETS
class ImageInfo:
    def __init__(self, center, size, radius = 0, num_pictures = 0,
                 lifespan = None, animated = False, slowdown_anim = 1):
        self.center = center
        self.size = size
        self.radius = radius
        self.num_pictures = num_pictures
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated
        self.slowdown_anim = slowdown_anim

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_num_pictures(self):
        return self.num_pictures
    
    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
    
    def get_slowdown_anim(self):
        return self.slowdown_anim

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
ship_info = ImageInfo([45, 45], [90, 90], 30)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, lifespan = PARMS["MISSILE_LIFE"])
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 30)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# animated asteriod - asteroid1.opengameart.warspawn.png
aster_anim_info = ImageInfo([64, 64], [128, 128], 30, 60, animated = True, slowdown_anim = 2)
aster_anim_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid1.opengameart.warspawn.png")

# sound assets purchased from sounddogs.com, please do not redistribute
if PARMS["SOUND_CHOICE"] == 1 :
    soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
if PARMS["SOUND_CHOICE"] == 2 :
    soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

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
        
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def get_image(self):
        return self.image
    
    def get_image_center(self):
        return self.image_center
    
    def get_image_size(self):
        return self.image_size
    
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
        global missile_group
        miss_pos = missile_pos(self.pos, self.angle)
        miss_vel = missile_vel(self.vel, self.angle)
        missile_group.add(Sprite(miss_pos, miss_vel, 0, 0,
                                 missile_image, missile_info, missile_sound))
    
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
        self.num_pictures = info.get_num_pictures()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.slowdown_anim = info.get_slowdown_anim()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
            
    def draw(self, canvas):
        if self.animated:
            index = (self.age // self.slowdown_anim) % self.num_pictures
            animation_center = [self.image_center[0] + index *
                       self.image_size[0], self.image_center[1]]
            canvas.draw_image(self.image, animation_center, self.image_size,
                       self.pos, (self.image_size[0]/2.0,self.image_size[1]/2.0)) 
        else:
            canvas.draw_image(self.image, self.image_center,
                   self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        update_pos(self.pos, self.vel)
        self.angle += self.angle_vel
        self.age += 1
        if self.age < self.lifespan :
            return False
        else:
            return True
        
    def collide(self, other_object):
        if ( dist(self.pos, other_object.get_position()) <=
             self.radius + other_object.get_radius() ) :
            return True
        else:
            return False

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

def process_sprite_group(sprite_group, canvas):
    for spr in set(sprite_group):
        spr.draw(canvas)
        if spr.update():
            sprite_group.remove(spr) 

def group_collide(sprite_group, other_object):
    global explosion_group
    collosion = False
    for spr in set(sprite_group):
        if spr.collide(other_object):
            sprite_group.remove(spr)
            collosion = True
            if PARMS["EXPL_ANIM"]:
                pos = spr.get_position()
                explosion_group.add(Sprite(pos, (0, 0), 0, 0,
                          explosion_image, explosion_info, explosion_sound))
    return collosion

def group_group_collide(sprite1_group, sprite2_group):
    count = 0
    for spr in set(sprite1_group):
        if group_collide(sprite2_group, spr):
            sprite1_group.discard(spr)
            count +=1
    return count


# DEFINE EVENT HANDLER FUNCTIONS           
# draw handler
def draw(canvas):
    global time, lives, score, started, my_ship, rock_group
    global missile_group, explosion_group, highscore
        
    # animate background
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

    # draw and update ship and sprite groups
    if group_collide(rock_group, my_ship):
        lives -= 1
    score += group_group_collide(missile_group, rock_group) * 10
    if lives == 0:
        started = False
        if score > highscore:
            highscore = score
        rock_group = set([])
        missile_group = set([])
        if PARMS["EXPL_ANIM"]:
            explosion_group = set([])
    my_ship.draw(canvas)
    my_ship.update()
            
    # draw and update sprites
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    if PARMS["EXPL_ANIM"]:
        process_sprite_group(explosion_group, canvas)
    
    # put user output on the canvas
    if lives > 0:
        canvas.draw_text("Lives remaining = ", PARMS["LIVES_POS"], PARMS["TEXT_SIZE"], PARMS["TEXT_COLOR"])
        for i in range(lives):
            lives_pos = [(PARMS["LIVES_POS2"][0]+PARMS["RED_SIZE"][0]*i),PARMS["LIVES_POS2"][1]]
            canvas.draw_image(my_ship.get_image(), my_ship.get_image_center(),
                              my_ship.get_image_size(), lives_pos, PARMS["RED_SIZE"])
    else:
        canvas.draw_text("No more lives remaining", PARMS["LIVES_POS"],
                         PARMS["TEXT_SIZE"], PARMS["TEXT_COLOR"])
    canvas.draw_text("Score", PARMS["SCORE_POS"], PARMS["TEXT_SIZE"], PARMS["TEXT_COLOR"])
    canvas.draw_text(str(score), PARMS["SCORE_POS2"], PARMS["TEXT_SIZE"], PARMS["TEXT_COLOR"])
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
        if highscore != 0:
            canvas.draw_text("Highest score = " + str(highscore),
                             PARMS["HIGH_SCORE_POS"], PARMS["TEXT_SIZE"], PARMS["HIGH_SCORE_COLOR"])
        
    
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group, my_ship, started
    if len(rock_group) < 12 and started:
        if score > 200:   i = 2
        elif score > 100: i = 1
        else:             i = 0
        pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
        vel = [random.randrange(PARMS["VEL_RANGE"][i][0], PARMS["VEL_RANGE"][i][1]) / 10.0,
               random.randrange(PARMS["VEL_RANGE"][i][0], PARMS["VEL_RANGE"][i][1]) / 10.0]
        ang_vel = random.randrange(PARMS["ANG_RANGE"][0], PARMS["ANG_RANGE"][1]) / 200.0
        pos_ship = my_ship.get_position()
        distance = dist(pos_ship, pos)
        if distance > PARMS["MIN_DIST"]:
            if PARMS["ROCK_ANIM"]:
                rock_group.add(Sprite(pos, vel, 0, 0,
                          aster_anim_image, aster_anim_info))
            else:
                rock_group.add(Sprite(pos, vel, 0, ang_vel, asteroid_image, asteroid_info))

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
    
# mouseclick handler that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        lives = 3
        score = 0
        soundtrack.rewind()
        soundtrack.play()

        
# CREATE FRAME
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# INITIALIZE SHIP AND SPRITES
my_ship = Ship([WIDTH / 4, HEIGHT / 2], [0, 0], 1, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])

# REGISTER EVENT HANDLERS
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.set_mouseclick_handler(click)
timer = simplegui.create_timer(1000.0, rock_spawner)

# START TIMER(S) AND FRAME
timer.start()
frame.start()