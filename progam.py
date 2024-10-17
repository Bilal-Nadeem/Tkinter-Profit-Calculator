import tkinter as tk

window = tk.Tk()

window.title("B")
window.iconbitmap("./ironman.ico")
window.geometry("180x170")
window.minsize(180, 180)
window.maxsize(180, 180)

f1 = tk.Frame()
f2 = tk.Frame()
f3 = tk.Frame()
f4 = tk.Frame()

labels = ["Amount Bought:", "Price Each Bought:", "Amount Sold:", "Price Each Sold:"]

#Bought

lbl_bought = tk.Label(text="Bought", font=("Arial", 11))
lbl_bought.pack()

lbl_bamount = tk.Label(f1, text="Amount:")
lbl_bamount.pack(side=tk.LEFT)
ent_bamount = tk.Entry(f1, width=17)
ent_bamount.pack(side=tk.RIGHT, padx=3)

lbl_bprice = tk.Label(f2, text="Price Each:")
lbl_bprice.pack(side=tk.LEFT)
ent_bprice = tk.Entry(f2, width=17)
ent_bprice.pack(side=tk.RIGHT, padx=3)

f1.pack(fill=tk.BOTH)
f2.pack(fill=tk.BOTH)

#Sold

lbl_sold = tk.Label(text="Sold", font=("Arial", 11))
lbl_sold.pack()

lbl_samount = tk.Label(f3, text="Amount:")
lbl_samount.pack(side=tk.LEFT)
ent_samount = tk.Entry(f3, width=17)
ent_samount.pack(side=tk.RIGHT, padx=3)

lbl_sprice = tk.Label(f4, text="Price Each:")
lbl_sprice.pack(side=tk.LEFT)
ent_sprice = tk.Entry(f4, width=17)
ent_sprice.pack(side=tk.RIGHT, padx=3)

f3.pack(fill=tk.BOTH)
f4.pack(fill=tk.BOTH)

#Submit

def submit(ignore=""):
    global lbl_submit
    try:
        if lbl_submit:
            lbl_submit.destroy()
    except:
        pass

    ba = ent_bamount.get()
    bp = ent_bprice.get()
    sa = ent_samount.get()
    sp = ent_sprice.get()

    ent_bamount.delete(0, tk.END)
    ent_bprice.delete(0, tk.END)
    ent_samount.delete(0, tk.END)
    ent_sprice.delete(0, tk.END)

    empty = False

    for _ in ba, bp, sa, sp:
        if _.strip() == "":
            txt = "Please fill all the fields"
            fg = "red"
            empty = True
            break
        try:
            int(_)
        except:
            txt = "Please input numbers"
            fg = "red"
            empty = True
            break


    if not empty:
        profit = (int(sa) * int(sp)) - (int(ba) * int(bp))
        txt = f"Profit: {profit}"
        fg = "black"

    lbl_submit = tk.Label(text=txt, font=("Arial", 10), fg=fg, bg="white")
    lbl_submit.pack()

btn_submit = tk.Button(text="Submit", command=submit)
btn_submit.pack(padx=5, pady=5)

window.bind('<Return>', submit)

window.mainloop()