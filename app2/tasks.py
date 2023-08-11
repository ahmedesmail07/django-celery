# Create Celery Taks to Run
from .email import send_email_review
from celery import shared_task
from celery.utils.log import get_task_logger

# This function is used to get a logger instance
# that can be used to log messages related to the task
logger = get_task_logger(__name__)


@shared_task(name='send_review_email_task')
def send_review_email_task(name, email, review):
    logger.info("sent email review")
    return send_email_review(name, email, review)


@shared_task()
def add(x, y):
    return x+y
