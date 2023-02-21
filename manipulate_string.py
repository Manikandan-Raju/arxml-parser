import re
import argparse
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import logging

logging.basicConfig(level=logging.INFO)

class Manipulate_string:
    def __init__(self):
        self.c = -1

    def manipulate(self, m):
        self.c += 1
        return f'{m.group(0).upper()}' if (self.c) % 2 == 0 else f'{m.group(0).lower()}'

    def output(self, string):
        o = re.sub('[A-Za-z]', lambda m: self.manipulate(m), string)
        logging.info('String manipulated')
        return o

class gui:

    def __init__(self,root) :
        self.root = root
        self.root.geometry('400x125')
        self.filename = ''
        self.foldername = ''
        self.show()

    def manipulate(self):
        if len(self.string.get().split(' ')) > 2:
            logging.info(f"input Sentence: {self.string.get()}")
            manipulate_string = Manipulate_string()
            output = manipulate_string.output(self.string.get())
            logging.info(f"Manipulated string: {output}")
            tk.messagebox.showinfo(title='output', message=output )
        else:
            tk.messagebox.showerror("showerror", "Enter a sentence with more than 2 words")
            logging.error('Sentence with less than 3 words')

    def show(self):
        row_1 = tk.Frame(self.root)
        sentence = tk.Label(row_1, text="Enter a sentence")
        sentence.pack(side=tk.LEFT)
        self.string = tk.Entry(row_1,width=100)
        self.string.pack(side=tk.RIGHT, padx=10, pady=10)
        row_1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        
        
        row_2 = tk.Frame(self.root)
        run = tk.Button(row_2, text='Manipulate',command=self.manipulate)
        run.pack(side=tk.LEFT, padx=70, pady=5)
        quit = tk.Button(row_2, text='Quit', command=self.root.quit)
        quit.pack(side=tk.RIGHT, padx=40, pady=5)
        row_2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        self.root.mainloop()

if __name__ == '__main__':
    cmd_parser = argparse.ArgumentParser(allow_abbrev=False)
    cmd_parser.add_argument(
        "--string",
        type=str,
        nargs="?",
        const="He is a Good Boy",
        help="Enter a sentence"
    )
    args = cmd_parser.parse_args()
    if args.string:
        logging.info(f"input Sentence: {args.string}")
        manipulate_string = Manipulate_string()
        output = manipulate_string.output(args.string)
        logging.info(f"Manipulated string: {output}")
    else:   
        logging.info("Starting  GUI")
        root = tk.Tk()
        gui(root)  
