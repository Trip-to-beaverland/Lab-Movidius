import cv2
import time
from imutils.video import VideoStream
from imutils.video import FPS

#DISPLAY_DIMS = (800, 480)

#vs = VideoStream(usePiCamera=True).start()
#vs = cv2.imread('/home/pi/Lab-Movidius/sample_img/doge.jpg')
vs = cv2.VideoCapture('videoplayback.mp4')
time.sleep(1)
fps = FPS().start()

# loop over frames from the video file stream
while (vs.isOpened()):
    start_time = time.time()
    ret, frame = vs.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fr_ps = time.time()-start_time
    txt = 'FPS:' + str(1/fr_ps)
    cv2.putText(gray, txt, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vs.release()
# stop the FPS counter timer
fps.stop()

# destroy all windows if we are displaying them

cv2.destroyAllWindows()

# stop the video stream
#vs.stop()

# display FPS information
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))