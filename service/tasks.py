from celery import Celery, Task
from database import db
from dotenv import load_dotenv
import os

from service.saveResultToFile import saveResultToFile

load_dotenv()
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST")

celery = Celery(
    'tasks',
    broker = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@localhost:5672/{RABBITMQ_VHOST}'   
)

class FibonacciTask(Task):
    def on_success(self, result, task_id, args, kwargs):
        saveResultToFile(task_id, result)
        
        cursor = db.cursor()
        cursor.execute(f""" 
            INSERT INTO task_table (task_id, result) VALUES ('{task_id}', {result}) 
            """
        )
        db.commit()


@celery.task(base = FibonacciTask) 
def calcFibonacci(n):
    if n <= 0:
        return False
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return calcFibonacci(n - 1) + calcFibonacci(n - 2)