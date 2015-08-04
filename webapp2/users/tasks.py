from celery import shared_task              # celery

from django.http import HttpResponse        # django

from push import easypush                   # project


FRIEND_FORMAT_STRING = '%s加你好友'
CUSTOM_TYPE = 'type'
CUSTOM_TYPE_FRIEND = 'friend'
CUSTOM_SENDER = 'sender'


@shared_task
def add_req_push(sender, receiver):
    alert = FRIEND_FORMAT_STRING % sender.username
    custom = {
        CUSTOM_TYPE: CUSTOM_TYPE_FRIEND,
        CUSTOM_SENDER: sender.username,
    }
    msg = easypush.BuildIOSMsg(alert, custom)
    easypush.DemoPushToken(msg, receiver.token)
