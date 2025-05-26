from threading import *
import time
from tkinter import *
from PIL import ImageTk, Image

# Variables aligned with the first code's naming
custReady = 0
accessWRSeats = 1
available_seats = 4
barberReady = 0
come = 0

def main():
    global c
    root = Tk()
    root.title("Sleeping Barber Problem - Solution")
    root.geometry("1600x740")
    c = Canvas(root, bg='cyan', height=1080, width=1920)
    c.pack()
    img = ImageTk.PhotoImage(Image.open("images/bachkhoa.jpg"))
    c.create_image(0, 0, anchor=NW, image=img)
    c.create_rectangle(100, 100, 1400, 650, fill='white')
    c.create_rectangle(110, 110, 500, 640, fill='white')
    c.create_rectangle(510, 110, 1100, 640, fill='white')
    c.create_rectangle(1110, 110, 1390, 640, fill='white')
    fnt = ('Times', 28, 'bold', 'underline')
    c.create_text(500, 50, text="Sleeping Barber Problem - Solution", font=fnt, fill='BLACK')
    c.create_text(300, 150, text="MAIN ROOM", font=fnt, fill='black')
    c.create_text(800, 150, text="WAITING ROOM", font=fnt, fill='black')
    c.create_text(1250, 150, text="ENTRY DOOR", font=fnt, fill='black')
    fnt = ('Times', 30, 'bold')
    b1 = Button(c, text="ENTER", font=fnt, command=lambda: buttonClick())
    b1.place(x=640, y=670, width=200, height=70)
    root.mainloop()

def buttonClick():
    global come
    come = 1

def signal1(s):
    global custReady
    custReady = s
    custReady = custReady + 1

def wait1(s):
    global custReady, c, img19
    cnt = 0
    custReady = s
    if custReady == 0:
        print("Barber is Sleeping")
        img1 = ImageTk.PhotoImage(Image.open("images/sleepingbarber.png"))
        c.create_image(170, 230, anchor=NW, image=img1)
        img2 = ImageTk.PhotoImage(Image.open("images/chairs.png"))
        c.create_image(620, 250, anchor=NW, image=img2)
    while custReady <= 0:
        cnt = 1
    if cnt == 1:
        cnt = 0
        print("Barber Wake Up")
        img3 = ImageTk.PhotoImage(Image.open("images/wakeupbarber.png"))
        c.create_image(170, 230, anchor=NW, image=img3)
        time.sleep(1)
        img19 = ImageTk.PhotoImage(Image.open("images/readybarber.png"))
        c.create_image(170, 230, anchor=NW, image=img19)
    custReady = custReady - 1

def signal2(s):
    global accessWRSeats
    accessWRSeats = s
    accessWRSeats = accessWRSeats + 1

def wait2(s):
    global accessWRSeats
    accessWRSeats = s
    while accessWRSeats <= 0:
        pass
    accessWRSeats = accessWRSeats - 1

class Barber(Thread):
    def run(self):
        global custReady, accessWRSeats, available_seats, c
        while True:
            wait1(custReady)
            wait2(accessWRSeats)
            time.sleep(0.2)
            print("Customer Enters into Main Room")
            if custReady == 1:
                img4 = ImageTk.PhotoImage(Image.open("images/1person.png"))
                c.create_image(620, 250, anchor=NW, image=img4)
            elif custReady == 2:
                img5 = ImageTk.PhotoImage(Image.open("images/2person.png"))
                c.create_image(620, 250, anchor=NW, image=img5)
            elif custReady == 3:
                img6 = ImageTk.PhotoImage(Image.open("images/3person.png"))
                c.create_image(620, 250, anchor=NW, image=img6)
            elif custReady == 4:
                img7 = ImageTk.PhotoImage(Image.open("images/4person.png"))
                c.create_image(620, 250, anchor=NW, image=img7)
            else:
                img8 = ImageTk.PhotoImage(Image.open("images/chairs.png"))
                c.create_image(620, 250, anchor=NW, image=img8)
            time.sleep(1)
            available_seats += 1
            print("started cutting")
            img9 = ImageTk.PhotoImage(Image.open("images/workingbarber.png"))
            c.create_image(170, 230, anchor=NW, image=img9)
            time.sleep(10)
            print("Cutting complete")
            img10 = ImageTk.PhotoImage(Image.open("images/readybarber.png"))
            c.create_image(170, 230, anchor=NW, image=img10)
            time.sleep(1)
            signal2(accessWRSeats)

class Customer(Thread):
    def run(self):
        global custReady, accessWRSeats, available_seats, come, c
        while True:
            if come == 1:
                come = 0
                img16 = ImageTk.PhotoImage(Image.open("images/entering.png"))
                i16 = c.create_image(1120, 250, anchor=NW, image=img16)
                time.sleep(1)
                c.delete(i16)
                if available_seats > 0:
                    print("Customer Enters into Waiting Room")
                    available_seats -= 1
                    signal1(custReady)
                    if custReady == 1:
                        img11 = ImageTk.PhotoImage(Image.open("images/1person.png"))
                        c.create_image(620, 250, anchor=NW, image=img11)
                    elif custReady == 2:
                        img12 = ImageTk.PhotoImage(Image.open("images/2person.png"))
                        c.create_image(620, 250, anchor=NW, image=img12)
                    elif custReady == 3:
                        img13 = ImageTk.PhotoImage(Image.open("images/3person.png"))
                        c.create_image(620, 250, anchor=NW, image=img13)
                    elif custReady == 4:
                        img14 = ImageTk.PhotoImage(Image.open("images/4person.png"))
                        c.create_image(620, 250, anchor=NW, image=img14)
                    else:
                        img15 = ImageTk.PhotoImage(Image.open("images/chairs.png"))
                        c.create_image(620, 250, anchor=NW, image=img15)
                    time.sleep(1)
                elif available_seats == 0:
                    img17 = ImageTk.PhotoImage(Image.open("images/nospace.png"))
                    i17 = c.create_image(1120, 250, anchor=NW, image=img17)
                    time.sleep(0.5)
                    c.delete(i17)
                    img18 = ImageTk.PhotoImage(Image.open("images/leaving.png"))
                    i18 = c.create_image(1120, 250, anchor=NW, image=img18)
                    time.sleep(1)
                    c.delete(i18)
                    print("Customer Enters But There is No Space, Customer Leaves")

b = Barber()
cus = Customer()

b.start()
cus.start()

main()