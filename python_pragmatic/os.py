def base64_to_file(content, file_path):
    f = open(file_path, "wb")
    f.write(content.decode('base64'))
    f.close()
