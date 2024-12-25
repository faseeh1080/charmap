from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Faseeh's CharMap")
root.attributes('-topmost', True)

# Frame to place character buttons.
charFrame = ttk.Frame(root, padding="6 6 6 6")
charFrame.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def pasteToClipboard(stringToPaste):
    root.clipboard_clear()
    root.clipboard_append(stringToPaste)

chars = "∑∏∞∂∫∇±≠≤≥≈∝√∛∜∴∵∟⊥∞"
charButtons = []
numberOfColumns = 3
currentRow = 0
currentColumn = 0
for char in chars:
    charButtons.append(
        ttk.Button(
            charFrame,
            text=char,
            command=lambda c=char: pasteToClipboard(c)
        )
    )
    if currentColumn >= numberOfColumns:
        currentRow += 1
        currentColumn = 0
    charButtons[-1].grid(row=currentRow, column=currentColumn)
    currentColumn += 1

root.mainloop()