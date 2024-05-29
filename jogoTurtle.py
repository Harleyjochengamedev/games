import turtle

janela = turtle.Screen()
janela.tracer(0)
janela.setup(0.5,0.75)
janela.bgcolor(0.2,0.2,0.2)
janela.title("Joguinho")

LEFT = -janela.window_width() / 2
RIGHT = janela.window_width() / 2
TOP = janela.window_height() / 2
BOTTOM = -janela.window_height() / 2
FLOOR_LEVEL = 0.9 * BOTTOM
GUTTER = 0.025 * janela.window_width()
LASER_LENGTH = 10
LASER_SPEED = 20


canhao = turtle.Turtle()
canhao.penup()
canhao.color(1,1,1)
canhao.shape('square')
canhao.setposition(0, FLOOR_LEVEL)

canhao.turtlesize(1, 3)  # Base
canhao.stamp()
canhao.sety(FLOOR_LEVEL + 10)
canhao.turtlesize(1, 1.5)  # Next tier
canhao.stamp()
canhao.sety(FLOOR_LEVEL + 20)
canhao.turtlesize(0.8, 0.3)  # Tip of cannon
canhao.stamp()
canhao.sety(FLOOR_LEVEL)

lasers = []
CANHAO_PASSO = 10

def desenhar_cachao():
    canhao.clear()
    canhao.turtlesize(1, 3)  # Base
    canhao.stamp()
    canhao.sety(FLOOR_LEVEL + 10)
    canhao.turtlesize(1, 1.5)  # Next tier
    canhao.stamp()
    canhao.sety(FLOOR_LEVEL + 20)
    canhao.turtlesize(0.8, 0.3)  # Tip of cannon
    canhao.stamp()
    canhao.sety(FLOOR_LEVEL)
    janela.update()

def mover_esquerda():
    novo_x = canhao.xcor() - CANHAO_PASSO
    if novo_x>= LEFT + GUTTER:
        canhao.setx(novo_x)
        desenhar_cachao()

def mover_direita():
    novo_x = canhao.xcor() + CANHAO_PASSO
    if novo_x<= RIGHT + GUTTER:
        canhao.setx(novo_x)
        desenhar_cachao()

def criar_lasers():
    laser = turtle.Turtle()
    laser.penup()
    laser.color(1, 0, 0)
    laser.hideturtle()
    laser.setposition(canhao.xcor(), canhao.ycor())
    laser.setheading(90)
    laser.forward(20)
    laser.pendown()
    laser.pensize(5)

    lasers.append(laser)
    

def move_laser(laser):
    laser.clear()
    laser.forward(LASER_SPEED)
    laser.forward(LASER_LENGTH)
    laser.forward(-LASER_LENGTH)

janela.onkeypress(mover_esquerda,'Left')
janela.onkeypress(mover_direita,'Right')
janela.onkeypress(criar_lasers,'w')
janela.onkeypress(turtle.bye,'q')
janela.listen()

desenhar_cachao()

while True:
    for laser in lasers.copy():
        move_laser(laser)
        if laser.ycor() > TOP:
            laser.clear()
            laser.hideturtle()
            lasers.remove(laser)
            turtle.turtles().remove(laser)
    janela.update()

turtle.done()