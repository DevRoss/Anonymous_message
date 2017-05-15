import qrcode
import base64


def generate_ss_link(self, obj):
    config = '{encrypt_method}:{password}@{ip}:{port}'
    config = config.format(encrypt_method=obj.encrypt_method, password=obj.password, ip=obj.ip, port=obj.port)
    server_name = str('#' + obj.server_name).encode()
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
    img_name = server_name + b'.png'
    img = qr.make_image()
    img.save(img_name)
