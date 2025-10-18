from celery import shared_task
from django.utils import timezone
from .models import Task
from .utils import send_email_via_brevo

@shared_task
def check_and_send_reminders():
    now = timezone.now()
    tasks = Task.objects.filter(scheduled_time__lte=now, is_notified=False)
    for task in tasks:
        send_email_via_brevo(task.user.email, task.title)
        task.is_notified = True
        task.save()
        print(f"Sent reminder for task: {task.title} to {task.user.email}")

