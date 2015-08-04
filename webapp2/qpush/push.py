try:
    from . import xinge
except ImportError:
    import xinge


ACCESS_ID = 2200132715
SECRET_KEY = 'aab48ad3def5f9d075cb39caf6ac9bc9'


# 定义iOS消息
def BuildIOSMsg(alert, custom):
    msg = xinge.MessageIOS()
    msg.alert = alert
    msg.badge = 1
    msg.custom = custom
    return msg

# 按token推送
def PushToken(msg, token, x=xinge.XingeApp(ACCESS_ID, SECRET_KEY)):
    x.PushSingleDevice(token, msg, xinge.XingeApp.ENV_DEV)

    
# 按app推送
def PushAll(msg, x=xinge.XingeApp(ACCESS_ID, SECRET_KEY)):
    x.PushAllDevices(0, msg, xinge.XingeApp.ENV_DEV)









