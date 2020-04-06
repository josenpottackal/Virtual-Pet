
# File Name: Virtual Pet
# Purpose: Models the action of a virtual pet
# Date: 2020-02-20
# Last modified: 2020-02-20
# Author: Josen Pottackal
# Copy right no copyright
# Version: 1.0

import random
import tkinter
from PIL import Image, ImageTk, ImageSequence

avatarName = "zog"
happiness = 1
hunger = 1
healthy = True
age = 1


class App:
    def __init__(self, parent, gifFile):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=400, height=400)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(gifFile))]
        self.image = self.canvas.create_image(200, 200, image=self.sequence[0])
        self.animate(1)

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter + 1) % len(self.sequence)))


def printGIF():
    root = tkinter.Tk()
    App(root, gifFile)
    root.mainloop()


while True:
    randomInt = random.randint(1, 5)
    randomInt = int(randomInt)

    randomInt2 = random.randint(1, 5)
    randomInt2 = int(randomInt2)

    if 0 <= happiness <= 4:
        print(avatarName + "'s happiness is LOW")
    elif 5 <= happiness <= 8:
        print(avatarName + "'s happiness is MEDIUM")
    else:
        print(avatarName + "'s happiness is HIGH")

    if 0 <= hunger <= 4:
        print(avatarName + "'s hunger is LOW")
    elif 5 <= hunger <= 8:
        print(avatarName + "'s hunger is MEDIUM")
    else:
        print(avatarName + "'s hunger is HIGH")

    if healthy:
        print(avatarName + " is healthy")
    elif not healthy:
        print(avatarName + " is sick")

    if healthy and randomInt == 1 and happiness > 0:  # lose happiness with p=0.5
        print(avatarName + "'s happiness decreased")
        happiness = happiness - 1

    if healthy and randomInt2 == 1 and hunger > 0:  # lose hunger with p=0.5
        print(avatarName + "'s fullness decreased")
        hunger = hunger - 1

    if not healthy and happiness > 0:
        print(avatarName + " is sick")
        print(avatarName + "'s happiness decreased")
        happiness = happiness - 1

    if not healthy and hunger > 0:
        print(avatarName + " is sick")
        print(avatarName + "'s fullness decreased")
        hunger = hunger - 1

    print("\n" + "Choose from the following options:")
    print("0: Do nothing")
    print("1: Give " + avatarName + " medicine")
    print("2: Play with " + avatarName)
    print("3: Feed " + avatarName)
    choice = input("Enter a number from 0-3: \n")
    choice = int(choice)

    if choice == 0:
        if healthy:
            gifFile = "Idle.gif"
            printGIF()
        elif not healthy:
            gifFile = "Sick.gif"
            printGIF()
        break
    elif choice == 1:  
        gifFile = "Pills.gif"
        printGIF()
        healthy = True
        if not healthy:
            print(avatarName + " is sick")
    elif choice == 2:
        if healthy:
            print("You are playing with " + avatarName + ". please wait")
            gifFile = "Play.gif"
            printGIF()
            if happiness < 13:
                happiness = happiness + 1
                print(avatarName + "'s happiness  increased\n")
        elif not healthy:
            print(avatarName + " is sick")
            gifFile = "Sick.gif"
            printGIF()

    elif choice == 3:
        if healthy:
            if hunger == 13:
                gifFile = "Idle.gif"
                printGIF()
                print("You cant feed " + avatarName + ". its full\n")
            else:
                gifFile = "Eat.gif"
                printGIF()
                hunger = hunger + 1
                print("You fed " + avatarName)
        elif not healthy:
            print(avatarName + " is sick")
            gifFile = "Sick.gif"
            printGIF()
    else:
        print("Invalid response, please re-enter\n")
