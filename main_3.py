import tkinter as tk

def show_page(page):
    page.tkraise()

root = tk.Tk()
root.geometry("400x300")

# Creating multiple frames/pages
page1 = tk.Frame(root, bg="blue",width=100)
page2 = tk.Frame(root, bg="green")

# Adding content to pages
label1 = tk.Label(page1, text="Page 1", font=("Arial", 18,'bold'), pady=20)
label1.pack()

label2 = tk.Label(page2, text="Page 2", font=("Arial", 18), pady=20)
label2.pack()

# Displaying initial page
page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")

# Button to switch between pages
button1 = tk.Button(root, text="Go to Page 1", command=lambda: show_page(page1))
button1.grid(row=1, column=0, pady=10)

button2 = tk.Button(root, text="Go to Page 2", command=lambda: show_page(page2))
button2.grid(row=2, column=0, pady=10)

root.mainloop()