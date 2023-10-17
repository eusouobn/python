import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit

class PontoDeVenda(QWidget):
    def __init__(self):
        super().__init__()
        self.produtos = {
            "Produto 1": 10.99,
            "Produto 2": 7.50,
            "Produto 3": 5.25,
            "Produto 4": 15.75
        }
        self.carrinho = {}
        self.total = 0

        self.initUI()

    def adicionar_produto(self, produto):
        if produto in self.produtos:
            if produto in self.carrinho:
                self.carrinho[produto] += 1
            else:
                self.carrinho[produto] = 1
            self.total += self.produtos[produto]
            self.atualizar_total()

    def atualizar_total(self):
        self.total_label.setText(f"Total: {self.total:.2f}")

    def finalizar_compra(self):
        print("Recibo:")
        for produto, quantidade in self.carrinho.items():
            print(f"{produto}: {quantidade} x {self.produtos[produto]}")
        print(f"Total: {self.total:.2f}")
        self.close()

    def initUI(self):
        layout = QVBoxLayout()

        for produto in self.produtos:
            button = QPushButton(produto)
            button.clicked.connect(lambda _, p=produto: self.adicionar_produto(p))
            layout.addWidget(button)

        self.total_label = QLabel("Total: 0.00")
        layout.addWidget(self.total_label)

        finalizar_button = QPushButton("Finalizar Compra")
        finalizar_button.clicked.connect(self.finalizar_compra)
        layout.addWidget(finalizar_button)

        self.setLayout(layout)
        self.setWindowTitle('PDV')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PontoDeVenda()
    sys.exit(app.exec_())
