import qrcode
import uuid

url = input('Enter your url :')

qr = qrcode.make(f'{url}')

qr.save(f'{uuid.uuid4()}.png')