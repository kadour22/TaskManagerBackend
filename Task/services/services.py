from .models import Task

def task_list() :
    return Task.objects.select_related("user").all()

def create_task(data):
    return Task.objects.create(**data)

def update_task(task_id, data):
    task = Task.objects.get(id=task_id)
    for key, value in data.items():
        setattr(task, key, value)
    task.save()
    return task

def delete_task(task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return True