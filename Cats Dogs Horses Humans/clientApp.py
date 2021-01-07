# Execution will start from clientApp.py.
#from wsgiref import simple_server

from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin

#Suppose if server is available in some other geographical location like australia and from india if you try to hit that
# server, in that case you have to communicate with client and server cross origin or cross regions. That's why we use
# cross_origin. As of now we r trying to execute everything in our local system.

from utils.utils import decodeImage             #Here we have created our own package and we r calling our own class
from predict import dog_cat_human_horse                                          #Again This is our own class

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)                                               #Here we are creating object of the flask
CORS(app)                                                           #CORS is applied for cross origin

#This app object will be responsible for forming this response and request kind of thing in b/w the server.
# It will be responsible for creating the url.



#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"                           # It will store the input image that you wil=l get from UI.
        self.classifier = dog_cat_human_horse(self.filename)                    # That image will be passed inside dogcat.


# Whenever we try to execute the clientApp.py, so it is supposed to show you a webpage and through that webpage
# you will be able to submit your image.So, how system will understand what to show during the time of execution.
# Our system does not know which html page it is supposed to open. Let's see how system understands -
# Flask app is responsible for creating the url. So, whenever it will create the url , on that url which is the
# first page it is supposed to open?

# We can give any thing inside route url whatever we want .

@app.route("/", methods=['GET'])                                  #So, whenever app will try to route or whenever app will try to execute
@cross_origin()                                                    #for the first time, it is supposed to render index.html
def home():
    return render_template('index.html')

# So, whenever we will ry to send(index.html) the data , it will convert the data into base64 and then it will try to call
# predictRoute() .

# Whenever we try to click on predict button in our UI, it will read out the below url

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']                                   # will read the encoded data.
    decodeImage(image, clApp.filename)                               # decoding will return our original image.
    result = clApp.classifier.predictionclass()
    return jsonify(result)                                            # It will capture the result in the json format.

# Then this json result will be passed to this route ->  /predict.
# So, again we are calling this particular html file and here we will be able to see the final responses.

#--------------------------------------------------------------------
# In predictRoute, first we will submit the image, get the prediction and then we will return the final json result which
# you will be able to see in the html page.


#port = int(os.getenv("PORT"))
if __name__ == "__main__":                            #Exexution will start from here as this is our main file.                                                 # Here we are trying to initiate entire clientApp.py file
    clApp = ClientApp()
   # host = '0.0.0.0'
    # port = 5000
    #app.run(host='0.0.0.0', port=port)
    app.run(debug=True)                       # you can give any number as port number.

   # httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host,port))
   # httpd.serve_forever()