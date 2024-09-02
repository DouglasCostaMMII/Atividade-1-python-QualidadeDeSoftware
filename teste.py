import tkinter as tk
from tkinter import simpledialog, messagebox

class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Compras")
        self.root.geometry("600x500")

        self.items = {}
        self.current_id = 1

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
        self.listbox.pack(pady=20)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Adicionar", command=self.adicionar_item)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(root, text="Editar", command=self.editar_item)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Excluir", command=self.excluir_item)
        self.delete_button.pack(pady=5)

        self.mark_button = tk.Button(root, text="Marcar como Comprado", command=self.marcar_item)
        self.mark_button.pack(pady=5)

    def adicionar_item(self):
        item = self.entry.get()
        if item:
            
            item_id = self.current_id
            self.current_id += 1
            
            self.items[item_id] = item
            self.listbox.insert(tk.END, f"{item} (ID: {item_id})")
            self.entry.delete(0, tk.END)

    def editar_item(self):
        selected_item_index = self.listbox.curselection()
        if selected_item_index:
            selected_text = self.listbox.get(selected_item_index)
            item_id = int(selected_text.split(" (ID: ")[1][:-1])

            new_item = simpledialog.askstring("Editar Item", "Novo valor:")
            if new_item:
                
                self.items[item_id] = new_item
                self.listbox.delete(selected_item_index)
                self.listbox.insert(selected_item_index, f"{new_item} (ID: {item_id})")

    def excluir_item(self):
        selected_item_index = self.listbox.curselection()
        if selected_item_index:
            selected_text = self.listbox.get(selected_item_index)
            item_id = int(selected_text.split(" (ID: ")[1][:-1])
            
            confirm = messagebox.askyesno("Confirmação de Exclusão", "Tem certeza que deseja excluir este item?")
            if confirm:
                
                del self.items[item_id]
                self.listbox.delete(selected_item_index)

    def marcar_item(self):

        selected_item_index = self.listbox.curselection()
        if selected_item_index:
            selected_text = self.listbox.get(selected_item_index)
        item_id = int(selected_text.split(" (ID: ")[1][:-1])

        if " (Comprado)" not in self.items[item_id]:
            self.items[item_id] += " (Comprado)"
        else:
            messagebox.showwarning("Erro", "Produto já comprado")

        self.listbox.delete(selected_item_index)
        self.listbox.insert(selected_item_index, f"{self.items[item_id]} (ID: {item_id})")

        


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()