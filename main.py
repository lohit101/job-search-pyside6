import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFormLayout, QLineEdit, QComboBox, QLabel, QTableWidget, QTableWidgetItem
from PySide6.QtCore import QObject
from job_record import JobRecord
from database_manager import DatabaseManager

import sqlite3

opener = None

class Win(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Job Search Tool')
        self.layout = QVBoxLayout()

        db = sqlite3.connect("job_records.db")
        cursor = db.cursor()

        command = ''' SELECT * FROM job_records '''

        result = cursor.execute(command)

        self.table = QTableWidget(10, 5, self)

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                ftext = str(row_data[0]) + " : " + str(row_data[1]) + " | " + str(row_data[2]) + " | " + str(row_data[3]) + " | " + str(row_data[4]) + " | " + str(row_data[5]) + " | " + str(row_data[6])
                self.line = QLabel()
                self.line.setText(ftext)
                self.space = QLabel()
                self.space.setText("\n")
            self.layout.addWidget(self.line)

        self.setLayout(self.layout)

class JobSearchApp(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Job Search Tool')
        self.layout = QVBoxLayout()
        self.create_form()
        self.list_records_button = QPushButton('List Job Records')
        self.list_records_button.clicked.connect(self.open_listings)
        self.layout.addWidget(self.list_records_button)
        self.setLayout(self.layout)

    def create_form(self):
        form_layout = QFormLayout()
        self.advert_type_combobox = QComboBox()
        self.advert_type_combobox.addItems(['Internship', 'Work-Study', 'Job'])
        form_layout.addRow('Advert Type:', self.advert_type_combobox)

        self.status_combobox = QComboBox()
        self.status_combobox.addItems(['Yes', 'No', 'Pending'])
        form_layout.addRow('Status:', self.status_combobox)

        self.date_edit = QLineEdit()
        form_layout.addRow('Date:', self.date_edit)

        self.company_edit = QLineEdit()
        form_layout.addRow('Company:', self.company_edit)

        self.position_edit = QLineEdit()
        form_layout.addRow('Position:', self.position_edit)

        self.link_edit = QLineEdit()
        form_layout.addRow('Link:', self.link_edit)

        self.add_record_button = QPushButton('Add Job Record')
        self.add_record_button.clicked.connect(self.add_job_record)
        form_layout.addWidget(self.add_record_button)

        self.layout.addLayout(form_layout)

    def add_job_record(self):
        advert_type = self.advert_type_combobox.currentText()
        status = self.status_combobox.currentText()
        date = self.date_edit.text()
        company = self.company_edit.text()
        position = self.position_edit.text()
        link = self.link_edit.text()

        job_record = JobRecord(advert_type, status, date, company, position, link, "", "", "", "")
        self.db_manager.insert_record(job_record)

    def open_listings(self):
        global opener
        opener = Win(db_manager)
        opener.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db_path = 'job_records.db'  # Adjust the path as needed
    db_manager = DatabaseManager(db_path)
    window = JobSearchApp(db_manager)
    window.show()
    sys.exit(app.exec_())
