import os
import requests
from decouple import config

def send_email_via_brevo(to_email, task_title):
    url = "https://api.brevo.com/v3/smtp/email"
    api_key = config("BREVO_API_KEY")
    data = {
        "sender": {"name": "Task Reminder", "email":config("EMAIL_HOST_USER")},
        "to": [{"email": to_email, "name": "User"}],
        "subject": "Task Reminder",
        "htmlContent": f"<html><body><h1>Hello {task.user.first_name}, Reminder for your task: {task_title}</h1></body></html>"
        }
    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json"
    }
    requests.post(url, json=data, headers=headers)