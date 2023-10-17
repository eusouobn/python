import tkinter as tk

class PontoDeVenda:
    def __init__(self, root):
        self.root = root
        self.root.title("PDV")

        self.produtos = {
            "Produto 1": 10.99,
            "Produto 2": 7.50,
            "Produto 3": 5.25,
            "Produto 4": 15.75
        }

        self.carrinho = {}
        self.total = tk.DoubleVar()

        self.construir_interface()

    def adicionar_produto(self, produto):
        if produto in self.produtos:
            if produto in self.carrinho:
                self.carrinho[produto] += 1
            else:
                self.carrinho[produto] = 1
            self.atualizar_total()

    def atualizar_total(self):
        total = sum(self.produtos[produto] * quantidade for produto, quantidade in self.carrinho.items())
        self.total.set(total)

    def finalizar_compra(self):
        print("Recibo:")
        for produto, quantidade in self.carrinho.items():
            print(f"{produto}: {quantidade} x {self.produtos[produto]}")
        print(f"Total: {self.total.get()}")

    def construir_interface(self):
        for produto in self.produtos:
            tk.Button(self.root, text=produto, command=lambda p=produto: self.adicionar_produto(p)).pack()

        tk.Label(self.root, text="Total:").pack()
        tk.Label(self.root, textvariable=self.total).pack()

        tk.Button(self.root, text="Finalizar Compra", command=self.finalizar_compra).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = PontoDeVenda(root)
    root.mainloop()
