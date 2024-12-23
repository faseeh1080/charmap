from tkinter import *
from tkinter import ttk
import keyboard

root = Tk()
root.title("Faseeh's CharMap")

# Frame to place character buttons.
charFrame = ttk.Frame(root, padding="6 6 6 6")
charFrame.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

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
            command=lambda: keyboard.write(char)
        )
    )
    if currentColumn >= numberOfColumns:
        currentRow += 1
        currentColumn = 0
    charButtons[-1].grid(row=currentRow, column=currentColumn)
    currentColumn += 1

root.mainloop()