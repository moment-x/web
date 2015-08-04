from celery import shared_task

from qpush import push

from .models import PendingData

@shared_task
def upload_pending_data_notify_receiver(sender, receiver, json):
    data = PendingData.objects.create(receiver=receiver, json=json)
    alert = '%s发你文件' % sender.username
    dic = {
        'type': 'file',
        'sender': sender.username,
        'url': '/squares/receive/%s' % data.id,
    }
    custom = {'custom': dic}
    msg = push.BuildIOSMsg(alert, custom)
    push.PushToken(msg, str(receiver.token))