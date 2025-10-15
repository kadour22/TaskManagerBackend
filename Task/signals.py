from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Task
from .tasks import send_task_email
from django.utils.dateparse import parse_datetime  
@receiver(post_save, sender=Task)
def schedule_task_email(sender, instance, **kwargs):
    scheduled_time = instance.scheduled_time

    # If it's a string, parse it
    if isinstance(scheduled_time, str):
        scheduled_time = parse_datetime(scheduled_time)
    
    # Make timezone-aware if naive
    if scheduled_time and timezone.is_naive(scheduled_time):
        scheduled_time = timezone.make_aware(scheduled_time, timezone.get_current_timezone())

    if scheduled_time and scheduled_time > timezone.now():
        send_task_email.apply_async((instance.id,), eta=scheduled_time)