from celery import Celery, shared_task
from celery.result import allow_join_result

app = Celery(__name__, 
             broker='pyamqp://guest@localhost//',
             backend='redis://:12345678@localhost/1/')

app.conf.task_default_queue = 'c1.queue'


@shared_task
def add(data):
    
    data['1'] = 'c1 -> c2'
    
    result = app.send_task(name='tasks.add',
                  args=[data],
             queue='c2.queue',
             bind=True)
    
    # This line is optional. Remove that!
    with allow_join_result():
        output = result.get()
    
    return output
 