import tkinter as tk
from tkinter import ttk
from API_Logic import get_Conversion_rates

bg = "#252525"

titleFG = "green"

textFG = "white"

textfieldBG = "white"
textfieldFG = "black"

buttonBG = "white"
buttonFG = "#252525"

class UI:
    def __init__(self,root):
        self.root = root
        self.rateList = get_Conversion_rates()

        root.title("Exchange Rate")
        root.geometry("500x400")
        root.configure(bg= bg)
        root.resizable(False, False)
        title = tk.Label(root, text="Exchange Rate", font=("Segoe UI", 20,"bold"), fg =titleFG, bg=bg)
        title.pack(pady=30)

        frame = tk.Frame(root,bg=bg)
        frame.pack()


        From = tk.Label(frame,bg = bg,fg=textFG,text = "from ",font=("Segoe UI", 14,"bold"))
        From.grid(row= 0,column=0,padx =(0,10))

        self.amount = tk.Entry(frame,bg=textfieldBG,fg = textfieldFG,width=23)
        self.amount.grid(row=0,column=1,padx =10)

        options = self.rateList["options"]
        self.selected_option_from = tk.StringVar(value=options[0])

        combo = ttk.Combobox(
            frame,
            textvariable=self.selected_option_from,
            values=options
        )

        combo.grid(row=0, column=2, padx=10)

        to = tk.Label(frame, bg=bg, fg=textFG, text="to ", font=("Segoe UI", 14, "bold"))
        to.grid(row=1, column=0, padx=(0,10))

        self.selected_option_to = tk.StringVar(value=options[0])
        combo = ttk.Combobox(
            frame,
            textvariable=self.selected_option_to,
            values=options
        )

        combo.grid(row=1, column=1, padx=0)

        convert_button = tk.Button(frame, text = "   convert   ", bg = buttonBG,fg=buttonFG, command=self.convert_cliked,font=("Calibri", 12))
        convert_button.grid(row=1, column=2, padx=(0,50),pady=20)

        resultFrame = tk.Frame(root,bg=bg)
        resultFrame.pack(pady=20)

        self.result = tk.Label(resultFrame, bg=bg, fg=textFG, text="", font=("Segoe UI", 14, "bold"))
        self.result.grid(row=2, column=0, padx=10)




    def convert_cliked(self):
        amount = self.amount.get()
        try:
            amount= float(amount)
        except ValueError:
            self.result.config( text="Amount Can be only number")
            return

        rates = self.rateList["rates"]
        From =self.selected_option_from.get()
        To = self.selected_option_to.get()

        From_rate = rates[From]
        To_rate = rates[To]

        converted_amount = amount / From_rate
        converted_amount = converted_amount * To_rate
        result = str(converted_amount) + " " + To
        self.result.config(text=result)






