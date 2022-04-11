import random
import pgzrun


"""GLOBAL VARIABLES"""  #In all caps makes it global
TITLE = "Alien Projectory"
THRUSTER = 2

TIME = 0
WIDTH = 850
HEIGHT = 400

PLANETS = ["planet1", "planet2"]



"""ACTORS"""

alien = Actor("aliennew")
alien.topright = 225, 55
alien.vy = 2.5
alien.health = 3
alien.collide = False

planet = Actor("planet1")
planet.topleft = WIDTH, random.randint(100, 300)
planet.lap = 1
planet.speed = 5
alien.life = True


health = Actor("health")
health.topleft = 5, 5

star = Actor("star")
star.topleft = 750,50


def draw():
    screen.blit('background', (0,0))
    alien.draw()
    planet.draw()
    health.draw()
    star.draw()

def update():
    # sounds.alienmusic.play()
    update_planet()
    update_alien()
    update_health()
    update_star()


def update_star():
    star.angle += 0.2


def update_alien():

    alien.y += alien.vy

    if alien.y > 350:
        alien.vy = -1
        alien.y = 350

    if alien.y < 50:
        alien.vy = 1
        alien.y = 50

def update_planet():

    if alien.life:
        planet.left -= planet.speed
        planet.angle -= 5

    if planet.left < 0:
        planet.right = WIDTH
        planet.y = random.randint(100, 300)
        planet.image = PLANETS[random.randint(0,1)]
        planet.lap += 1
        alien.collide = False

    if planet.lap % 5 == 0:
        planet.speed += 1
        planet.lap = 1

    if planet.colliderect(alien) and not alien.collide:
        set_alien_hurt()
        alien.health -= 1
        alien.collide = True

def update_health():
    if alien.health == 2:
        health.image = "health2"

    if alien.health == 1:
        health.image = "health3"

    if alien.health == 0:
        alien.life = False

def on_key_down():
    if keyboard.w or keyboard.up:
        alien.vy -= THRUSTER
        set_alien_thrust()

    if keyboard.s or keyboard.down:
        alien.vy += THRUSTER
        set_alien_thrust()

def set_alien_hurt():
    alien.image = 'alien_hurt'
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'aliennew'

def set_alien_thrust():
    alien.image = "alien_thrust"
    clock.schedule_unique(set_alien_normal, 0.2)

pgzrun.go()