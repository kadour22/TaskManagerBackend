from celery import shared_task
from django.core.mail import send_mail
from .models import Task
from django.conf import settings
@shared_task
def send_task_email(task_id):
    try:
        task = Task.objects.get(id=task_id)
        send_mail(
            subject=f"Reminder: {task.title}",
            message=f"Your scheduled task is now due:\n\n{task.title}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[task.user.email],
        )
        print(f"✅ Email sent to {task.user.email} for task '{task.title}'")
    except Task.DoesNotExist:
        print(f"⚠️ Task with id={task_id} not found.")
