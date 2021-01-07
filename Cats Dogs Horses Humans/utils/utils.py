import base64


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    # base64 is going to use lesser space as compared to total images bcoz it is images which is available in string format.
    # This is called encoded format.

    # So, we have decoding code as well to convert this encoded format back to the images.

    #Suppose , from UI we are transferring data to the server and we don't want anyone to decode our dataset so in that case
    # we can encode our dataset and then transfer.

    #----------------------------------------- CONCEPT ---------------------------------------------------------------------

    ## Images will be onverted into Base64 and this images which we have converted to base64 will be send to the model.
    ## Base64 is a array kind of structure and whenever we try to transfer data from client side(UI) to server side(model.h5)
    ## you are supposed to transfer those images in terms of base64 or any other encoding format.
