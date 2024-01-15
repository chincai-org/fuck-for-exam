import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLineEdit, QLabel, QComboBox, QCheckBox
from json import load, dump

QUESTION_TYPES = ["vocab", "normal"]
ANSWER_TYPES = ["objective", "subjective"]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.load_data()
        self.init_ui()


    def load_data(self):
        with open('bank.json', 'r', encoding='utf-8') as f:
            self.bank = load(f)

        with open('questions.json', 'r', encoding='utf-8') as f:
            self.questions = load(f)

        with open('definitions.json', 'r', encoding='utf-8') as f:
            self.definition = load(f)


    def get_question(self, id):
        return self.questions[id]

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

        layout.addWidget(QLabel(["Language", "Form", "Subject", "Bab", "Subbab", "Level", "Questions"][len(history)], bank_page))
        if datas and not isinstance(datas[0], str):
            for i, data in enumerate(datas):
                button = QPushButton(data["title"], bank_page)
                button.clicked.connect(lambda _, d=data["childs"], h=history + [i]: self.bank_start(d, h))
                layout.addWidget(button)
                buttons.append(button)

            # Create new item

            new_item = QLineEdit(bank_page)
            new_item.setPlaceholderText('Create new item...')
            new_item.returnPressed.connect(lambda: self.new_item(layout, buttons, new_item, bank_page, history.copy(), datas))
            layout.addWidget(new_item)
        else:
            for id, question in zip(datas, map(self.get_question, datas)):
                button = QPushButton(question["name"], bank_page)
                button.clicked.connect(lambda _, i=id, q=question: self.make_question_editor(i, q))
                layout.addWidget(button)




        back_button = QPushButton('Back', bank_page)
        back_button.clicked.connect(self.back)
        layout.addWidget(back_button)

        self.pages.append(bank_page)
        self.stackedWidget.addWidget(bank_page)
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def make_question_editor(self, id, question):
        question_page = QWidget()
        layout = QVBoxLayout(question_page)

        layout.addWidget(QLabel(question["name"], question_page))

        # Question type
        layout.addWidget(QLabel("Question Type:"))

        question_type = QComboBox(question_page)
        question_type.addItems(QUESTION_TYPES)
        question_type.setCurrentIndex(QUESTION_TYPES.index(question["questionType"]))
        layout.addWidget(question_type)

        # Answer type
        layout.addWidget(QLabel("Answer Type:"))

        answer_type = QComboBox(question_page)
        answer_type.addItems(ANSWER_TYPES)
        answer_type.setCurrentIndex(ANSWER_TYPES.index(question["answerType"]))
        layout.addWidget(answer_type)

        # Question
        layout.addWidget(QLabel("Question:"))

        actual_question = QLineEdit(question_page)
        actual_question.setText(question["question"])
        layout.addWidget(actual_question)

        # Answer
        layout.addWidget(QLabel("Answer:"))

        actual_answer = QLineEdit(question_page)
        actual_answer.setText(question["answer"])
        layout.addWidget(actual_answer)

        # Choices
        if question["answerType"] == "objective":
            self.make_choices(question_page, question, layout)

        # Shuffle
        layout.addWidget(QLabel("Shuffle:"))

        shuffle = QCheckBox(question_page)
        shuffle.setChecked(question["shuffle"])
        layout.addWidget(shuffle)

        self.pages.append(question_page)
        self.stackedWidget.addWidget(question_page)
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)


    def make_choices(self, question_page, question, layout):
        layout.addWidget(QLabel("Choices:"))

        for choice in question["choices"]:
            choice_widget = QLineEdit(question_page)
            choice_widget.setText(choice)
            layout.addWidget(choice_widget)


    def back(self):
        self.stackedWidget.removeWidget(self.pages.pop(self.stackedWidget.currentIndex()))


    def new_item(self, layout, buttons, item: QLineEdit, bank_page, history, datas):
        datas.append({"id": self.load_id(), "title": item.text(), "childs": []})
        data = datas[-1]

        self.dump_data(self.bank, 'bank.json')

        button = QPushButton(item.text(), bank_page)
        button.clicked.connect(lambda: self.bank_start(data["childs"], history + [len(buttons)]))
        buttons.append(button)
        layout.insertWidget(len(buttons), button)
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
