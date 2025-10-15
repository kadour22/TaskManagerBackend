from .tasks import schedule_task_email
from django.utils import timezone

def schedule_email_for_task(task):
    if task.scheduled_time and task.scheduled_time > timezone.now():
        schedule_task_email.apply_async(
            args=[task.id],
            eta=task.scheduled_time  # exact datetime when to run
        )