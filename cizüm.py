import turtle 
import random 

def kare(a):
    for  i  in  range(4):
       ok.forward(a)
       ok.left(90)
       ok.color(random.choice(renk))
       
       
renk = [ 'red',  'green',  'blue',  'yellow', 'purple', 'brown' ]
ok = turtle.Turtle()
ok.speed(0)


kenar = 2
for  i  in  range(10000):
   
   kare(kenar)
   kenar = kenar + 2
   ok.right(120)
