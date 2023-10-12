import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS job_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                advert_type TEXT,
                status TEXT,
                date TEXT,
                company TEXT,
                position TEXT,
                link TEXT,
                ad_text TEXT,
                contact TEXT,
                notes TEXT,
                reminder_dates TEXT
            )
        ''')
        self.conn.commit()

    def insert_record(self, job_record):
        self.cursor.execute('''
            INSERT INTO job_records (advert_type, status, date, company, position, link, ad_text, contact, notes, reminder_dates)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            job_record.advert_type, job_record.status, job_record.date,
            job_record.company, job_record.position, job_record.link,
            job_record.ad_text, job_record.contact, job_record.notes,
            job_record.reminder_dates
        ))
        self.conn.commit()

    def get_all_records(self):
        self.cursor.execute('SELECT * FROM job_records')
        return self.cursor.fetchall()
