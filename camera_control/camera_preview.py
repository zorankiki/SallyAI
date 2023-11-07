from picamera import PiCamera
import time

camera = PiCamera()
# camera.framerate = 15
# camera.resolution = (800, 600)

#camera.start_preview()
#time.sleep(30)
#camera.stop_preview()

# camera.start_recording('/home/raspberry/Desktop/camera_control/sample_video_1.h264')
# 
# camera.wait_recording(10)
# 
# camera.stop_recording()

camera.start_preview()
time.sleep(10)
# 
# count = 0
# for filename in camera.capture_continuous('./frame_by_frame_2023_11_2_1/img{counter:03d}.jpg'):
#      print('captured %s'%filename)
#      count+=1
#      if count == 20:
#          break
#      time.sleep(.05)
camera.stop_preview()
