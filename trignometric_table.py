import pygame as py
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
animation_timer = py.time.Clock()
input1 = "function"
input2 = "degree"
input3 = "Answer"
Trig_list = [("Sin", 50,80,100,40,red,green),
            ("Cos", 50,160,100,40,red,green),
            ("Tan", 50,240,100,40,red,green),
            ("Cosec",50,320,100,40,red,green),
            ("Sec",50,400,100,40,red,green),
            ("Cot",50,480,100,40,red,green),
            ("0\xb0",250,120,100,40,red,green),
            ("30\xb0",250,200,100,40,red,green),
            ("45\xb0",250,280,100,40,red,green),
            ("60\xb0",250,360,100,40,red,green),
            ("90\xb0",250,440,100,40,red,green)]

py.init()
screen = py.display.set_mode((800,600))
py.display.set_caption("Trignometric values")
running = True

def txt_object(text,x,y,l,w,ic,ac=blue):
    textSurface = py.font.Font("freesansbold.ttf",20).render(text, True, (0,0,0))
    tesxtRect = textSurface.get_rect()
    mouse = py.mouse.get_pos()
    click = py.mouse.get_pressed()
    if x+l > mouse[0] > x and y+w > mouse[1] > y:
        py.draw.rect(screen, ac, (x, y, l, w))
        if click[0] == 1:
            global input1,input2
            if text == "Sin" or text == "Cos" or text == "Tan" or text == "Cosec" or text == "Sec" or text == "Cot" :
                input1 = text
                print(input1)
            else:
                input2 = text

    else:
        py.draw.rect(screen, ic, (x, y, l, w))
    tesxtRect.center = ((x+l/2), (y+w/2))
    screen.blit(textSurface, tesxtRect)

while running:
    for e in py.event.get():
        if e.type == py.QUIT:
            running = False

    screen.fill((255,255,255))

    for x in Trig_list:
        txt_object(*(x))

    txt_object(input1, 450, 200, 120, 40, blue)
    txt_object(input2, 450, 360, 120, 40, blue)


    if input1 == "Sin" and input2 =="0\xb0":
        input3 = "0"
    elif input1 == "Sin" and input2 =="30\xb0":
        input3 = "1/2"
    elif input1 == "Sin" and input2 =="45\xb0":
        input3 = "1/"+u"\u221A"+"2"
    elif input1 == "Sin" and input2 =="60\xb0":
        input3 = u"\u221A"+"3/2"
    elif input1 == "Sin" and input2 =="90\xb0":
        input3 = "1"
    elif input1 == "Cos" and input2 =="90\xb0":
        input3 = "0"
    elif input1 == "Cos" and input2 =="60\xb0":
        input3 = "1/2"
    elif input1 == "Cos" and input2 =="45\xb0":
        input3 = "1/"+u"\u221A"+"2"
    elif input1 == "Cos" and input2 =="30\xb0":
        input3 = u"\u221A"+"3/2"
    elif input1 == "Cos" and input2 =="0\xb0":
        input3 = "1"
    elif input1 == "Tan" and input2 =="90\xb0":
        input3 = "Not Defined"
    elif input1 == "Tan" and input2 =="60\xb0":
        input3 = u"\u221A" + "3"
    elif input1 == "Tan" and input2 =="45\xb0":
        input3 = "1"
    elif input1 == "Tan" and input2 =="30\xb0":
        input3 = "1/"+u"\u221A"+"3"
    elif input1 == "Tan" and input2 =="0\xb0":
        input3 = "0"
    elif input1 == "Cot" and input2 =="90\xb0":
        input3 = "1"
    elif input1 == "Cot" and input2 =="60\xb0":
        input3 = "1/"+u"\u221A"+"3"
    elif input1 == "Cot" and input2 =="45\xb0":
        input3 = "1"
    elif input1 == "Cot" and input2 =="30\xb0":
        input3 = u"\u221A" + "3"
    elif input1 == "Cot" and input2 =="0\xb0":
        input3 = "Not Defined"
    elif input1 == "Cosec" and input2 =="90\xb0":
        input3 = "1"
    elif input1 == "Cosec" and input2 =="60\xb0":
        input3 = "2/"+u"\u221A" + "3"
    elif input1 == "Cosec" and input2 =="45\xb0":
        input3 = u"\u221A"+"2"
    elif input1 == "Cosec" and input2 =="30\xb0":
        input3 = "2"
    elif input1 == "Cosec" and input2 =="0\xb0":
        input3 = "Not Defined"
    elif input1 == "Sec" and input2 =="90\xb0":
        input3 = "Not Defined"
    elif input1 == "Sec" and input2 =="60\xb0":
        input3 = "2"
    elif input1 == "Sec" and input2 =="45\xb0":
        input3 = u"\u221A"+"2"
    elif input1 == "Sec" and input2 =="30\xb0":
        input3 = "2/"+u"\u221A" + "3"
    elif input1 == "Sec" and input2 =="0\xb0":
        input3 = "1"

    else:
        input3 = "answer" 
    txt_object(input3, 650, 280, 120, 40, blue)

    animation_timer.tick(60)
    py.display.update()
py.quit()