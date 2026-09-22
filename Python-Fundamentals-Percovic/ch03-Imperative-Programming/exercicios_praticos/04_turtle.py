# importando o módulo turtle

import turtle

#instanciando um objeto Screen (Tela de desenho na qual iremos desenhar)

s = turtle.Screen()

# Iniciando a caneta inicando no centro da tela (0,0) que se volta inicialmente para a direita

t = turtle.Turtle()

# Movimenta a caneta para frente pela quantidade pix fornecida, no caso 100 px

t.forward(100)

# Vira a caneta para a esquerda de acordo com o ângulo fornecido. No caso, 90° para a esquerda.

t.left(90)

# Instanciando uma novo objeto Turtle e operando sobre ele

u = turtle.Turtle()
u.left(90)
u.forward(100)
t.forward(100)

# Gira a direção da caneta para a direita em 45 graus

u.right(45)

# Mantem a janela Screen aberta

s.exitonclick()