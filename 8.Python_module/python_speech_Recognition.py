"""
Speech recognition (Python package)
Summary
Python library to connect to several speech recognition APIs, including CMU Sphinx, Google Cloud, Wit.ai, … . It can be used for stream processing (in “real-time” with automatic detection of end according to the API) or for batch processing, both with synchronous speech recognition (response as soon as it is processed) for short audio sequences and asynchronous speech recognition (for larger files).

Below, we explain how to make it work with two particular speech recognition APIs, namely CMU Sphinx and the Google API. Let us quickly compare their pros and cons:

Note

We found the google API to be very precise straight out of the box. Sphinx performance very poor and was close to non-usuable without a grammar definition (explained in detail below) and good with a grammar.



pip install SpeechRecognition


Hardware requirements
microphone, e.g. the internal microphone of the Kinect
Software requirements
installed microphone drivers, e.g. as part of the Kinect drivers
PyAudio (specifically considered as part of the installation procedure below)

The library requires PyAudio as a dependency (and PyAudio’s dependencies) in order to use real-time microphone input. The pip installation procedure should install PyAudio automatically, but the pip full pip installation is as of the date of this writing broken and might still be when used in the future. Note that a simple pip install pyaudio does not work. To resolve this, please follow the steps of the setup test below. If the output is correct, PyAudio has been installed correctly and you can jump to the next step. However, if the output is an error message indicating something similar to
AttributeError: Could not find PyAudio; check installation
then PyAudio has not been installed correctly and you have to follow the following steps:

a) Install several further dependencies of PyAudio manually by executing sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg libav-tools. b) Now, install PyAudio manually by executing pip install pyaudio. c) As a final step, re-run the setup test below and give Fezzik a hand for documenting all this struggle.
Now let’s install further dependencies for the underlying APIs. Note that you can install either the Google API or CMU Sphinx; they are independent.

Google Cloud API for speech recognition
Some useful links to start: * Documentation: https://cloud.google.com/speech/docs/ * Overview of Google speech recognition API: https://cloud.google.com/speech/

Follow the steps under https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account to create a service account. To do so, you need a Google account and have to provide billing information (a working credit card).
At the end of this process, you should get a so-called service account key which is a .json file. You will need the content of this key for the speech recognition package. Store it in a location on your local machine (don’t share it via git, since it can be used to access the API).
Note

You only have to setup an API key and activate the service once. You can use it later on other machines, thus, you can skip this first step in such a case.

Install the python API client (assuming you are using python) by executing
$ pip install --upgrade google-api-python-client


Install the python API client (assuming you are using python) by executing
$ pip install --upgrade google-api-python-client
How to setup the CMU Sphinx package
$ sudo apt-get install python3 python3-all-dev python3-pip build-essential swig git libpulse-dev
$ pip3 install pocketsphinx
Setup test
This is a setup test for the speech recognition package only.

Run the demo program by executing: python -m speech_recognition
This should start a demo program which, if correct, outputs something similar to:

Say something!
Got it! Now to recognize it...
You said hello hello
Say something!
Got it! Now to recognize it...
Oops! Didn't catch that


"""
import speech_recognition as sr
# print(sr.__version__)
r = sr.Recognizer()
# r.recognize_google()
mic=sr.Microphone()
try:
    with mic as source:
        print("Listening..")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    query=r.recognize_google(audio,language="en-US")
    print(f'User said:\n {query}')
    print("Thanks you man")
except Exception as e:
    print("This is Exception occurs")
    print(e)

print(sr.Microphone.list_microphone_names())

