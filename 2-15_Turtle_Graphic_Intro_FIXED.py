import turtle
turtle.speed(1)
turtle.penup()
turtle.setup(1920,1080)
#860,540
#фигура 1
turtle.goto(-830,440)
turtle.begin_fill()
turtle.pendown()
turtle.goto(-791.11,478.89)
turtle.goto(-752.22,440.00)
turtle.goto(-713.33,478.89)
turtle.goto(-674.44,440.00)
turtle.goto(-713.33,401.11)
turtle.goto(-752.22,440.00)
turtle.goto(-791.11,401.11)
turtle.goto(-830,440)
turtle.end_fill()
turtle.penup()
#фигура 2
turtle.goto(-624.33,401.11)
turtle.pendown()
turtle.goto(-574.33,478.89)
turtle.goto(-524.33,401.11)
turtle.goto(-624.33,401.11)
turtle.begin_fill()
turtle.goto(-574.33,440.00)
turtle.goto(-524.33,401.11)
turtle.goto(-624.33,401.11)
turtle.end_fill()
turtle.penup()
#Фигура 3 , ради ровных квадратов размеры отличаются.
turtle.goto(-474.33,478.89) # верх лево
turtle.pendown()
turtle.goto(-424.33,478.89) # верх центр
turtle.goto(-424.33,378.89) # низ центр
turtle.goto(-374.33,378.89) # низ право
turtle.goto(-374.33,428.89) # центр право
turtle.goto(-474.33,428.89) # центр лево
turtle.goto(-474.33,478.89)
turtle.goto(-374.33,378.89)
turtle.penup()
turtle.goto(-474.33,428.89)
turtle.pendown()
turtle.goto(-424.33,378.89)
turtle.penup()
turtle.goto(-424.33,478.89)
turtle.pendown()
turtle.goto(-374.33,428.89)
turtle.penup()
# 4 фигура
turtle.goto(-830,310) # Основание 1 круга
turtle.pendown()
turtle.circle(20)
turtle.penup()
turtle.goto(-780,310) # Основание 2 круга
turtle.pendown()
turtle.circle(20)
turtle.penup()
turtle.goto(-730,310) # Основание 3 круга
turtle.pendown()
turtle.circle(20)
turtle.penup()
turtle.goto(-805,290) # Основание 4 круга
turtle.pendown()
turtle.circle(20)
turtle.penup()
turtle.goto(-755,290)
turtle.pendown()
turtle.circle(20)
turtle.penup()
# 5 фигура
turtle.goto(-655,290) # Низ Лево
turtle.dot()
turtle.pendown()
turtle.goto(-655,350) # Верх лево
turtle.dot()
turtle.goto(-625,320) # Центр
turtle.dot()
turtle.goto(-595,290) # Низ право
turtle.dot()
turtle.goto(-595,350) # Верх право
turtle.dot()
turtle.goto(-655,290)
turtle.forward(8)
turtle.penup()
turtle.forward(7.5)
turtle.pendown()
turtle.forward(10.5)
turtle.penup()
turtle.forward(7.5)
turtle.pendown()
turtle.forward(10.5)
turtle.penup()
turtle.forward(7.5)
turtle.pendown()
turtle.forward(8)
turtle.goto(-655,350)
turtle.forward(8)
turtle.penup()
turtle.forward(7.5)
turtle.pendown()
turtle.forward(10.5)
turtle.penup()
turtle.forward(7.5)
turtle.pendown()
turtle.forward(10.5)
turtle.penup()
turtle.forward(7.5)
turtle.pendown()
turtle.forward(8)
turtle.penup()
# 6 фигура
turtle.goto(0,-20)
turtle.pendown()
turtle.circle(20)
turtle.goto(0,200) # Верх
turtle.goto(0,-200) # Низ
turtle.goto(0,0)
turtle.goto(200,0) # Право
turtle.goto(-200,0) # Лево 
turtle.penup()
turtle.goto(-235,-5)
turtle.write('Запад')
turtle.goto(-15,205)
turtle.write('Север')
turtle.goto(210,-5)
turtle.write('Восток')
turtle.goto(-6,-218)
turtle.write('Юг')
turtle.hideturtle()
turtle.done()