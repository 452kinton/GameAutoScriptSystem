import base64


def image2Str(path):
    _image2str = ""
    with open(path, "rb") as imageFile:
        _image2str = base64.b64encode(imageFile.read())
    return _image2str

    