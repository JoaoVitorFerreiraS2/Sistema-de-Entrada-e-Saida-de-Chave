from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLabel
from PySide6.QtGui import QFont, QColor
from TesteMarcacaoDeChave2 import Ui_MainWindow
import sys
from datetime import datetime
import pandas as pd
import os.path
import psutil

tempo_de_reset = 2000
tempo_de_exibicao = 5000  # Tempo em milissegundos para exibir o registro antes de removê-lo da aplicação

#Essa aplicação foi feita para o local onde trabalho, existe uma entrada e saída de chaves de blocos onde os técnicos
#trabalham
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de entrada e saída de chave | @JoaoVitorFerreira")

        #Aqui fica o local onde é digitado a matricula do técnico
        self.text_label3 = QLabel("Matricula: <Digite sua matricula>", self.frame_3)
        self.text_label3.setGeometry(-100, -10, 580, 100)  # Ajuste as dimensões conforme necessário
        self.text_label3.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 14)
        self.text_label3.setFont(font)

        #A ação da entrada e saída de chaves
        self.text_label3 = QLabel("Ação: Escolha se é entrada ou saída da chave", self.frame_3)
        self.text_label3.setGeometry(-40, 30, 580, 100)  # Ajuste as dimensões conforme necessário
        self.text_label3.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 14)
        self.text_label3.setFont(font)

        self.pushButton.clicked.connect(self.confirmacao_tecnico)

        self.file_path = "<Aqui fica o local onde terá o excel como banco de dados>"

    def confirmacao_tecnico(self):
        self.pushButton.setEnabled(False)  # Desabilita o botão após o clique

        
        matricula = self.matricula_entry.text()
        
        tecnicos_por_matricula = {
            # Aqui fica o local onde as matriculas constaração. Exemplo:
            "00000": {"nome": "João Vitor", "bloco": "Bloco 2"}

        }  # Dados dos técnicos omitidos para manter o foco no problema

        if matricula in tecnicos_por_matricula:
            #Aqui é onde é feita a verificação da lista.
            tecnico_info = tecnicos_por_matricula[matricula]
            matricula = tecnico_info["nome"]
            bloco = tecnico_info["bloco"]
            matriculaX = matricula.split(' ')
            if self.entrada_radio.isChecked():
                acao = "Entrada"
            elif self.saida_radio.isChecked():
                acao = "Saída"
            else:
                QMessageBox.warning(self, "Aviso", f"Por favor, selecione uma ação.")
                self.pushButton.setEnabled(True)  # Habilita o botão novamente
                return
            
            # Mostrar mensagem de confirmação
            msg = QMessageBox()
            msg.setWindowTitle("Confirmação")
            msg.setText(f"Confirma o registro para Matrícula: {matriculaX[0]} | Ação: {acao}?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            
            # Capturar a resposta do usuário
            resposta = msg.exec()
            
            if resposta == QMessageBox.Yes:
                self.registrar_acao(matricula, bloco)
            else:
                self.pushButton.setEnabled(True)  # Habilitar o botão novamente

        else:
            QMessageBox.warning(self, "Registrado", f"A Matricula: {matricula} não foi reconhecida.")

        QTimer.singleShot(tempo_de_reset, self.habilitar_botao)

    def habilitar_botao(self):
        self.pushButton.setEnabled(True)

    def registrar_acao(self, matricula, bloco):
        
        if self.entrada_radio.isChecked():
            acao = "Entrada"
        elif self.saida_radio.isChecked():
            acao = "Saída"

        #Aqui é pego a data e hora do momento exato que é feita a confirmação
        data = datetime.now().strftime('%d-%m-%Y')
        hora = datetime.now().strftime('%H:%M:%S')

        row_count = self.registros_table.rowCount()
        self.registros_table.insertRow(row_count)

        item_matricula = QTableWidgetItem(matricula)
        item_matricula.setFlags(Qt.ItemIsEnabled)  # Impedir edição direta do item
        item_matricula.setTextAlignment(Qt.AlignCenter)
        self.registros_table.setItem(row_count, 0, item_matricula)

        item_acao = QTableWidgetItem(acao)
        item_acao.setFlags(Qt.ItemIsEnabled)  # Impedir edição direta do item
        item_acao.setTextAlignment(Qt.AlignCenter)
        self.registros_table.setItem(row_count, 1, item_acao)

        item_bloco = QTableWidgetItem(bloco)
        item_bloco.setFlags(Qt.ItemIsEnabled)  # Impedir edição direta do item
        item_bloco.setTextAlignment(Qt.AlignCenter)
        self.registros_table.setItem(row_count, 2, item_bloco)

        item_hora = QTableWidgetItem(hora)
        item_hora.setFlags(Qt.ItemIsEnabled)  # Impedir edição direta do item
        item_hora.setTextAlignment(Qt.AlignCenter)
        self.registros_table.setItem(row_count, 3, item_hora)

        item_data = QTableWidgetItem(data)
        item_data.setFlags(Qt.ItemIsEnabled)  # Impedir edição direta do item
        item_data.setTextAlignment(Qt.AlignCenter)
        self.registros_table.setItem(row_count, 4, item_data)

        self.matricula_entry.clear()
    

        self.export_to_excel()
        print(f'matricula: {matricula}, hora: {hora}')

        # Configuração do QTimer para remover a linha da tabela após um tempo de exibição
        QTimer.singleShot(tempo_de_exibicao, lambda: self.remover_registro(row_count))

    def remover_registro(self, row):
        #Retirada do registro da aplicação mas não do excel.
        self.registros_table.removeRow(row)

    def export_to_excel(self):
        #Aqui fica a exportação para o excel
        if os.path.isfile(self.file_path):
            existing_data = pd.read_excel(self.file_path)
        else:
            existing_data = pd.DataFrame(columns=["Matrícula", "Ação", "Bloco", "Hora", "Data"])

        df = pd.DataFrame(columns=["Matrícula", "Ação", "Bloco", "Hora", "Data"])
        for row in range(self.registros_table.rowCount()):
            matricula = self.registros_table.item(row, 0).text()
            acao = self.registros_table.item(row, 1).text()
            bloco = self.registros_table.item(row, 2).text()
            hora = self.registros_table.item(row, 3).text()
            data = self.registros_table.item(row, 4).text()

            if not existing_data.empty and \
                    (existing_data["Matrícula"] == matricula).any() and \
                    (existing_data["Ação"] == acao).any() and \
                    (existing_data["Bloco"] == bloco).any() and \
                    (existing_data["Hora"] == hora).any() and \
                    (existing_data["Data"] == data).any():
                continue
            else:
                df = pd.concat([df, pd.DataFrame({"Matrícula": [matricula], "Ação": [acao], "Bloco": [bloco], "Hora": [hora], "Data": [data]})], ignore_index=True)

        df = pd.concat([existing_data, df], ignore_index=True)

        df.to_excel(self.file_path, index=False)

    def load_data_from_excel(self):
        #Aqui carrega a planilha

        try:
            df = pd.read_excel(self.file_path)
            QMessageBox.warning(self, "Bem vindo", f"Aplicação inicializada com sucesso")
            for index, row in df.iterrows():
                matricula = row["Matrícula"]
                acao = row["Ação"]
                bloco = row["Bloco"]
                hora = row["Hora"]
                data = row["Data"]
            self.pushButton.setEnabled(True)
            self.entrada_radio.setEnabled(True)
            self.saida_radio.setEnabled(True)
            self.matricula_entry.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.atualizar.setEnabled(False)

        except:
            #Se o arquivo do excel estiver em algum local da rede, ele informa algumas informações do motivo de não está funcionando
            QMessageBox.warning(self, "Erro", f"Banco de dados não encontrado")
            self.pushButton.setEnabled(False)
            self.entrada_radio.setEnabled(False)
            self.saida_radio.setEnabled(False)
            self.matricula_entry.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.atualizar.setEnabled(True)
            QMessageBox.warning(self, "Verifique", f"Verifique se o cabo de internet está conectado ao computador")
            pergunta = QMessageBox.question(self, "Reiniciar", f"Posso Reiniciar a aplicação?", QMessageBox.Yes)

            if pergunta == QMessageBox.Yes:
                self.load_data_from_excel()
            
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.load_data_from_excel()
    window.show()
    sys.exit(app.exec())
