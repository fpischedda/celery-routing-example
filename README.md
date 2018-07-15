This code shows how to route tasks to specific queues, it can be useful to
prioritize tasks based on named queues.

Dependencies
------------

This example requires at least Python 3.6 (for no other reason than the use of
f-strings but still...) and Redis which is used by Celery to handle the tasks.
If you don't have Redis installed you can you the provided docker-compose.yml
to run it so you can keep your system clean.

Setting up the environment
--------------------------

- Install the dependencies using the provided requirements.txt file
- Run Redis


First example
_____________

For the first example we will have one worker listening to the low priority
queue and another listening to the default queue, to see the results it would
be ideal to have three terminals, two for the worker and one for the
task_test.py script.

Run the low priority worker with:
$ celery -A tasks worker --loglevel=INFO -Q low

Run the default priority worker with:
$ celery -A tasks worker --loglevel=INFO -Q default

Run the test script with:
$ python task_test.py

As you can see the low priority worker will be idle after it will finish to
handle the low priority tasks, and this is not ideal.o

Second example
______________

For the second example we will have to low priority worker listening to both
queues so it will not be idle when it finished with the low priority tasks

Run the low,default priority worker with:
$ celery -A tasks worker --loglevel=INFO -Q low,default

Run the default priority worker with:
$ celery -A tasks worker --loglevel=INFO -Q default

Run the test script with:
$ python task_test.py

In this case the first worker will continue to be busy when it will finish with
the low priority tasks solving the idling worker problem
