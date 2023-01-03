# Simple Face Detection 
![img](https://user-images.githubusercontent.com/102472934/210349737-dcaefcde-899a-4581-a1ae-248afb0839fb.gif)

## Goal of this Script
This Script will detect only the frontal faces in a video or the faces that are in front of the opened camera.
> The required and used library in this script is a computer vision library called [OpenCV](https://opencv.org/).

Download the library by typing this line in the command prompt
```
pip install opencv-python
```
> Alternatively, if you are working in an Anaconda environment, you can open the Anaconda PowerShell prompt, copy and paste this line, and hit enter
```
conda install -c conda-forge opencv
```
## Note
If you are using the regular version of Python, you may encounter issues with autocomplete or the IDE you are using may highlight the cv2 module attributes, functions or methods. However, the code will still work without any issues. If you are experiencing this problem, you can try using the Anaconda environment and specifying the path of the classifier that you are using. This has worked for me without any issues.

## Modify the code to meet your main needs from the program
• You can modify which camera you want to use by changing the parameter of ```cv2.VideoCapture(0)``` to the camera number you want. In this case, I am using a laptop and the default camera number is always 0. However, if you have multiple cameras connected to your device, you can specify a different camera by using its corresponding number. For example, if you want to use the second camera, you can use ```cv2.VideoCapture(1)```.

• If you want to detect faces in a video, you can modify the parameter of cv2.VideoCapture(0) to the name of the video file in the project directory. 
For example, if you have a video called "yoga.mp4" and you want to detect the faces in this video, you can change the parameter of ```cv2.VideoCapture(0)``` to ```cv2.VideoCapture("yoga.mp4")``` This will allow the script to use the video file as the input for face detection.

• The script will run in an infinite loop until you press the 'q' key on your keyboard.

## Some warnings and information you should know
• This script may generate random or inaccurate squares in your camera/video or may not detect some faces, or encounter other errors, as it is not professionally written. I am not an expert in using the OpenCV library, so the script may not be of high quality. However, it should still meet your minimum needs for a simple project that involves computer vision.

• However, there are various factors that can contribute to these inaccuracies. Some of these may include:
  1. The quality of the video or camera input
  2. The accuracy of the classifier used for face detection
  3. The lighting conditions and other environmental factors
  4. The processing power of the device being used
  5. The configuration and optimization of the script

# Finally 
I wanted to take a moment to thank you for taking the time to read and view this project. Your interest and attention are greatly appreciated. It means a lot to me that you took the time to learn more about what I have created.
Thank you again for your support. I hope you found the project informative and enjoyable.

Sincerely,

Mahmoud Dello
