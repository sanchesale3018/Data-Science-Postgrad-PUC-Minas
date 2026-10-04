import turtle
import math


def poligono(quantidade_lados, medida_lado):

    medida_lado = 37.8*medida_lado
    s = turtle.Screen()
    q = turtle.Turtle()
    q.dot(3)
    q.penup()
    q.goto(-medida_lado/2, -medida_lado/2)
    q.pendown()

    for n in range(quantidade_lados):
       
        q.forward(medida_lado)
        q.left(180 - (((quantidade_lados-2)*180)/quantidade_lados))
    q.circle(medida_lado/(2*math.sin(180/quantidade_lados)))
    s.exitonclick()

quantidade_lados = int(input("Qual a quantidade de lados do polígono regular deseja gerar? "))
medida_lado = int(input("Qual a medida do lado? "))

poligono(quantidade_lados,medida_lado)




    

