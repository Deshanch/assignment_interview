# assignment_interview
This is created for an assignment given in an interview process


## Clone this repository 
#### from the current folder :
git clone https://github.com/Deshanch/assignment_interview \
cd assignment_interview \
From here you have to run following commands in assignment_interview 

## Create virtual environment for this project
python3 -m pip --version \
python3 -m pip install --user virtualenv \
python3 -m venv env \
source env/bin/activate

## Install dependencies
pip install -r requirements.txt

## Setup Darknet python interface - YoloV7-tiny
git clone https://github.com/WongKinYiu/yolov7.git \
visit https://github.com/WongKinYiu/yolov7/releases \
Download yolo7-tiny.pt to current folder (./assignment_interview/)

├── app
│   ├── css
│   │   ├── **/*.css
│   ├── favicon.ico
│   ├── images
│   ├── index.html
│   ├── js
│   │   ├── **/*.js
│   └── partials/template
├── dist (or build)
├── node_modules
├── bower_components (if using bower)
├── test
├── Gruntfile.js/gulpfile.js
├── README.md
├── package.json
├── bower.json (if using bower)
└── .gitignore
