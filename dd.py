import tkinter as tk

root = tk.Tk()

# Create a Canvas widget with a fixed height
canvas = tk.Canvas(root, height=300)
canvas.pack(fill="both", expand=True)

# Create a Scrollbar and link it to the canvas
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.config(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the child widgets
frame = tk.Frame(canvas)

# Create a window on the canvas containing the frame
canvas.create_window((0, 0), window=frame, anchor="nw")

# Add some widgets to the frame
for i in range(50):
    tk.Label(frame, text=f"Label {i+1}").pack()

# Update the scroll region based on the content size
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
