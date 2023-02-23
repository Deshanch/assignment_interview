# importing the required libraries
import os
from flask import Flask, render_template, request, send_file, redirect
from werkzeug.utils import secure_filename
from PIL import Image

"""
This system has the capability of uploading a image from a local machine and download the detected image to the local storage

Use YOLO V7 - tiny for object detection
"""

app = Flask(__name__)

# Creating the upload folder
upload_folder = "uploads/"
if not os.path.exists(upload_folder):
   os.mkdir(upload_folder)

# Max size of the file of uploading
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

# Configuring the upload folder
app.config['UPLOAD_FOLDER'] = upload_folder

# allowed extensions of image uploading
allowed_extensions = ['jpg', 'png', 'pdf']

def check_file_extension(filename):
    return filename.split('.')[-1] in allowed_extensions

# The path for uploading the file
@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/upload', methods = ['POST'])
def uploadfile():
   if request.method == 'POST':
      f = request.files['file']
      # Saving the file
      if check_file_extension(f.filename):
         f.save(os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename("detect.jpg"))) # this will secure the file
         return redirect('/')
      else:
         return 'The file extension is not allowed'

# Sending the file to the user
@app.route('/detect')
def detect():

   # remove files and folders that save previously detected images to remove conflicts
   try:
      os.remove("./runs/detect/exp/detect.jpg")
   except OSError as error:
      print(error)
   try:
      os.rmdir("./runs/detect/exp")
   except OSError as error:
      print(error)
 
   # run terminal command to call to darknet interface - have to run locally 
   try:
      os.system("python yolov7/detect.py --weights yolov7-tiny.pt --source uploads/detect.jpg")
      return redirect('/')
   except:
      return 'The detection failed'   


# Sending the file to the user
@app.route('/download')
def download():
   try:
      return send_file('runs/detect/exp/detect.jpg', as_attachment=True)    
   except:
      return 'Error with downloading'       
		
if __name__ == '__main__':
   app.run(debug=True) # running the flask app