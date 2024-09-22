import smtplib
from email.mime.text import MIMEText

class Notifier:
    def __init__(self, email, password, recipient):
        self.email = email
        self.password = password
        self.recipient = recipient

    def send_notification(self, gas_value):
        subject = "Alerta de Vazamento de Gás"
        body = f"Vazamento de gás detectado! Valor do sensor: {gas_value}"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.email
        msg['To'] = self.recipient

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email, self.password)
            server.sendmail(self.email, self.recipient, msg.as_string())
            server.quit()
            print("Notificação enviada com sucesso.")
        except Exception as e:
            print(f"Erro ao enviar notificação: {e}")
