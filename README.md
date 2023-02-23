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
Download yolo7-tiny.pt to current folder \

## Folder structure looks like

├── assignment_interview \
│   ├── env \
│   ├── templates \
│   ├── yolov7 \
│   ├── .gitignore \
│   ├── app.py \
│   ├── README.md \
│   ├── requirements.txt \
│   ├── traced_model.pt \
│   └── yolov7-tiny.pt

## Finally run 

python app.py
