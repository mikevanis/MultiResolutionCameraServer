# MultiResolutionCameraServer

This is a demo that captures two video streams from a Pi Camera at multiple resolutions and serves them as .mjpg files through a threaded HTTP server. Part of the [My Naturewatch](https://mynaturewatch.net) project.

## System requirements

- Docker running on Raspbian Stretch
- picamera enabled through raspi-config or similar

## Running the main script

1. Build the Docker container

        docker build -t camserver .

2. Run the container

        docker run --device /dev/vcsm --device /dev/vchiq -p 9090:9090 camserver

3. You can then access the high resolution stream at:

        raspberrypi.local:9090/hrs.mjpg

... and the low resolution stream at:

        raspberrypi.local:9090/lrs.mjpg

Be sure to replace `raspberrypi.local` with whatever hostname the Pi has been given.
