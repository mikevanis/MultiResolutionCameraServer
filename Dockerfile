FROM sgtwilko/rpi-raspbian-opencv:stretch-latest

# Install python requirements
RUN pip install picamera
RUN pip3 install picamera

# Bundle source
COPY . .

# Expose port
EXPOSE 9090

# Run
CMD ["python3", "MultiResolutionCameraServer.py"]
