from celery import Celery
from kombu import Queue

print(__file__)

app = Celery(__name__, broker='pyamqp://guest@localhost//',
              backend='redis://:12345678@localhost/1/')

app.conf.task_queues = (
    Queue('saeed',    routing_key='add'),
    Queue('celery',   routing_key='divide'),
)

@app.task(name='add_func', routing_key='add')
def add(x, y):
    print('>> EXCHANGE...')
    return x + y


@app.task(name='divide_func', routing_key='add')
def divide(x, y):
    return x / y