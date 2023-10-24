import tkinter as tk
from tkinter import messagebox

'''
1. n1+ n2 + n3 + n4 + n5 = l1
2. n1+ n2 + n3 + n4 - n5 = l2
- print l3 = "l1""l2"
'''
root = tk.Tk()
root.geometry("200x200")
root.title("Dekoder")

text_box = tk.Entry(root, width=10)
text_box.pack(pady=10)

output_box = tk.Text(root, height=1, width=10)
output_box.pack(pady=10)
output_box.config(state="disabled")

def check_digits():
    input = str(text_box.get())

    if len(str(input)) == 5:
       n1, n2, n3, n4, n5 = map(int, input)
       l1 = n1 + n2 + n3 + n4 + n5
       l2 = n1 + n2 + n3 + n4 - n5
       l3 = str(l1) + str(l2)
       output_box.config(state="normal")
       output_box.delete(1.0, tk.END)
       output_box.insert(tk.END, l3)
       output_box.tag_configure("center", justify="center")
       output_box.tag_add("center", "1.0", "end")
       output_box.config(state="disabled")
    
    else:
        messagebox.showerror("Podaj liczbę która ma 5 cyfr")


button = tk.Button(root, text="Check", command=check_digits)
button.pack()

root.mainloop()
        