# push.py

from firebase_admin import messaging


def send_push_notification(token, title, body):
    message = messaging.Message(
        token=token,
        notification=messaging.Notification(
            title=title,
            body=body
        )
    )
    response = messaging.send(message)
    print('Push notification sent:', response)
