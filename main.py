from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import platform
import webbrowser

def initialize() -> bool:
    """Returns True if it is the first time the user is opening the app."""
    path = "favorites.txt"
    if not os.path.exists(path): # Create 'favorites.txt' if it doesn't exist.
        with open (path, 'w', encoding="utf-8") as file:
            file.write("±√π∑∞θαβ≠≤≥∅∫≈±Ω")
        # Since there is no 'favorites.txt', it is the first time the user opening this app.
        firstTimeOpening = True
    else:
        firstTimeOpening = False
    return firstTimeOpening

def readFavourites():
    with open('favorites.txt', 'r', encoding="utf-8") as file:
        return file.read()
    
def refreshFavorites():
    with open("favorites.txt", 'w', encoding="utf-8") as file:
        file.write(favorites)

    # Destroy all favourite buttons.
    for widget in favoriteCharsFrame.winfo_children():
        widget.destroy()
    # Create new buttons.
    global favoriteCharButtons
    favoriteCharButtons = createCharButtons(favoriteCharsFrame, favorites)
    # Pack new buttons.
    gridButtons(favoriteCharButtons, 4)

def addToFavourites():
    global favorites
    favorites += clipboard.get()
    favorites = ''.join(sorted(favorites))
    refreshFavorites()

def removeFromFavorites():
    global favorites
    favorites = favorites.replace(clipboard.get(), '')
    favorites = ''.join(sorted(favorites))
    refreshFavorites()

def goToFavorites():
    filePath = "favorites.txt"
    if platform.system() == "Windows":  # For Windows.
        os.startfile(filePath)
    elif platform.system() == "Darwin":  # For MacOS.
        os.system(f"open {filePath}")
    else:  # For Linux.
        os.system(f"xdg-open {filePath}")

def clearFavorites():
    global favorites
    favorites = ""
    refreshFavorites()

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

def help():
    messagebox.showinfo("Quick help", "• Click on any character to copy it to your clipboard.\n• Add your favorite characters to the 'Favorites' list for easy access.\n• If you need a character that's missing, just add it using the 'Clipboard' field at the right!\n\n'Help/From the Web' for more information.")

# Window
root = Tk()
root.title("Faseeh's CharMap")
try:
    root.iconbitmap("assets/icon.ico")
except:
    print("Unable to load icon file")
root.config(padx=6, pady=6)
root.attributes('-topmost', True)
root.resizable(False, False)

# Logic
firstTimeOpening = initialize()
alwaysOnTop = IntVar(value=1)
favorites = readFavourites()
clipboard = StringVar() # Currently selected character. Connected to clipboardInfo Label.

# Menu
rootMenu = Menu(root)
root.config(menu=rootMenu)

## File Menu
fileMenu = Menu(rootMenu, tearoff=0)
fileMenu.add_command(label="Open Favourites File", command=goToFavorites)
fileMenu.add_command(label="Clear Favourites", command=clearFavorites)
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

## Help Menu
helpMenu = Menu(rootMenu, tearoff=0)
helpMenu.add_command(label="Quick help", command=help)
helpMenu.add_command(label="From the Web", command=lambda: webbrowser.open("https://faseeh-z.github.io/content/download/charmap.html"))

## Configure the menus.
rootMenu.add_cascade(label="File", menu=fileMenu)
rootMenu.add_cascade(label="View", menu=viewMenu)
rootMenu.add_cascade(label="Help", menu=helpMenu)

# Frames (1)
actionFrame = ttk.Frame (root, padding="0 6 0 0")
actionFrame.grid(row=0, column=1)

## Frames (2)
favoriteCharsFrame = ttk.Frame(root, padding="3 3 3 3") # Lists all favorite characters.
favoriteCharsFrame.grid(row=0, column=0, sticky=N)

# Widgets (1)
clipboardLabel = ttk.Label(actionFrame, text="Clipboard :")
clipboardInfo = ttk.Entry(actionFrame, textvariable=clipboard, width=5)
addButton = ttk.Button(actionFrame, text="Add", command=addToFavourites)
removeButton = ttk.Button(actionFrame, text="Remove", command=removeFromFavorites)

ACTION_FRAME_GAP = 2
clipboardLabel.grid(row=0, column=0, padx=ACTION_FRAME_GAP, pady=ACTION_FRAME_GAP)
clipboardInfo.grid(row=1, column=0, padx=ACTION_FRAME_GAP, pady=ACTION_FRAME_GAP)
addButton.grid(row=2, column=0, padx=ACTION_FRAME_GAP, pady=ACTION_FRAME_GAP)
removeButton.grid(row=3, column=0, padx=ACTION_FRAME_GAP, pady=ACTION_FRAME_GAP)

# Widgets (2)
favoriteCharButtons = createCharButtons(favoriteCharsFrame, favorites)

gridButtons(favoriteCharButtons, 4)

clipboard.set("") # Empty clipboard on start.

if firstTimeOpening:
    message = "Thanks for downloading my character map!\n\nHere's how to use it:\n• Click on any character to copy it to your clipboard.\n• Add your favorite characters to the 'Favorites' list for easy access.\n• If you need a character that's missing, just add it using the 'Clipboard' field at the right!"
    messagebox.showinfo("Faseeh's CharMap", message)

root.mainloop()
