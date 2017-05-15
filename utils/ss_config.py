import qrcode
import base64
from Anonymous_message.settings import MEDIA_ROOT
import os


def generate_ss_uri(serializer):
    config = '{encrypt_method}:{password}@{ip}:{port}'
    config = config.format(encrypt_method=serializer.validated_data['encrypt_method'],
                           password=serializer.validated_data['password'],
                           ip=serializer.validated_data['ip'], port=serializer.validated_data['port'])
    server_name = str('#' + serializer.validated_data['server_name']).encode()
    ret = b'ss://' + base64.urlsafe_b64encode(config.encode()) + server_name
    return ret


def generate_qc(ss_uri, server_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=5,
        border=0
    )
    qr.add_data(ss_uri)
    img_name = server_name + '.png'
    img = qr.make_image()
    path = os.path.join(MEDIA_ROOT, 'QR', img_name)
    img.save(stream=path)
