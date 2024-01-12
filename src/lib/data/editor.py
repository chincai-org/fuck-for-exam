import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLineEdit
from json import load, dump

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.load_data()
        self.init_ui()


    def load_data(self):
        with open('bank.json', 'r', encoding='utf-8') as f:
            self.bank = load(f)

        with open('questions.json', 'r', encoding='utf-8') as f:
            self.question = load(f)

        with open('definitions.json', 'r', encoding='utf-8') as f:
            self.definition = load(f)

    def dump_data(self, data, file):
        with open(file, 'w', encoding='utf-8') as f:
            dump(data, f, indent=4)

    def load_id(self):
        with open("uniq_id.txt", "r") as f:
            id = int(f.read())

        with open("uniq_id.txt", "w") as f:
            f.write(str(id + 1))

        return hex(id)[2:]


    def init_ui(self):
        self.setWindowTitle('Bank Editor')

        self.stackedWidget = QStackedWidget(self)
        self.pages = []

        home = self.make_home()
        self.pages.append(home)
        self.stackedWidget.addWidget(home)

        

        # Create main page with buttons to navigate to other pages
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.stackedWidget)

        self.setLayout(main_layout)
        self.show()

    def make_home(self):
        home_page = QWidget()
        layout = QVBoxLayout(home_page)

        layout.addWidget(self.make_bank_btn(home_page))

        

        return home_page

    def make_bank_btn(self, page):
        bank_btn = QPushButton('Bank', page)
        bank_btn.clicked.connect(self.bank_start)
        return bank_btn
    
    def bank_start(self, datas=None, history=None):
        if datas == False:
            datas = self.bank

        history = history or []

        bank_page = QWidget()
        layout = QVBoxLayout(bank_page)
        buttons = []

        for i, data in enumerate(datas):
            button = QPushButton(data["title"], bank_page)
            button.clicked.connect(lambda: self.bank_start(data["childs"], history + [i]))
            layout.addWidget(button)
            buttons.append(button)

        # Create new item

        new_item = QLineEdit(bank_page)
        new_item.setPlaceholderText('Create new item...')
        new_item.returnPressed.connect(lambda: self.new_item(layout, buttons, new_item, bank_page, history.copy(), datas))
        layout.addWidget(new_item)



        back_button = QPushButton('Back', bank_page)
        back_button.clicked.connect(self.back)
        layout.addWidget(back_button)

        self.pages.append(bank_page)
        self.stackedWidget.addWidget(bank_page)
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def back(self):
        self.stackedWidget.removeWidget(self.pages.pop(self.stackedWidget.currentIndex()))


    def new_item(self, layout, buttons, item: QLineEdit, bank_page, history, datas):
        datas.append({"id": self.load_id(), "title": item.text(), "childs": []})
        data = datas[-1]

        self.dump_data(self.bank, 'bank.json')

        button = QPushButton(item.text(), bank_page)
        button.clicked.connect(lambda: self.bank_start(data["childs"], history + [len(buttons)]))
        buttons.append(button)
        layout.insertWidget(len(buttons) - 1, button)
        item.setText('')



    def recursive_find(self, history: list, datas = None):
        datas = datas or self.bank

        if len(history) == 0:
            return datas

        print(history)
        index = history.pop(0)
        return self.recursive_find(history.copy(), datas[index]["childs"])


    def make_definition_btn(self):
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
