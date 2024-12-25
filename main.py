from tkinter import *
from tkinter import ttk

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
    for button in charButtons:
        if currentColumn >= noOfColumns:
            currentRow += 1
            currentColumn = 0
        button.grid(row=currentRow, column=currentColumn)
        currentColumn += 1

# Logic
chars = "∑∏∞∂∫∇±≠≤≥≈∝√∛∜∴∵∟⊥∞"

# Window
root = Tk()
root.title("Faseeh's CharMap")
root.attributes('-topmost', True)

# Containers
charFrame = ttk.Frame(root, padding="6 6 6 6") # To place character buttons.
charFrame.grid(column=0, row=0, sticky=(N, W, E, S))

# Widgets
charButtons = createCharButtons(charFrame, chars)
gridButtons(charButtons, 5)

root.mainloop()