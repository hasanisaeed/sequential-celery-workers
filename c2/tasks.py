from celery import Celery, shared_task
from celery.result import allow_join_result

app = Celery(__name__, 
             broker='pyamqp://guest@localhost//',
             backend='redis://:12345678@localhost/1/')

app.conf.task_default_queue = 'c2.queue'


@shared_task
def add(data):
    
    # Do your job
    
    data['2'] = 'c2 -> c3'
    
    result = app.send_task(name='tasks.add',
                  args=[data],
             queue='c3.queue',
             bind=True)
    
    # This line is optional. Remove that!
    with allow_join_result():
        output = result.get()
    
    return output
