import hashlib
import random
import unicodedata
from base64 import b64encode
from datetime import datetime
from io import BytesIO


def generate_hash(length=5):
    salt = str(random.random())
    pepper = str(datetime.now())
    soup = (salt + pepper).encode('utf-8')
    return hashlib.sha1(soup).hexdigest()[:length]


def barcode(code, args=None):
    options = dict()
    if args is not None:
        arguments = args.split(',')
        for arg_pair in arguments:
            key, value = arg_pair.split('=')
            options[key] = int(value)

    from python_pragmatic.thirdparty import BarcodeImageWriter

    import barcode
    output = BytesIO()

    barcode.Code39(code=code,
                   # writer=ImageWriter(),  # has bottom padding
                   writer=BarcodeImageWriter(),  # removes bottom padding
                   add_checksum=False)\
        .write(output, options={
            # ImageWriter options
            # 'quiet_zone': 2.5,
            # 'dpi': 300,
            # 'font_size': 30,
            # 'module_height': 7.0,
            # 'text_distance': 2

            # BarcodeImageWriter options
            'quiet_zone': 2.5,
            'dpi': 300,
            'font_size': 60,
            'module_height': 7.0,
            'text_distance': 1
        })

    code_in_bytes = output.getvalue()
    code_in_base64_bytes = b64encode(code_in_bytes)
    code_in_base_64_string = code_in_base64_bytes.decode("utf-8")
    return code_in_base_64_string


def remove_accents(input):
    """ Normalise (normalize) unicode string to remove umlauts, accents etc. """
    return unicodedata.normalize('NFKD', str(input)).encode('ASCII', 'ignore')
