from tkinter import *
from tkinter import ttk
import webbrowser

def pasteToClipboard(stringToPaste):
    root.clipboard_clear()
    root.clipboard_append(stringToPaste)

def createCharButtons(frame, chars):
    charButtons = []
    for char in chars:
        charButtons.append(
            ttk.Button(
                frame,
                text=char,
                width=5,
                command=lambda c=char: pasteToClipboard(c)
            )
        )
    return charButtons

def gridButtons(buttons, noOfColumns):
    currentRow = 0
    currentColumn = 0
    for button in buttons:
        if currentColumn >= noOfColumns:
            currentRow += 1
            currentColumn = 0
        button.grid(row=currentRow, column=currentColumn)
        currentColumn += 1

def alwaysOnTopCheckButtonAction():
    if alwaysOnTop.get() == 1:
        root.attributes('-topmost', True)
    else:
        root.attributes('-topmost', False)

# Window
root = Tk()
root.title("Faseeh's CharMap")
root.attributes('-topmost', True)
root.resizable(False, False)

# Logic
chars = "∑∏∞∂∫∇±≠≤≥≈∝√∛∜∴∵∟⊥∞"
alwaysOnTop = IntVar(value=1)
favorites = "abcd"

# Menu
rootMenu = Menu(root)
root.config(menu=rootMenu)

## File Menu
fileMenu = Menu(rootMenu, tearoff=0)
fileMenu.add_command(label="Open Favourites File", command=lambda: print("open favourites"))
fileMenu.add_command(label="Clear Favourites")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=lambda: root.destroy())

## View Menu
viewMenu = Menu(rootMenu, tearoff=0)
viewMenu.add_checkbutton(label="Always on Top", variable=alwaysOnTop, command=alwaysOnTopCheckButtonAction)
viewMenu.add_command(label="Scale 1.0", command=pasteToClipboard("Scale"))
viewMenu.add_command(label="Scale 1.2", command=pasteToClipboard("Scale"))
viewMenu.add_command(label="Scale 1.4", command=pasteToClipboard("Scale"))
viewMenu.add_command(label="Scale 1.6", command=pasteToClipboard("Scale"))
viewMenu.add_separator()
viewMenu.add_command(label="Reset Scaling", command=pasteToClipboard("Reset"))

## Configure the menus.
rootMenu.add_cascade(label="File", menu=fileMenu)
rootMenu.add_cascade(label="View", menu=viewMenu)
rootMenu.add_command(label="Help", command=lambda: webbrowser.open("https://faseeh-z.github.io/"))

# Containers
charFrame = ttk.Frame(root, padding="6 6 6 6") # To place character buttons.
charFrame.grid(row=1, column=0, sticky=N)
favoritesFrame = ttk.Frame(root, padding="6 6 6 6")
favoritesFrame.grid(row=1, column=1, sticky=N)

# Widgets
allCharsLabel = ttk.Label(root, text="All characters")
allCharsLabel.grid(row=0, column=0)
favoriteCharsLabel = ttk.Label(root, text="Favorites")
favoriteCharsLabel.grid(row=0, column=1)

## Characters
charButtons = createCharButtons(charFrame, chars)
gridButtons(charButtons, 5)
favoriteCharButtons = createCharButtons(favoritesFrame, favorites)
gridButtons(favoriteCharButtons, 3)

root.mainloop()