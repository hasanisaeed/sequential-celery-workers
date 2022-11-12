from celery import Celery, shared_task

app = Celery(__name__, 
             broker='pyamqp://guest@localhost//',
             backend='redis://:12345678@localhost/1/')

app.conf.task_default_queue = 'c3.queue'

@shared_task
def add(data):
    
    # Do your job!
    
    data['3'] = 'c3 (END)' 
    return data
