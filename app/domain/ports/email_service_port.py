from typing import Protocol

class EmailServicePort(Protocol):
    def send_email(self, to_email: str, subject: str, body: str) -> None:
        pass
