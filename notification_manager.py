import os
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)
        self.number = "+91 99620 41384"

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ.get("TWILIO_PHONE_NUMBER"),
            body=message_body,
            to=self.number
        )
        print(message.sid)
