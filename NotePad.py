import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from PIL import Image, ImageTk


class BlocNotes:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloc-Notes")

        # Charger une image personnalisée
        image = Image.open("N.png")
        self.custom_logo = ImageTk.PhotoImage(image)

        # Utiliser l'image comme logo
        self.root.iconphoto(False, self.custom_logo)

        # Créer un widget de zone de texte
        self.text_widget = tk.Text(self.root, wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Créer un menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Menu Fichier
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Fichier", menu=self.file_menu)
        self.file_menu.add_command(label="Nouveau", command=self.nouveau)
        self.file_menu.add_command(label="Ouvrir", command=self.ouvrir)
        self.file_menu.add_command(label="Enregistrer", command=self.enregistrer)
        self.file_menu.add_command(label="Enregistrer sous...", command=self.enregistrer_sous)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quitter", command=self.quitter)

        # Menu Edition
        self.edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edition", menu=self.edit_menu)
        self.edit_menu.add_command(label="Couper", command=self.couper)
        self.edit_menu.add_command(label="Copier", command=self.copier)
        self.edit_menu.add_command(label="Coller", command=self.coller)

    def nouveau(self):
        self.text_widget.delete(1.0, tk.END)

    def ouvrir(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)

    def enregistrer(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_widget.get(1.0, tk.END)
                file.write(content)

    def enregistrer_sous(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_widget.get(1.0, tk.END)
                file.write(content)

    def quitter(self):
        self.root.quit()

    def couper(self):
        self.text_widget.event_generate("<<Cut>>")

    def copier(self):
        self.text_widget.event_generate("<<Copy>>")

    def coller(self):
        self.text_widget.event_generate("<<Paste>>")


if __name__ == "__main__":
    root = tk.Tk()
    app = BlocNotes(root)
    root.mainloop()
