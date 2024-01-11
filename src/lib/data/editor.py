import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLineEdit
from json import load, dump

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.load_data()
        self.initUI()


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

    def initUI(self):
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
        new_item.returnPressed.connect(lambda: self.new_item(layout, buttons, new_item, bank_page, history.copy()))
        layout.addWidget(new_item)



        back_button = QPushButton('Back', bank_page)
        back_button.clicked.connect(self.back)
        layout.addWidget(back_button)

        self.pages.append(bank_page)
        self.stackedWidget.addWidget(bank_page)
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def back(self):
        self.stackedWidget.removeWidget(self.pages.pop(self.stackedWidget.currentIndex()))


    def new_item(self, layout, buttons, item: QLineEdit, bank_page, history):
        datas = self.recursive_find(history.copy())
        print(history)
        datas.append({"title": item.text(), "childs": []})

        self.dump_data(self.bank, 'bank.json')

        button = QPushButton(item.text(), bank_page)
        button.clicked.connect(lambda: self.bank_start([], history + [len(buttons)]))
        buttons.append(button)
        layout.insertWidget(len(buttons) - 1, button)
        item.setText('')



    def recursive_find(self, history, datas = None):
        datas = datas or self.bank

        if len(history) == 0:
            return datas

        return self.recursive_find(datas[history.pop(0)]["childs"], history)


    def make_definition_btn(self):
        pass


    def createPage(self, index):
        page = QWidget()
        layout = QVBoxLayout(page)

        # Create buttons for the page
        for i in range(3):
            button = QPushButton(f'Page {index + 1} - Button {i + 1}', page)
            button.clicked.connect(lambda _, idx=index, btn=i: self.onButtonClick(idx, btn))
            layout.addWidget(button)

        # Add "Back" button
        back_button = QPushButton('Back', page)
        back_button.clicked.connect(self.goBack)
        layout.addWidget(back_button)

        return page

    def onButtonClick(self, pageIndex, buttonIndex):
        print(f'Button {buttonIndex + 1} on Page {pageIndex + 1} clicked')
        self.stackedWidget.setCurrentIndex(buttonIndex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
