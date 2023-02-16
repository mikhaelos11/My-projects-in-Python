import tkinter as tk

calculation = ""
def addToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def EvaluateCalculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        ClearField()
        text_result.insert(1.0,"Error")

def ClearField():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x300")

text_result = tk.Text(root, height=2, width=16, font=("Tahoma",24))
text_result.grid(columnspan=5)
# numerical keyboard
btn_1 = tk.Button(root, text="1", command=lambda: addToCalculation(1), width=5, font=("Tahoma", 14))
btn_1.grid(row=2,column=1)
btn_2 = tk.Button(root, text="2", command=lambda: addToCalculation(2), width=5, font=("Tahoma", 14))
btn_2.grid(row=2,column=2)
btn_3 = tk.Button(root, text="3", command=lambda: addToCalculation(3), width=5, font=("Tahoma", 14))
btn_3.grid(row=2,column=3)
btn_4 = tk.Button(root, text="4", command=lambda: addToCalculation(4), width=5, font=("Tahoma", 14))
btn_4.grid(row=3,column=1)
btn_5 = tk.Button(root, text="5", command=lambda: addToCalculation(5), width=5, font=("Tahoma", 14))
btn_5.grid(row=3,column=2)
btn_6 = tk.Button(root, text="6", command=lambda: addToCalculation(6), width=5, font=("Tahoma", 14))
btn_6.grid(row=3,column=3)
btn_7 = tk.Button(root, text="7", command=lambda: addToCalculation(7), width=5, font=("Tahoma", 14))
btn_7.grid(row=4,column=1)
btn_8 = tk.Button(root, text="8", command=lambda: addToCalculation(8), width=5, font=("Tahoma", 14))
btn_8.grid(row=4,column=2)
btn_9 = tk.Button(root, text="9", command=lambda: addToCalculation(9), width=5, font=("Tahoma", 14))
btn_9.grid(row=4,column=3)
btn_0 = tk.Button(root, text="0", command=lambda: addToCalculation(0), width=5, font=("Tahoma", 14))
btn_0.grid(row=5,column=2)
# operators
btn_plus = tk.Button(root, text="+", command=lambda: addToCalculation("+"), width=5, font=("Tahoma", 14))
btn_plus.grid(row=2,column=4)
btn_minus = tk.Button(root, text="-", command=lambda: addToCalculation("-"), width=5, font=("Tahoma", 14))
btn_minus.grid(row=3,column=4)
btn_mul = tk.Button(root, text="*", command=lambda: addToCalculation("*"), width=5, font=("Tahoma", 14))
btn_mul.grid(row=4,column=4)
btn_div = tk.Button(root, text="/", command=lambda: addToCalculation("/"), width=5, font=("Tahoma", 14))
btn_div.grid(row=5,column=4)
# equal and parenthesis
btn_equals = tk.Button(root, text="=", command=lambda: EvaluateCalculation(), width=5, font=("Tahoma", 14))
btn_equals.grid(row=6,column=4)
btn_lpar = tk.Button(root, text="(", command=lambda: addToCalculation("("), width=5, font=("Tahoma", 14))
btn_lpar.grid(row=5,column=1)
btn_rpar = tk.Button(root, text=")", command=lambda: addToCalculation(")"), width=5, font=("Tahoma", 14))
btn_rpar.grid(row=5,column=3)
# clear button
btn_clear = tk.Button(root, text="C", command=ClearField, width=5, font=("Tahoma", 14))
btn_clear.grid(row=6,column=3)
#memory
'''btn_memory = tk.Button(root, text="M", command=Memory(), width=5, font=("Tahoma",14))
btn_memory.grid(row=6, column=2)'''
root.mainloop()
