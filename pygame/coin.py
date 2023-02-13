from random import randint
Width = 400
Height = 400
score = 0
game_over = False
fox = Actor ("fox")
fox.pos = 100,  100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill(blue)
    fox.draw()
    coin.draw()
    screen.draw.text("Score:" + str(score), color:"black", topleft:(10, 10))

if game_over:
    screen.fill("pink")
    screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (Width - 20))
    coin.y = randint(20, (Height - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.rigth:
        fox.x = fox.x + 2
    elif beyboard.up:
        fox.y = fox.y -2
    elif keyboard.down:
        foc.y = fox.y + 2
    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()

clock.schedule(time_up, 7.0)
place_coin()



