from push import easypush
from django.http import HttpResponse

from celery import shared_task

@shared_task
def add_req_push(sender, receiver):
    alert = '%s加你好友' % sender.username
    custom = {
        'type': 'friend',
        'sender': str(sender.username),
    }
    msg = easypush.BuildIOSMsg(alert, custom)
    easypush.DemoPushToken(msg, receiver.token)

def add_req_push_n(sender, receiver):
    alert = '%s加你好友' % sender.username
    custom = {
        'type': 'friend',
        'sender': sender.username,
    }
    msg = easypush.BuildIOSMsg(alert, custom)
    easypush.DemoPushToken(msg, receiver.token)

@shared_task
def test_celery():
    from .models import Test
    Test.objects.create(text='1231231401-2402930-4295')