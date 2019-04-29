import cv2
import time
from imutils.video import VideoStream
from imutils.video import FPS

DISPLAY_DIMS = (800, 480)

vs = VideoStream(usePiCamera=True).start()

while True:
	try:
            frame = vs.read()
            image_for_result = frame.copy()
            image_for_result = cv2.resize(image_for_result, DISPLAY_DIMS)
            cv2.imshow("Output", image_for_result)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                    break

	except KeyboardInterrupt:
		break

	except AttributeError:
		pass

cv2.destroyAllWindows()
vs.stop()
