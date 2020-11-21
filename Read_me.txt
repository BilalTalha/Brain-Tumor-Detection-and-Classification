Annotations:
Download annotator from link given below
https://tzutalin.github.io/labelImg/

Detection:
After preparing your annotations run the detection code present on link given below
https://github.com/BilalTalha/Car-game/blob/master/Copy_of_Untitled4.ipynb
Samples of output will be present in notebook
For your own data only give link of your data in given line below in the code
"!wget https://github.com/BilalTalha/Car-game/raw/master/Braintumor.zip"

Cropping:
Crop the detected region using code in cropping.py
You will be able to do it one by one

DWT:
Apply DWT and extract features by running DWT.m
\\\\\\\\\\\\\\\\\\\\\\\\
D = 'C:\Users\Talha Bilal\Desktop\New folder (3)\cropped';
fileID = fopen('C:\\Users\\Talha Bilal\\Desktop\\New folder (3)\\menigiomia.txt','w');
\\\\\\\\\\\\\\\\\\\\\\\\\
You have to give link to your own dataset folder in first line
In 2nd line you give link where the extracted features will be stored

SVM:
Run the code in svm.py for classification by placing the path of featrues file in line 41 