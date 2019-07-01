FROM sgtwilko/rpi-raspbian-opencv:stretch-latest

# Install python requirements
RUN pip install picamera

# Bundle source
COPY . .

# Expose port
EXPOSE 9090

# Run
CMD ["python", "MultiResolutionCameraServer.py"]
