import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt  # 1. Importe o Qt no topo do arquivo

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha primeira janela")
        self.resize(400, 250)

        rotulo = QLabel("Olá, PySide6!", parent=self)
        self.setCentralWidget(rotulo)
        rotulo.setAlignment(Qt.AlignCenter)  # 2. Use o alinhamento corretamente


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())