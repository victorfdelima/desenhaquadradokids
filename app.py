import turtle

def desenhaQuadrado(t, tam):
    """Faca a tartaruga t desenhar um quadrado de lado tam."""

    for i in ['red','purple','hotpink','blue']:
        t.forward(tam)
        t.color(i)
        t.left(90)


wn = turtle.Screen()              # Inicializa a janela e seus atributos
wn.bgcolor("lightgreen")

alex = turtle.Turtle()            # cria alex
desenhaQuadrado(alex, 50)         # Chama a função para desenhar um quadrado

alex.penup()
alex.goto(100,100)
alex.pendown()

desenhaQuadrado(alex,75)          # Desenha outro quadrado

tess = turtle.Turtle()            # cria tess e seus atributos
tess.pensize(3)

for i in range(15):
    desenhaQuadrado(tess, tamanho)
    tamanho = tamanho + 10       # aumenta o tamanho para a próxima vez
    tess.forward(10)             # move tess um pouco à frente
    tess.right(18)               # e dá uma virada nela
wn.exitonclick()
