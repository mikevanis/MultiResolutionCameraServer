import time
import numpy as np
import picamera
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
from threading import Thread
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from __future__ import print_function

# Multiple resolution setup
camera = PiCamera()
camera.resolution = (1024,768)
camera.framerate = 30
hiResCapture = PiRGBArray(camera)
lowResCapture = PiRGBArray(camera, size=(320,240))
hiResStream = camera.capture_continuous(hiResCapture, format="bgr", use_video_port=True)
lowResStream = camera.capture_continuous(lowResCapture, format="bgr", use_video_port=True, splitter_port=2, resize=(320,240))

time.sleep(0.5)

class CamHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		print(self.path)
		if self.path.endswith("lrs.mjpg"):
			self.send_response(200)
			self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=--jpgboundary')
			self.end_headers()
			print("Serving low res mjpg...")
			while True:
				lrs = lowResStream.next()
				img = lrs.array
				lowResCapture.truncate(0)
				lowResCapture.seek(0)
				r, buf = cv2.imencode(".jpg", img)
				self.wfile.write("--jpgboundary\r\n")
				self.send_header('Content-type', 'image/jpeg')
				self.send_header('Content-length', str(len(buf)))
				self.end_headers()
				self.wfile.write(bytearray(buf))
				self.wfile.write('\r\n')

		if self.path.endswith("hrs.mjpg"):
			self.send_response(200)
                        self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=--jpgboundary')
                        self.end_headers()
                        print("Serving hi res mjpg...")
                        while True:
                                hrs = hiResStream.next()
                                hiresImage = hrs.array
                                hiResCapture.truncate(0)
                                hiResCapture.seek(0)
                                r, buf = cv2.imencode(".jpg", hiresImage)
                                self.wfile.write("--jpgboundary\r\n")
                                self.send_header('Content-type', 'image/jpeg')
                                self.send_header('Content-length', str(len(buf)))
                                self.end_headers()
                                self.wfile.write(bytearray(buf))
                                self.wfile.write('\r\n')

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in separate threads."""

def main():
	try:
		server = ThreadedHTTPServer(('', 9090), CamHandler)
		print("Server started.")
		server.serve_forever()
	except (KeyboardInterrupt, SystemExit):
		camera.close()
		server.socket.close()

if __name__ == '__main__':
	main()
