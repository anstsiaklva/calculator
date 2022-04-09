from tkinter import *
from logger import Logger

class GUI:
    def __init__(self, processor):
        self.processor = processor
        self.logger = Logger()

        self.root = Tk()
        self.root.title("Calculator")

        self.e = Entry(self.root, width = 52, borderwidth = 1)
        self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        
        #digit button
        self.button_1 = Button(self.root, text='1', padx=40,pady=20, command=lambda: self.process_button('1'))
        self.button_2 = Button(self.root, text='2', padx=40,pady=20, command=lambda: self.process_button('2'))
        self.button_3 = Button(self.root, text='3', padx=40,pady=20, command=lambda: self.process_button('3'))
        self.button_4 = Button(self.root, text='4', padx=40,pady=20, command=lambda: self.process_button('4'))
        self.button_5 = Button(self.root, text='5', padx=40,pady=20, command=lambda: self.process_button('5'))
        self.button_6 = Button(self.root, text='6', padx=40,pady=20, command=lambda: self.process_button('6'))
        self.button_7 = Button(self.root, text='7', padx=40,pady=20, command=lambda: self.process_button('7'))
        self.button_8 = Button(self.root, text='8', padx=40,pady=20, command=lambda: self.process_button('8'))
        self.button_9 = Button(self.root, text='9', padx=40,pady=20, command=lambda: self.process_button('9'))
        self.button_0 = Button(self.root, text='0', padx=40,pady=20, command=lambda: self.process_button('0'))

        self.button_1.grid(row = 3,column=0)
        self.button_2.grid(row = 3,column=1)
        self.button_3.grid(row = 3,column=2)

        self.button_4.grid(row = 2,column=0)
        self.button_5.grid(row = 2,column=1)
        self.button_6.grid(row = 2,column=2)

        self.button_7.grid(row = 1,column=0)
        self.button_8.grid(row = 1,column=1)
        self.button_9.grid(row = 1,column=2)

        self.button_0.grid(row = 4,column=0)

        #operation buttons
        self.button_add = Button(self.root, text='+', padx=39, pady=20, command=lambda: self.process_button('+'))
        self.button_sub = Button(self.root, text='-', padx=40, pady=20, command=lambda: self.process_button('-'))
        self.button_mul = Button(self.root, text='*', padx=40, pady=20, command=lambda: self.process_button('*'))
        self.button_div = Button(self.root, text='/', padx=40, pady=20, command=lambda: self.process_button('/'))
        self.button_pow = Button(self.root, text='^', padx=39, pady=20, command=lambda: self.process_button('^'))

        self.button_eq = Button(self.root, text='=', padx=39, pady=20, command=self.process_eq_button)


        self.button_add.grid(row = 1, column = 4)
        self.button_sub.grid(row = 2, column = 4)
        self.button_mul.grid(row = 3, column = 4)
        self.button_div.grid(row = 4, column = 4)
        self.button_pow.grid(row = 5, column = 4)
        self.button_eq.grid(row = 5, column = 1)

        #system buttons
        self.button_LP = Button(self.root, text = '(', padx = 41, pady = 20, command=lambda: self.process_button('('))
        self.button_RP = Button(self.root, text = ')', padx = 41, pady = 20, command=lambda: self.process_button(')'))
        self.button_dot = Button(self.root, text = '.', padx = 42, pady = 20, command=lambda: self.process_button('.'))
        self.button_LP.grid(row = 4, column = 1)
        self.button_RP.grid(row = 4, column = 2)
        self.button_dot.grid(row = 5, column=2)

        self.button_clear = Button(self.root, text='c', padx = 40, pady = 20, command=self.process_clear_button)
        self.button_clear.grid(row = 5, column = 0)

        self.root.mainloop()
    
    def process_button(self, symbol):
        self.e.insert(END, symbol)

    def process_clear_button(self):
        self.e.delete(0, END)
    
    def process_eq_button(self):
        self.inp = self.e.get()
        self.e.delete(0, END)
        try:
            self.value = self.processor.process(self.inp)
        except:
            self.value = 'Syntax Error or Runtime Math Error' 


        self.logger.log(f"input: {self.inp}; output: {self.value}\n")
        self.e.insert(0, str(self.value))