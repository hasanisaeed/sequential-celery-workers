import sys

from tasks import add, divide

r1 = add.apply_async((87.7, 2), propagate= True)


divide.apply_async((200, 2), propagate= True)
