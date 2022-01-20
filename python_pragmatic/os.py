from base64 import b64decode


def base64_to_file(content, file_path):
    f = open(file_path, "wb")

    try:
        f.write(content.decode('base64'))  # python 2
    except AttributeError:
        f.write(b64decode(content))  # python 3

    f.close()
