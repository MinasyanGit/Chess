from tkinter import *


# Main Window

window = Tk()
window.title("Chess")
a = Canvas(window, height=1000, width=1500)


# Assets ------------------------------------–––––––--

# White images
whiteKing = PhotoImage(file='assets/white/whiteKing.png')
whiteQueen = PhotoImage(file='assets/white/whiteQueen.png')
whiteOfficer = PhotoImage(file='assets/white/whiteOfficer.png')
whiteHorse = PhotoImage(file='assets/white/whiteHorse.png')
whiteSheep = PhotoImage(file="assets/white/whiteSheep.png")
whiteSoldier = PhotoImage(file="assets/white/whiteSoldier.png")


# Black images
blackKing = PhotoImage(file='assets/black/blackKing.png')
blackQueen = PhotoImage(file='assets/black/blackQueen.png')
blackSheep = PhotoImage(file='assets/black/blackSheep.png')
blackOfficer = PhotoImage(file='assets/black/blackOfficer.png')
blackHorse = PhotoImage(file='assets/black/blackHorse.png')
blackSoldier = PhotoImage(file='assets/black/blackSoldier.png')


a.pack()


# code


# Board
recSize = 80
multY, y = 9, recSize
if recSize > 80:
    y, multY = 10, 8

x1, y1 = recSize * 3, y
x2, y2 = x1 + recSize, y1 + recSize
numbersX, numbersY = x1 - recSize / 4, y1 + recSize / 2
alphabetX, alphabetY = x1 + recSize / 2, recSize * multY + recSize / 4 + 1

numbers, alphabet = ["8", "7", "6", "5", "4", "3", "2", "1"], ["A", "B", "C", "D", "E", "F", "G", "H"]
cords = []
fonts = recSize // 4
fonts = "Times", fonts, "bold"

for i in range(8):
    a.create_text(numbersX, numbersY, text=numbers[i], font=fonts)
    a.create_text(alphabetX, alphabetY, text=alphabet[i], font=fonts)
    alphabetX += recSize
    numbersY += recSize
    for j in range(8):
        cords.append(alphabet[i] + numbers[j])
        if (i + j) % 2 != 0:
            a.create_rectangle(x1, y1, x2, y2, fill="#2A6731")
        else:
            a.create_rectangle(x1, y1, x2, y2, fill="white")
        x1 += recSize
        x2 += recSize
    x1 -= recSize * 8
    x2 -= recSize * 8
    y1 += recSize
    y2 += recSize


# White Assets ----------------------------------------------------------------------------------------
whiteSheep1 = a.create_image(recSize * 3 + recSize * 0, y, image=whiteSheep, anchor=NW)
whiteHorse1 = a.create_image(recSize * 3 + recSize * 1, y, image=whiteHorse, anchor=NW)
whiteOfficer1 = a.create_image(recSize * 3 + recSize * 2, y, image=whiteOfficer, anchor=NW)
whiteKing1 = a.create_image(recSize * 3 + recSize * 3, y, image=whiteKing, anchor=NW)
whiteQueen1 = a.create_image(recSize * 3 + recSize * 4, y, image=whiteQueen, anchor=NW)
whiteOfficer2 = a.create_image(recSize * 3 + recSize * 5, y, image=whiteOfficer, anchor=NW)
whiteHorse2 = a.create_image(recSize * 3 + recSize * 6, y, image=whiteHorse, anchor=NW)
whiteSheep2 = a.create_image(recSize * 3 + recSize * 7, y, image=whiteSheep, anchor=NW)

whiteSoldier1 = a.create_image(recSize * 3 + recSize * 0, y + recSize, image=whiteSoldier, anchor=NW)
whiteSoldier2 = a.create_image(recSize * 3 + recSize * 1, y + recSize, image=whiteSoldier, anchor=NW)
whiteSoldier3 = a.create_image(recSize * 3 + recSize * 2, y + recSize, image=whiteSoldier, anchor=NW)
whiteSoldier4 = a.create_image(recSize * 3 + recSize * 3, y + recSize, image=whiteSoldier, anchor=NW)
whiteSoldier5 = a.create_image(recSize * 3 + recSize * 4, y + recSize, image=whiteSoldier, anchor=NW)
whiteSoldier6 = a.create_image(recSize * 3 + recSize * 5, y + recSize, image=whiteSoldier, anchor=NW)
whiteSoldier7 = a.create_image(recSize * 3 + recSize * 6, y + recSize, image=whiteSoldier, anchor=NW)
whiteSoldier8 = a.create_image(recSize * 3 + recSize * 7, y + recSize, image=whiteSoldier, anchor=NW)

#   black Assets ----------------------------------------------------------------------------------------


blackSheep1 = a.create_image(recSize * 3 + recSize * 0, y * 8, image=blackSheep, anchor=NW)
blackHorse1 = a.create_image(recSize * 3 + recSize * 1, y * 8, image=blackHorse, anchor=NW)
blackOfficer1 = a.create_image(recSize * 3 + recSize * 2, y * 8, image=blackOfficer, anchor=NW)
blackKing1 = a.create_image(recSize * 3 + recSize * 3, y * 8, image=blackKing, anchor=NW)
blackQueen1 = a.create_image(recSize * 3 + recSize * 4, y * 8, image=blackQueen, anchor=NW)
blackOfficer2 = a.create_image(recSize * 3 + recSize * 5, y * 8, image=blackOfficer, anchor=NW)
blackHorse2 = a.create_image(recSize * 3 + recSize * 6, y * 8, image=blackHorse, anchor=NW)
blackSheep2 = a.create_image(recSize * 3 + recSize * 7, y * 8, image=blackSheep, anchor=NW)

blackSoldier1 = a.create_image(recSize * 3 + recSize * 0, y * 7, image=blackSoldier, anchor=NW)
blackSoldier2 = a.create_image(recSize * 3 + recSize * 1, y * 7, image=blackSoldier, anchor=NW)
blackSoldier3 = a.create_image(recSize * 3 + recSize * 2, y * 7, image=blackSoldier, anchor=NW)
blackSoldier4 = a.create_image(recSize * 3 + recSize * 3, y * 7, image=blackSoldier, anchor=NW)
blackSoldier5 = a.create_image(recSize * 3 + recSize * 4, y * 7, image=blackSoldier, anchor=NW)
blackSoldier6 = a.create_image(recSize * 3 + recSize * 5, y * 7, image=blackSoldier, anchor=NW)
blackSoldier7 = a.create_image(recSize * 3 + recSize * 6, y * 7, image=blackSoldier, anchor=NW)
blackSoldier8 = a.create_image(recSize * 3 + recSize * 7, y * 7, image=blackSoldier, anchor=NW)

window.mainloop()
