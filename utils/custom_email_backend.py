# utils/custom_email_backend.py

from django.core.mail.backends.smtp import EmailBackend
import smtplib

class CustomEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False
        try:
            self.connection = self.connection_class(self.host, self.port)
            self.connection.ehlo()
            if self.use_tls:
                self.connection.starttls()  # Ensure no keyfile argument is passed
                self.connection.ehlo()
            self.connection.login(self.username, self.password)
        except smtplib.SMTPException:
            if self.fail_silently:
                return False
            raise
        return True
