from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def sleepy(duration):

    print('======================', duration)
    sleep(duration)
    return None

@shared_task
def send_mail_task():
    sleep(15)
    # send_mail(
    #     'PHONGTRANDEV RESET PASSWORD',
    #     'Here is the message.',
    #     'phongtran.dev',
    #     ['tanphongtr@gmail.com'],
    #     fail_silently=False,
    # )

    print('==============================')
    return None

@shared_task
def create_onetime_password():
    pass