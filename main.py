from tkinter import Tk, Label, Button, StringVar, W, E, filedialog
import checksum

class Sha256Gui:

    def __init__(self, master):
        self.master = master
        master.title("Generate SHA-256 Hash")

        self.filename = "..."
        self.sha256hash = "..."

        self.filename_label_text = StringVar()
        self.filename_label_text.set(self.filename)
        self.filename_label = Label(master, textvariable=self.filename_label_text)

        self.sha256hash_label_text = StringVar()
        self.sha256hash_label_text.set(self.sha256hash)
        self.sha256hash_label = Label(master, textvariable=self.sha256hash_label_text)

        self.title_filename_label = Label(master, text="Filename:")
        self.title_sha256hash_label = Label(master, text="SHA-256 Hash:")

        self.browse_button = Button(master, text="Browse...", command=lambda: self.update("browse"))
        self.generate_button = Button(master, text="Generate", command=lambda: self.update("generate"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # Layout
        self.title_filename_label.grid(row=0, column=0, columnspan=3, sticky=W)
        self.browse_button.grid(row=0, column=4, sticky=W+E)
        self.filename_label.grid(row=1, column=0, columnspan=4, sticky=W+E)
        self.generate_button.grid(row=2, column=0, columnspan=4, sticky=W+E)
        self.reset_button.grid(row=2, column=4, sticky=W+E)
        self.title_sha256hash_label.grid(row=3, column=0, columnspan=3, sticky=W)
        self.sha256hash_label.grid(row=4, column=0, columnspan=5, sticky=W+E)

    def update(self, method):
        if method == "browse":
            self.clearFields()
            root = Tk()
            file = filedialog.askopenfile(parent=root, mode='rb', title='Choose a file')
            if file != None:
                self.filename = file.name
                self.filename_label_text.set(self.filename)
            root.withdraw()
        elif method == "generate":
            self.sha256hash = checksum.generate_sha256(self.filename)
            self.sha256hash_label_text.set(self.sha256hash)
        else: # reset
            self.clearFields()

    def clearFields(self):
        self.filename = "..."
        self.filename_label_text.set(self.filename)
        self.sha256hash = "..."
        self.sha256hash_label_text.set(self.sha256hash)

root = Tk()
my_gui = Sha256Gui(root)
root.mainloop()
