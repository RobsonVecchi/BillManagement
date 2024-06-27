import tkinter

#Window
root = tkinter.Tk()
root.geometry("1000x500")
root.title("Bill Management Made Easy")
root.resizable(False, False)

#Commands
def set_to_zero():
    entry_croissant.delete(0, tkinter.END)
    entry_americano.delete(0, tkinter.END)
    entry_bagel.delete(0, tkinter.END)
    entry_cappuccino.delete(0, tkinter.END)
    entry_espresso.delete(0, tkinter.END)
    entry_milk_shake.delete(0, tkinter.END)
    entry_mocha.delete(0, tkinter.END)

def show_total():
    try:a1=int(espresso.get())
    except:a1=0   
    
    try:a2=int(americano.get())
    except:a2=0
    
    try:a3=int(cappuccino.get())
    except:a3=0
    
    try:a4=int(mocha.get())
    except:a4=0
    
    try:a5=int(milk_shake.get())
    except:a5=0
    
    try:a6=int(bagel.get())
    except:a6=0

    try:a7=int(croissant.get())
    except:a7=0
    
    #Cost of each item * units:
    c1 = a1*7
    c2 = a2*10
    c3 = a3*16
    c4 = a4*18
    c5 = a5*28
    c6 = a6*16
    c7 = a7*18
    
    lbl_total = tkinter.Label(right_frame, font=("courier", 20), text="Total", width=18, fg="white", bg="grey10")
    lbl_total.place(x=0, y=60)

    entry_total = tkinter.Entry(right_frame, font=("courier", 20), textvariable=total_bill, highlightthickness=0, width=18, bg="grey10", fg="white", justify="center")
    entry_total.place(x=0, y=100)

    total_cost = c1+c2+c3+c4+c5+c6+c7
    string_bill = f"R$ {total_cost},00"
    total_bill.set(string_bill)
        
tkinter.Label(text="BILL MANAGEMENT MADE EASY", bg="black", fg="white", font=("calibri", 33), width="300", height="2").pack()

#Menu card
left_frame=tkinter.Frame(root, bg="grey16", highlightbackground="black", highlightthickness=1, width=290, height=370)
left_frame.place(x=10, y=118)

tkinter.Label(left_frame, text="Menu", font=("calibri", 40), fg="white", bg="grey16").place(x=80, y=0)

tkinter.Label(left_frame, font=("courier", 12), text="Espresso --------- R$  7,00", fg="white", bg="grey16").place(x=8, y=80)
tkinter.Label(left_frame, font=("courier", 12), text="Americano -------- R$ 10,00", fg="white", bg="grey16").place(x=8, y=120)
tkinter.Label(left_frame, font=("courier", 12), text="Cappuccino ------- R$ 16,00", fg="white", bg="grey16").place(x=8, y=160)
tkinter.Label(left_frame, font=("courier", 12), text="Mocha ------------ R$ 18,00", fg="white", bg="grey16").place(x=8, y=200)
tkinter.Label(left_frame, font=("courier", 12), text="Milk Shake ------- R$ 28,00", fg="white", bg="grey16").place(x=8, y=240)
tkinter.Label(left_frame, font=("courier", 12), text="Bagel ------------ R$ 16,00", fg="white", bg="grey16").place(x=8, y=280)
tkinter.Label(left_frame, font=("courier", 12), text="Croissant -------- R$ 18,00", fg="white", bg="grey16").place(x=8, y=320)

#Bill
right_frame = tkinter.Frame(root, bg="grey16", highlightbackground="black", highlightthickness=1, width=290, height=370)
right_frame.place(x=700, y=118)

bill = tkinter.Label(right_frame, text="Bill", font=("courier", 20), bg="white")
bill.place(x=110, y=10)

#Entry work
middle_frame=tkinter.Frame(root, bd=5, width=290, height=370, bg="grey16", highlightbackground="black", highlightthickness=1, )
middle_frame.place(x=310, y=118)

espresso = tkinter.StringVar()
americano = tkinter.StringVar()
cappuccino = tkinter.StringVar()
mocha = tkinter.StringVar()
milk_shake = tkinter.StringVar()
bagel = tkinter.StringVar()
croissant = tkinter.StringVar()
total_bill = tkinter.StringVar()

#Label
lbl_espresso = tkinter.Label(middle_frame, font=("courier", 20), text="Espresso", width=12, fg="grey16", pady=4)
lbl_espresso.grid(row=1, column=0)

lbl_americano = tkinter.Label(middle_frame, font=("courier", 20), text="Americano", width=12, fg="grey16", pady=4)
lbl_americano.grid(row=2, column=0)

lbl_cappuccino = tkinter.Label(middle_frame, font=("courier", 20), text="Cappuccino", width=12, fg="grey16", pady=4)
lbl_cappuccino.grid(row=3, column=0)

lbl_mocha = tkinter.Label(middle_frame, font=("courier", 20), text="Mocha", width=12, fg="grey16", pady=4)
lbl_mocha.grid(row=4, column=0)

lbl_milk_shake = tkinter.Label(middle_frame, font=("courier", 20), text="Milk shake", width=12, fg="grey16", pady=4)
lbl_milk_shake.grid(row=5, column=0)

lbl_bagel = tkinter.Label(middle_frame, font=("courier", 20), text="Bagel", width=12, fg="grey16", pady=4)
lbl_bagel.grid(row=6, column=0)

lbl_croissant = tkinter.Label(middle_frame, font=("courier", 20), text="Croissant", width=12, fg="grey16", pady=4)
lbl_croissant.grid(row=7, column=0)




#Entry
entry_espresso = tkinter.Entry(middle_frame, font=("courier", 20), textvariable=espresso, bd=2, width=8, bg="white")
entry_espresso.grid(row=1, column=1)

entry_americano = tkinter.Entry(middle_frame, font=("courier", 20), textvariable=americano, bd=2, width=8, bg="white")
entry_americano.grid(row=2, column=1)

entry_cappuccino = tkinter.Entry(middle_frame, font=("courier", 20), textvariable=cappuccino, bd=2, width=8, bg="white")
entry_cappuccino.grid(row=3, column=1)

entry_mocha = tkinter.Entry(middle_frame, font=("courier", 20), textvariable=mocha, bd=2, width=8, bg="white")
entry_mocha.grid(row=4, column=1)

entry_milk_shake = tkinter.Entry(middle_frame, font=("courier", 20), textvariable=milk_shake, bd=2, width=8, bg="white")
entry_milk_shake.grid(row=5, column=1)

entry_bagel = tkinter.Entry(middle_frame, font=("courier", 20), textvariable=bagel, bd=2, width=8, bg="white")
entry_bagel.grid(row=6, column=1)

entry_croissant = tkinter.Entry(middle_frame, font=("courier", 20), textvariable=croissant, bd=2, width=8, bg="white")
entry_croissant.grid(row=7, column=1)


#Buttons
btn_reset = tkinter.Button(middle_frame, fg="white", bg="grey16", font=("courier", 20), width=10, text="Reset", command=set_to_zero)
btn_reset.grid(row=8, column=0)

btn_total = tkinter.Button(middle_frame, fg="white", bg="grey16", font=("courier", 20), width=10, text="Total", command=show_total)
btn_total.grid(row=8, column=1)


root.mainloop()