import tkinter as tk
from tkinter import simpledialog

class ShoppingListApp:
    def init(self, root):
        self.root = root
        self.root.title("Lista de Compras")

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.listbox.pack(pady=20)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.addbutton = tk.Button(root, text="Adicionar", command=self.adicionaritem)
        self.addbutton.pack(pady=5)

        self.editbutton = tk.Button(root, text="Editar", command=self.editar_item)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Excluir", command=self.excluir_item)
        self.delete_button.pack(pady=5)

        self.mark_button = tk.Button(root, text="Marcar como Comprado", command=self.marcar_item)
        self.mark_button.pack(pady=5)
        

    def adicionar_item(self):
        item = self.entry.get()
        if item:
            self.listbox.insert(tk.END, item)
            self.entry.delete(0, tk.END)

    def editar_item(self):
        selected_item_index = self.listbox.curselection()
        if selected_item_index:
            new_item = simpledialog.askstring("Editar Item", "Novo valor:")
            if new_item:
                self.listbox.delete(selected_item_index)
                self.listbox.insert(selected_item_index, new_item)

    def excluir_item(self):
        selected_item_index = self.listbox.curselection()
        if selected_item_index:
            self.listbox.delete(selected_item_index)

    def marcar_item(self):
        selected_item_index = self.listbox.curselection()
        if selected_item_index:
            item = self.listbox.get(selected_item_index)
            self.listbox.delete(selected_item_index)
            self.listbox.insert(selected_item_index, item + " (Comprado)")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()