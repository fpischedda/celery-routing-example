"""
This module routes the tasks to two different queues, it is used to test
the behaviour of the workers that listen to specific queues
"""
import tasks


def gen_id():
    idx = 0
    while True:
        idx = idx + 1
        yield idx


if __name__ == '__main__':

    generator = gen_id()
    for i in range(5):
        tasks.task.apply_async(args=('low', next(generator)),
                               queue='low')

    for i in range(15):
        tasks.task.apply_async(args=('default', next(generator)),
                               queue='default')
