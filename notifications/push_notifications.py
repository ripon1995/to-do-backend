# push.py

import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials

cred = credentials.Certificate("utils/todo-1938b-firebase-adminsdk-vdquj-077001057e.json")
firebase_admin.initialize_app(cred)
print("firebase app initialized")


def send_push_notification(token, title, body):
    message = messaging.Message(
        token=token,
        notification=messaging.Notification(
            title=title,
            body=body
        )
    )
    response = messaging.send(message)
