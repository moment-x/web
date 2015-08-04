import tencentyun
import time

APPID = '10002458'
SECRET_ID = 'AKIDpfLlXhjLoRSEACPSgmqKbTjrnIiyscvR'
SECRET_KEY = 'IMbbMjxmuo7a9Bs2lYijE6Ys79i8y6qC'
BUCKET = 'atest'
AUTH = tencentyun.Auth(SECRET_ID, SECRET_KEY)


def multipleEntrySign(fileid=''):
    expired = int(time.time()) + 999
    sign = AUTH.get_app_sign_v2(BUCKET, fileid, expired)
    return sign
