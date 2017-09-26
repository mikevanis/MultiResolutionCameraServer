# MultiResolutionCameraServer

This is a unit test that captures two video streams from a Pi Camera at multiple resolutions and serves them as .mjpg files through a threaded HTTP server. Part of the Naturewatch project in collaboration with the Royal College of Art.

## System requirements

- OpenCV 3.1.0 or higher, as well as contrib modules.
- Python 2.7
- picamera + array variant
- Raspberry Pi 3 or Zero W
- Pi Camera module
- 16GB SD card

## Running the main script

Simply run the script with Python.

        python MultiResolutionCameraServer.py

You can then access the high resolution stream at:

        raspberrypi.local:9090/hrs.mjpg

... and the low resolution stream at:

        raspberrypi.local:9090/lrs.mjpg

Be sure to replace `raspberrypi.local` with whatever hostname the Pi has been given. 
