from turtle import *
speed (30)
width(4)

# კვადრატი
color("brown")
begin_fill()      
forward(220)
left(90)

forward(220)
left(90)

forward(220)
left(90)

forward(220)
left(90)
end_fill()

# კარები
forward(80)
color("gray")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(220, 220)
pendown()

#სახურავი
color("saddle brown")
begin_fill()
right(140)
forward(160)
left(95)
forward(170)
end_fill()

# ფანჯარა 1
color("cyan")
begin_fill()
penup()
goto(20, 140)
pendown()
right(135)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()
right(90)
forward(30)
right(90)
color("white")
forward(60)
color("cyan")
left(90)
forward(30)
left(90)
forward(30)
left(90)
color("white")
forward(60)

# ფანჯარა 2
color("cyan")
begin_fill()
penup()
goto(140, 140)
pendown()
left(90)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()
right(90)
forward(30)
right(90)
color("white")
forward(60)
color("cyan")
left(90)
forward(30)
left(90)
forward(30)
left(90)
color("white")
forward(60)


exitonclick()