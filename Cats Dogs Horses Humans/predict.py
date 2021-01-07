import numpy as np
from keras.models import load_model
from keras.preprocessing import image

class dog_cat_human_horse:
    def __init__(self,filename):
        self.filename =filename


    def predictionclass(self):
        # load model
        model = load_model('model_test.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        result=np.argmax(result,axis=1)

        if result == 1:
            prediction = 'dog'
            return [{ "image" : prediction}]
        elif result == 0:
            prediction = 'cat'
            return [{ "image" : prediction}]
        elif result== 2:
            prediction = 'horse'
            return [{"image": prediction}]
        elif result == 3:
            prediction = 'human'
            return [{"image": prediction}]


