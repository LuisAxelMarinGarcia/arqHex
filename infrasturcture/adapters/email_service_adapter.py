import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ...infrastructure.config.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

class EmailServiceAdapter(EmailServicePort):
    def send_email(self, to_email: str, subject: str, body: str):
        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.starttls()
                server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                text = msg.as_string()
                server.sendmail(EMAIL_HOST_USER, to_email, text)
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")
