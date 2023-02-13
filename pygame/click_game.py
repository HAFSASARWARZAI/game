character = Actor('character-1')
character .pos = 100,56

WIDTH = 500
HEIGHT = character .height + 20

def draw():
    screen.clear()
    character.draw()

def update():
    character.left = character.left + 2
    if character.left > WIDTH:
        character.right = 0

def on_mouse_down(pos):
    if character.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")


def on_mouse_down(pos):
    if character.collidepoint(pos):
        sounds.eep.play()
        character.image = 'character_hurt'

def on_mouse_down(pos):
    if character.collidepoint(pos):
        sounds.eep.play()
        character.image = 'alien_hurt'
        time.sleep(1)
        character.image = 'alien'






