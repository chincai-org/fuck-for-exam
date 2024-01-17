import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLineEdit, QLabel, QComboBox, QCheckBox
from json import load, dump
from qdarkstyle import load_stylesheet_pyqt5

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

            # Import existing questions
            import_button = QPushButton('Import existing questions', bank_page)
            import_button.clicked.connect(lambda: self.import_questions(datas))
            layout.addWidget(import_button)

            # Create new item
            create_button = QPushButton('Create new question', bank_page)
            create_button.clicked.connect(lambda: self.new_question(datas))
            layout.addWidget(create_button)



        back_button = QPushButton('Back', bank_page)
        back_button.clicked.connect(self.back)
        layout.addWidget(back_button)

        self.pages.append(bank_page)
        self.stackedWidget.addWidget(bank_page)
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def import_questions(self, datas):
        import_page = QWidget()
        layout = QVBoxLayout(import_page)

        def manage_click(id):
            datas.append(id)
            self.dump_data(self.bank, "bank.json")

            self.back()

        for id, question in self.questions.items():
            button = QPushButton(question["name"], import_page)
            button.clicked.connect(lambda _, id=id: manage_click(id))
            layout.addWidget(button)

        self.pages.append(import_page)
        self.stackedWidget.addWidget(import_page)
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def new_question(self, datas):
        id = self.load_id()
        datas.append(id)
        self.dump_data(self.bank, "bank.json")

        self.questions[id] = {
            "name": "Write a unique name that helps u to identify this question",
            "questionType": "normal",
            "answerType": "objective",
            "question": "o sitelen e ijo pi sona ala lon ma ni",
            "answer": "Skribu vian respondon ĉi tie",
            "choices": [],
            "shuffle": False
        }

        self.dump_data(self.questions, "questions.json")

        self.make_question_editor(id, self.questions[id])



    def edit_question(self, id, question):
        self.questions[id] = question

        self.dump_data(self.questions, "questions.json")

    def change_question(self, question, attr, value):
        question[attr] = value

    def make_question_editor(self, id, question: dict):
        question_page = QWidget()
        layout = QVBoxLayout(question_page)

        question_name = QLineEdit(question_page)
        question_name.setText(question["name"])
        question_name.textChanged.connect(lambda: self.change_question(question, "name", question_name.text()))
        layout.addWidget(question_name)

        # Question type
        layout.addWidget(QLabel("Question Type:"))

        question_type = QComboBox(question_page)
        question_type.addItems(QUESTION_TYPES)
        question_type.setCurrentIndex(QUESTION_TYPES.index(question["questionType"]))
        question_type.currentIndexChanged.connect(lambda index, q=question: self.change_question(q, "questionType", QUESTION_TYPES[index]))
        layout.addWidget(question_type)

        # Answer type
        layout.addWidget(QLabel("Answer Type:"))

        answer_type = QComboBox(question_page)
        answer_type.addItems(ANSWER_TYPES)
        answer_type.setCurrentIndex(ANSWER_TYPES.index(question["answerType"]))
        answer_type.currentIndexChanged.connect(lambda index, q=question: self.change_question(q, "answerType", ANSWER_TYPES[index]))
        layout.addWidget(answer_type)

        # Question
        layout.addWidget(QLabel("Question:"))

        actual_question = QLineEdit(question_page)
        actual_question.setText(question["question"])
        actual_question.textChanged.connect(lambda: self.change_question(question, "question", actual_question.text()))
        layout.addWidget(actual_question)

        # Answer
        layout.addWidget(QLabel("Answer:"))

        actual_answer = QLineEdit(question_page)
        actual_answer.setText(question["answer"])
        actual_answer.textChanged.connect(lambda: self.change_question(question, "answer", actual_answer.text()))
        layout.addWidget(actual_answer)

        # Choices
        if question["answerType"] == "objective":
            self.make_choices(question_page, question, layout)

        # Shuffle
        layout.addWidget(QLabel("Shuffle:"))

        shuffle = QCheckBox(question_page)
        shuffle.setChecked(question["shuffle"])
        shuffle.stateChanged.connect(lambda state, q=question: self.change_question(q, "shuffle", bool(state)))
        layout.addWidget(shuffle)

        # Save
        save = QPushButton("Save", question_page)
        save.clicked.connect(lambda: self.edit_question(id, question))
        layout.addWidget(save)

        # Clone
        clone = QPushButton("Clone question", question_page)
        clone.clicked.connect(lambda: self.clone_question(question.copy()))
        layout.addWidget(clone)

        # # Delete
        # delete = QPushButton("Delete question", question_page)
        # delete.clicked.connect(lambda: self.delete_question(id))
        # layout.addWidget(delete)


        # Back
        back = QPushButton("Back", question_page)
        back.clicked.connect(self.back)
        layout.addWidget(back)


        self.pages.append(question_page)
        self.stackedWidget.addWidget(question_page)
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def clone_question(self, question):
        question["name"] += "-clone"
        self.questions[self.load_id()] = question
        self.dump_data(self.questions, "questions.json")


    def make_choices(self, question_page, question, layout):
        layout.addWidget(QLabel("Choices:"))

        for i, choice in enumerate(question["choices"]):
            choice_widget = QLineEdit(question_page)
            choice_widget.setText(choice)
            choice_widget.textChanged.connect(lambda _, c=choice, i=i, q=question: self.change_choice(q["choices"], i, choice_widget.text()))
            layout.addWidget(choice_widget)

    def change_choice(self, choice, index, value):
        choice[index] = value


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
    app.setStyleSheet(load_stylesheet_pyqt5())  # Apply dark mode
    mainWindow = MainWindow()
    sys.exit(app.exec_())
