# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.


## Prep

1.  Pull the new Github Repo.
2.  Read about [OpenCV](https://opencv.org/about/).
3.  Read Belloti, et al's [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.


## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

Befor you get started connect the RaspberryPi Camera V2. [The Pi hut has a great explanation on how to do that](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera).  

#### OpenCV
A more traditional to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python.

Additionally, we also included 4 standard OpenCV examples. These examples include contour(blob) detection, face detection with the ``Haarcascade``, flow detection(a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (I.e. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example.

```shell
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```
#### Filtering, FFTs, and Time Series data. (beta, optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

Include links to your code here, and put the code for these in your repo--they will come in handy later.

#### Teachable Machines (beta, optional)
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple.  However, its simplicity is very useful for experimenting with the capabilities of this technology.

You can train a Model on your browser, experiment with its performance, and then port it to the Raspberry Pi to do even its task on the device.

Here is Adafruit's directions on using Raspberry Pi and the Pi camera with Teachable Machines:

1. [Setup](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/raspberry-pi-setup)
2. Install Tensorflow: Like [this](https://learn.adafruit.com/running-tensorflow-lite-on-the-raspberry-pi-4/tensorflow-lite-2-setup), but use this [pre-built binary](https://github.com/bitsy-ai/tensorflow-arm-bin/) [the file](https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl) for Tensorflow, it will speed things up a lot.
3. [Collect data and train models using the PiCam](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/training)
4. [Export and run trained models on the Pi](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/transferring-to-the-pi)

Alternative less steps option is [here](https://github.com/FAR-Lab/TensorflowonThePi).

#### PyTorch  
As a note, the global Python install contains also a PyTorch installation. That can be experimented with as well if you are so inclined.

### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interactions outputs and inputs.
**Describe and detail the interaction, as well as your experimentation.**

> In this lab, I constructed a detection system for users' emotions by Google's Teachable machines. To be more specific, this is a tool to capture people's reactions while listening to a song or a speech. Based on this, the experiment requires users to open the webcam and play their favored playlist or podcast for at least 20 mins. During this term, they could do anything they would like to, for example, sing with the music or study along with the radio. The expected of the experiment will be the facial expression from users corresponding to the audio input.
>
> Our model includes five emotion categories: Intense, Pleasant, Melancholy, Peaceful, and Engaging. After collecting data from participants, we could label the audio they listened to by one of these emotions.  **As a result, we aim to build an easy way to assess people's reactions corresponding to any kind of audio input.**
>
> The motivation behind this is that the current emotion dataset for songs is mainly based on the music analysis, namely the melody or tempo. However, it's not convincing since the emotion data doesn't come from actual reactions by the audience. Furthermore, when musicians desire to know the exact feelings of listeners, they usually find it's obscured by solely reading the comments. As a solution, we could embed this system into any music or video streaming platforms, enabling creators to collect real user data or form a more accurate emotion database.

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:
For example:

1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

> When the webcam is on, the system will classify the user's facial expression corresponding to the five emotions per frame. Accordingly, there are five bars in the display showing the likelihood in percentage for each emotion that the model determines the user belongs to.
>
> Since the current model had been trained for only a short time, the structure hasn't been optimized, so it bears unstable performance. As a result, there are chances that the trained model assigns an incorrect label to the user's images. By incorrect, it means when the user shows the exact same facial expression, the model couldn't indicate the same emotion as the actual category.
>
> The possible reason behind this might reside in the training dataset. So far, there are around 240 images for each category, so the increases in the number of samples are expected. Besides, the quality of the data might also generate some uncertainties. Particularly, when the sample image for different categories looks much alike, it confuses the model while trying to learn a way to distinguish during the training phase.
>
> Moreover, because of the observed inaccuracy of the system, it's reasonable to doubt that when the user's environment changes, for example, the background or the brightness, the accuracy might drop even worse. In addition, once there are items blocking the user's face, or the image doesn't cover the whole face, the model will not function properly either.        

**Think about someone using the system. Describe how you think this will work.**

1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

> It is possible that users will be aware of the inconsistency or the inaccuracy of the system once the output category doesn't match their real feelings. Ideally, they won't be affected by the misclassification since they might be doing other stuff instead of paying attention to the system output. Even though they notice the unexpected return from the model, it's totally fine for them to ignore it and keep acting naturally.
>
> However, in the worst case, participants get confused by the misclassification and possibly try to behave according to the model output in return. This interaction is actually the worst since it biased the user's behavior, which conflicts with the original system design. In other words, we only expect to observe people's reactions but not influence their actions.
>
> To address this issue, one way is to improve accuracy by increasing the variance in the training dataset, for example, to include images from different people with different backgrounds, or of varying brightness. By doing so, the model will gain the capability to accommodate more various scenarios and produce accurate classifications.
>
> Regarding the sense-making algorithm, one improvement could be generalizing the category a bit, for example, having broader emotion categories such as happy, angry, and sad. There are two advantages; first of all, it will be easier for the model to distinguish between different emotions. Secondly, the output could describe people's feelings at a higher level, which in other words, leads to less confusion of users.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:

* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**Include a short video demonstrating the answers to these questions.**
[![Demo](http://img.youtube.com/vi/nSvxlUTeS_c/0.jpg)](http://www.youtube.com/watch?v=nSvxlUTeS_c "Demo")

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**Include a short video demonstrating the finished result.**
[![Final Demo](http://img.youtube.com/vi/Eu1ujFYFpl4/0.jpg)](http://www.youtube.com/watch?v=Eu1ujFYFpl4 "Final Demo")
