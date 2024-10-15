import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from .arxml_parsing import arxml_parsing

import logging
logging.basicConfig(level=logging.INFO)


class gui:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("500x150")
        self.filename = "AutosarFile.arxml"
        self.foldername = "db"
        self.show()

    def browsefile(self):
        tk.Tk().withdraw()
        self.filename = askopenfilename()
        if os.path.isfile(self.filename) and "xml" in self.filename:
            logging.info("ARXML File selected")
            tk.messagebox.showinfo(title="ARXML File selected", message=self.filename)
        else:
            logging.error("ARXMl path not valid")
            tk.messagebox.showerror("showerror", "Please Update valid ARXMl path")

    def browsefolder(self):
        tk.Tk().withdraw()
        self.foldername = askdirectory()
        if os.path.isdir(self.foldername):
            logging.info("Excel directory selected")
            tk.messagebox.showinfo(
                title="Excel directory selected", message=self.foldername
            )
        else:
            logging.error("Excel path not valid")
            tk.messagebox.showerror("showerror", "Please Update valid Excel path")

    def run(self):
        if (
            os.path.isfile(self.filename)
            and "xml" in self.filename
            and os.path.isdir(self.foldername)
        ):
            arxml_parsing(self.filename, self.foldername)
            self.root.quit()
        else:
            tk.messagebox.showerror(
                "showerror", "Please Update Both ARXMl and Excel valid paths"
            )
            logging.error("Please Update Both ARXMl and Excel valid paths")

    def show(self):
        row_1 = tk.Frame(self.root)
        arxml = tk.Label(row_1, text="Choose input ARXML file")
        arxml.pack(side=tk.LEFT)
        arxml_path = tk.Button(row_1, text="Browse", command=self.browsefile)
        arxml_path.pack(side=tk.RIGHT, padx=5, pady=5)
        row_1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=0)

        row_2 = tk.Frame(self.root)
        xl = tk.Label(row_2, text="Choose excel output directory")
        xl.pack(side=tk.LEFT)
        xl_path = tk.Button(row_2, text="Browse", command=self.browsefolder)
        xl_path.pack(side=tk.RIGHT, padx=5, pady=5)
        row_2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=0)

        row_3 = tk.Frame(self.root)
        run = tk.Button(row_3, text="Parse", command=self.run)
        run.pack(side=tk.LEFT, padx=40, pady=5)
        quit = tk.Button(row_3, text="Quit", command=self.root.quit)
        quit.pack(side=tk.RIGHT, padx=40, pady=5)
        row_3.pack(side=tk.TOP, fill=tk.X, padx=10, pady=0)
        self.root.mainloop()


if __name__ == "__main__":
    logging.info("Starting ARXML Parser tool GUI")
    gui()
    logging.info("DONE")
