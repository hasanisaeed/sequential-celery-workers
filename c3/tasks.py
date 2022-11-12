from celery import Celery
from kombu import Queue

app = Celery('tasks', broker='pyamqp://guest@localhost//',
              backend='redis://:12345678@localhost/1/')

# app.conf.task_queues = (
#     # Queue('saeed',    routing_key='add_f'),
#     Queue('saeed',   routing_key='divide_.#'),
# )
@app.task(name='add_function', queue='celery')
def add(x, y):
    print('>> EXCHANGE...')
    return x + y


@app.task(name='divide_function', queue='saeed')
def divide(x, y):
    return x / y