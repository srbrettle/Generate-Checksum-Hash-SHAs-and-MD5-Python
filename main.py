from tkinter import Tk, Label, Button, StringVar, W, E, filedialog
import checksum

class ChecksumGui:

    def __init__(self, master):
        self.master = master
        master.title("Generate Checksum")

        self.filename = "..."
        self.sha1hash = "..."
        self.sha224hash = "..."
        self.sha256hash = "..."
        self.sha384hash = "..."
        self.sha512hash = "..."
        self.sha3_224hash = "..."
        self.sha3_256hash = "..."
        self.sha3_384hash = "..."
        self.sha3_512hash = "..."
        self.md5hash = "..."

        self.filename_label_text = StringVar()
        self.filename_label_text.set(self.filename)
        self.filename_label = Label(master, textvariable=self.filename_label_text)

        self.sha1hash_label_text = StringVar()
        self.sha1hash_label_text.set(self.sha1hash)
        self.sha1hash_label = Label(master, textvariable=self.sha1hash_label_text)
        self.sha224hash_label_text = StringVar()
        self.sha224hash_label_text.set(self.sha224hash)
        self.sha224hash_label = Label(master, textvariable=self.sha224hash_label_text)
        self.sha256hash_label_text = StringVar()
        self.sha256hash_label_text.set(self.sha256hash)
        self.sha256hash_label = Label(master, textvariable=self.sha256hash_label_text)
        self.sha384hash_label_text = StringVar()
        self.sha384hash_label_text.set(self.sha384hash)
        self.sha384hash_label = Label(master, textvariable=self.sha384hash_label_text)
        self.sha512hash_label_text = StringVar()
        self.sha512hash_label_text.set(self.sha512hash)
        self.sha512hash_label = Label(master, textvariable=self.sha512hash_label_text)
        self.sha3_224hash_label_text = StringVar()
        self.sha3_224hash_label_text.set(self.sha3_224hash)
        self.sha3_224hash_label = Label(master, textvariable=self.sha3_224hash_label_text)
        self.sha3_256hash_label_text = StringVar()
        self.sha3_256hash_label_text.set(self.sha3_256hash)
        self.sha3_256hash_label = Label(master, textvariable=self.sha3_256hash_label_text)
        self.sha3_384hash_label_text = StringVar()
        self.sha3_384hash_label_text.set(self.sha3_384hash)
        self.sha3_384hash_label = Label(master, textvariable=self.sha3_384hash_label_text)
        self.sha3_512hash_label_text = StringVar()
        self.sha3_512hash_label_text.set(self.sha3_512hash)
        self.sha3_512hash_label = Label(master, textvariable=self.sha3_512hash_label_text)
        self.md5hash_label_text = StringVar()
        self.md5hash_label_text.set(self.md5hash)
        self.md5hash_label = Label(master, textvariable=self.md5hash_label_text)

        self.title_filename_label = Label(master, text="Filename:")
        self.title_sha1hash_label = Label(master, text="SHA-1 Hash:")
        self.title_sha224hash_label = Label(master, text="SHA-224 Hash:")
        self.title_sha256hash_label = Label(master, text="SHA-256 Hash:")
        self.title_sha384hash_label = Label(master, text="SHA-384 Hash:")
        self.title_sha512hash_label = Label(master, text="SHA-512 Hash:")
        self.title_sha3_224hash_label = Label(master, text="SHA-3-224 Hash:")
        self.title_sha3_256hash_label = Label(master, text="SHA-3-256 Hash:")
        self.title_sha3_384hash_label = Label(master, text="SHA-3-384 Hash:")
        self.title_sha3_512hash_label = Label(master, text="SHA-3-512 Hash:")
        self.title_md5hash_label = Label(master, text="MD5 Hash:")

        self.browse_button = Button(master, text="Browse...", command=lambda: self.update("browse"))
        self.generate_button = Button(master, text="Generate", command=lambda: self.update("generate"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # Layout
        self.title_filename_label.grid(row=0, column=0, sticky=W)
        self.browse_button.grid(row=0, column=4, sticky=W+E)
        self.filename_label.grid(row=0, column=1, columnspan=3, sticky=W)
        self.generate_button.grid(row=2, column=0, columnspan=4, sticky=W+E)
        self.reset_button.grid(row=2, column=4, sticky=W+E)
        self.title_sha1hash_label.grid(row=3, column=0, sticky=W)
        self.sha1hash_label.grid(row=3, column=1, columnspan=4, sticky=W)
        self.title_sha224hash_label.grid(row=4, column=0, sticky=W)
        self.sha224hash_label.grid(row=4, column=1, columnspan=4, sticky=W)
        self.title_sha256hash_label.grid(row=5, column=0, sticky=W)
        self.sha256hash_label.grid(row=5, column=1, columnspan=4, sticky=W)
        self.title_sha384hash_label.grid(row=6, column=0, sticky=W)
        self.sha384hash_label.grid(row=6, column=1, columnspan=4, sticky=W)
        self.title_sha512hash_label.grid(row=7, column=0, sticky=W)
        self.sha512hash_label.grid(row=7, column=1, columnspan=4, sticky=W)
        self.title_sha3_224hash_label.grid(row=8, column=0, sticky=W)
        self.sha3_224hash_label.grid(row=8, column=1, columnspan=4, sticky=W)
        self.title_sha3_256hash_label.grid(row=9, column=0, sticky=W)
        self.sha3_256hash_label.grid(row=9, column=1, columnspan=4, sticky=W)
        self.title_sha3_384hash_label.grid(row=10, column=0, sticky=W)
        self.sha3_384hash_label.grid(row=10, column=1, columnspan=4, sticky=W)
        self.title_sha3_512hash_label.grid(row=11, column=0, sticky=W)
        self.sha3_512hash_label.grid(row=11, column=1, columnspan=4, sticky=W)
        self.title_md5hash_label.grid(row=12, column=0, sticky=W)
        self.md5hash_label.grid(row=12, column=1, columnspan=4, sticky=W)

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
            Hashes = checksum.generateHash(self.filename)
            self.sha1hash = Hashes['sha1']
            self.sha1hash_label_text.set(self.sha1hash)
            self.sha224hash = Hashes['sha224']
            self.sha224hash_label_text.set(self.sha224hash)
            self.sha256hash = Hashes['sha256']
            self.sha256hash_label_text.set(self.sha256hash)
            self.sha384hash = Hashes['sha384']
            self.sha384hash_label_text.set(self.sha384hash)
            self.sha512hash = Hashes['sha512']
            self.sha512hash_label_text.set(self.sha512hash)
            self.sha3_224hash = Hashes['sha3_224']
            self.sha3_224hash_label_text.set(self.sha3_224hash)
            self.sha3_256hash = Hashes['sha3_256']
            self.sha3_256hash_label_text.set(self.sha3_256hash)
            self.sha3_384hash = Hashes['sha3_384']
            self.sha3_384hash_label_text.set(self.sha3_384hash)
            self.sha3_512hash = Hashes['sha3_512']
            self.sha3_512hash_label_text.set(self.sha3_512hash)
            self.md5hash = Hashes['md5']
            self.md5hash_label_text.set(self.md5hash)
        else: # reset
            self.clearFields()

    def clearFields(self):
        self.filename = "..."
        self.filename_label_text.set(self.filename)
        self.sha1hash = "..."
        self.sha1hash_label_text.set(self.sha1hash)
        self.sha224hash = "..."
        self.sha224hash_label_text.set(self.sha224hash)
        self.sha256hash = "..."
        self.sha256hash_label_text.set(self.sha256hash)
        self.sha384hash = "..."
        self.sha384hash_label_text.set(self.sha384hash)
        self.sha512hash = "..."
        self.sha512hash_label_text.set(self.sha512hash)
        self.sha3_224hash = "..."
        self.sha3_224hash_label_text.set(self.sha3_224hash)
        self.sha3_256hash = "..."
        self.sha3_256hash_label_text.set(self.sha3_256hash)
        self.sha3_384hash = "..."
        self.sha3_384hash_label_text.set(self.sha3_384hash)
        self.sha3_512hash = "..."
        self.sha3_512hash_label_text.set(self.sha3_512hash)
        self.md5hash = "..."
        self.md5hash_label_text.set(self.md5hash)

root = Tk()
my_gui = ChecksumGui(root)
root.mainloop()
