import base64
import hashlib
import random
import unicodedata
from datetime import datetime


def generate_hash(length=5):
    salt = hashlib.sha1(str(random.random())).hexdigest()
    pepper = str(datetime.now())
    return hashlib.sha1(salt + pepper).hexdigest()[:length]


def barcode(code, args=None):
    options = dict()
    if args is not None:
        arguments = args.split(',')
        for arg_pair in arguments:
            key, value = arg_pair.split('=')
            options[key] = int(value)

    import barcode
    from io import BytesIO
    from .thirdparty import BarcodeImageWriter
    CODETYPE = 'code39'
    bc = barcode.get_barcode(CODETYPE)
    bc = bc(code, writer=BarcodeImageWriter(), add_checksum=False)
    bc.default_writer_options['quiet_zone'] = 6.4
    bc.default_writer_options['dpi'] = 300
    bc.default_writer_options['text_distance'] = 1.0
    bc.default_writer_options['module_height'] = 10.0
    # bc.default_writer_options['module_width'] = 0.3
    bc.default_writer_options['font_size'] = int(bc.default_writer_options['dpi'] / 10)

    # update by custom arguments
    bc.default_writer_options.update(options)

    #write PNG image
    output = BytesIO()
    bc.write(output)
    contents = output.getvalue()
    output.close()

    content = base64.b64encode(contents)

    return content.decode('utf8')


def remove_accents(input):
    """ Normalise (normalize) unicode string to remove umlauts, accents etc. """
    return unicodedata.normalize('NFKD', u''.__class__(input)).encode('ASCII', 'ignore')
