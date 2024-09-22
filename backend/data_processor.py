import sqlite3
from notifier import Notifier

class DataProcessor:
    def __init__(self, threshold, notifier):
        self.threshold = threshold
        self.notifier = notifier
        self.values = []

        # Inicializar banco de dados
        self.conn = sqlite3.connect('gas_data.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS gas_data (
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                value INTEGER
            )
        """)
        self.conn.commit()

    def process(self, value):
        self.values.append(value)
        self.cursor.execute("INSERT INTO gas_data (value) VALUES (?)", (value,))
        self.conn.commit()

        if value > self.threshold:
            print("ALERTA: Vazamento de gás detectado!")
            self.notifier.send_notification(value)

    def get_recent_values(self, window_size=10):
        return self.values[-window_size:]
