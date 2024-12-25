from tkinter import *
from tkinter import ttk
import webbrowser

def pasteToClipboard(stringToPaste):
    root.clipboard_clear()
    root.clipboard_append(stringToPaste)
    clipboard.set(stringToPaste)

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
root.config(padx=6, pady=6)
root.attributes('-topmost', True)
root.resizable(False, False)

# Logic
chars = "∀∂∃∅∆∇∞∫∏∑√≈≠≡≤≥⊂⊃⊄⊆⊇⊕⊗⊥⊮⊰⊱∪∩∧∨∼≃≅≆∝∞∠∫αβγδεζηθικλμνξοπρσςτυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
alwaysOnTop = IntVar(value=1)
favorites = "abcd"
clipboard = StringVar() # Currently selected character. Connected to clipboardInfo Label.
clipboard.set("None")

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

# Frames (1)
allChars = ttk.Frame(root, padding="0 0 0 0", borderwidth=5, relief="solid") # Holds allChars frame.
favoritesFrame = ttk.Frame(root, padding="0 0 0 0") # Holds fravoriteCharsFrame.
actionFrame = ttk.Frame (root, padding="0 6 0 0")

allChars.grid(row=0, column=0)
favoritesFrame.grid(row=0, column=1, sticky=N)
actionFrame.grid(row=1, column=0, columnspan=2)

## Frames (2)
charFrame = ttk.Frame(allChars, padding="3 3 3 3") # Lists all characters.
favoriteCharsFrame = ttk.Frame(favoritesFrame, padding="3 3 3 3") # Lists all favorite characters.

charFrame.grid(row=1, column=0, sticky=N)
favoriteCharsFrame.grid(row=1, column=0, sticky=N)

# Widgets (1)
allCharsLabel = ttk.Label(allChars, text="All characters")
favoriteCharsLabel = ttk.Label(favoritesFrame, text="Favorites")
clipboardLabel = ttk.Label(actionFrame, text="Clipboard :")
clipboardInfo = ttk.Label(actionFrame, textvariable=clipboard)
addButton = ttk.Button(actionFrame, text="Add to Favorites")
removeButton = ttk.Button(actionFrame, text="Remove from Favorites")

allCharsLabel.grid(row=0, column=0)
favoriteCharsLabel.grid(row=0, column=0)
clipboardLabel.grid(row=0, column=0)
clipboardInfo.grid(row=0, column=1)
addButton.grid(row=0, column=2)
removeButton.grid(row=0, column=3)

# Widgets (2)
charButtons = createCharButtons(charFrame, chars)
favoriteCharButtons = createCharButtons(favoriteCharsFrame, favorites)

gridButtons(charButtons, 5)
gridButtons(favoriteCharButtons, 3)

root.mainloop()