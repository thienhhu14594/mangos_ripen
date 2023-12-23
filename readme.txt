     MANGO RIPENESS LEVEL CLASSIFICATION

I. Desciption
    This project aim to a simple web application to let people upload the
    mango image and classify the ripeness of it. There 3 level of ripeness
    this project archive so far: unripe, partially ripe, and ripe (full ripe)

II. Installation
    1. Clone this app to local repo
    2. Install node js (if haven't installed yet) on computer
    3. Install the following libraries: numpy, ultralytics, opencv
    4. Recommendation on using Anaconda to support creating environment

III. Usage
    1. Run the the web server from terminal in this project directory by
    this command line
        node server.js
    2. From the terminal, an IPv4 adress is given, access to the web from
    browser by the given IPv4 adress (Ex: 192.x.x.x:3000)
    3. Upload the image and the web application will return the result
    detection(image) and the ripeness classification result(if possible)

IV. Configuration
    1. The standart rate to determine the ripe and partially ripe mango can
    be adjusted in the python predict.py, to adjust the rate, please see the
    document in Project(M24)/Mango_Ripeness_Level_Classification/data_color_analysis[1]
    2. The classification model classify.pt and the detection model detect.pt
    can be found in
        Project(M24)/Mango_Ripeness_Level_Classification/classify_model
        Project(M24)/Mango_Ripeness_Level_Classification/detect_model[2]

V. Credit
    Node js, python, numpy, ultralytics, YOLOv8, OpenCv, Anaconda

VI. Acknowledgments
    This project is contribute by Nguyen Duc Huu Thien, Vien Kim Lan,
    and supported by the instructor Dr. Vo Bich Hien

VII. Documentation
    1. [1],[2] The classification and detection trained models, and the color
    determine ratio can be view in
    https://drive.google.com/drive/folders/1rsqHrjEPGc5eLv-1FQ26lAFm-bvWCdnJ?usp=sharing
    2. Extension and libraries
    https://nodejs.org/
    https://www.python.org/
    https://numpy.org/
    https://github.com/ultralytics
    https://opencv.org/
    https://www.anaconda.com/