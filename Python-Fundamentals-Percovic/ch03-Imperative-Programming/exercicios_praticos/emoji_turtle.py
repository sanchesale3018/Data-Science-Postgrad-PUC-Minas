# Desenhando uma face sorridente com a tartaruga.
import turtle

s = turtle.Screen()

t = turtle.Turtle()

# Desfina a espessura da linha da caneta como largura
t.pensize(3)

# definimos as coordenadas no Screen onde estará localizado o queixo da carinha 
x = -100
y = 100

# Move a caneta para o local definido nas coordenadas
t.goto(x, y)

# Desfaz o movimento anterior
t.undo()

# Levante a caneta não desenhando ao movimentar
t.penup()

# Repetindo o movimento porém com a caneta agora levantada
t.goto(x, y)

# Desça a caneta; a partir desse momento desenha ao movimentar
t.pendown()

# Desenha um círculo completo com o raio indicado (o centro fica à esquerda da tartaruga).
t.circle(100)

# Levanta a caneta e leva ela para a posição do olho esquerdo levando em consideração a posição do queixo
t.penup()
t.goto(x - 35, y + 120)
t.pendown()

# Cria um ponto preenchido na posição atual com o diâmetro e a cor definidos.
t.dot(25)

# Faz a mesma coisa com o olho direito
t.penup()
t.goto(x + 35, y + 120)
t.pendown()
t.dot(25)

t.penup()
t.goto(x - 60.62, y + 65)
t.pendown()



t.setheading(-60)
t.circle(70, 120)

# Mantem a janela Screen aberta

s.exitonclick()