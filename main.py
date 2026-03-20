# ================================
# DROWSINESS DETECTION SYSTEM 🚗😴
# ================================

# Import required libraries
from scipy.spatial import distance as dist
from imutils import face_utils
import imutils
import dlib
import cv2
import winsound   # For alarm sound (Windows only)

# ================================
# ALARM SETTINGS
# ================================
frequency = 2500   # Sound frequency
duration = 1000    # Sound duration (ms)

# ================================
# FUNCTION: Eye Aspect Ratio (EAR)
# ================================
def eye_aspect_ratio(eye):
    """
    Compute the Eye Aspect Ratio (EAR)
    to detect blinking / eye closure
    """
    # Vertical eye distances
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # Horizontal eye distance
    C = dist.euclidean(eye[0], eye[3])

    # EAR formula
    ear = (A + B) / (2.0 * C)
    return ear

# ================================
# INITIAL VARIABLES
# ================================
counter = 0                 # Frame counter
EAR_THRESHOLD = 0.3         # Threshold for eye closure
EAR_CONSEC_FRAMES = 48      # Frames for drowsiness detection

# ================================
# LOAD MODELS
# ================================
shape_predictor_path = "models/shape_predictor_68_face_landmarks.dat"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor_path)

# Get indexes for left & right eye
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# ================================
# START VIDEO STREAM
# ================================
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Resize frame for faster processing
    frame = imutils.resize(frame, width=450)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    rects = detector(gray, 0)

    for rect in rects:
        # Get facial landmarks
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # Extract eye coordinates
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        # Compute EAR for both eyes
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # Average EAR
        ear = (leftEAR + rightEAR) / 2.0

        # Draw eye contours
        cv2.drawContours(frame, [cv2.convexHull(leftEye)], -1, (0, 0, 255), 1)
        cv2.drawContours(frame, [cv2.convexHull(rightEye)], -1, (0, 0, 255), 1)

        # Check if EAR is below threshold
        if ear < EAR_THRESHOLD:
            counter += 1

            if counter >= EAR_CONSEC_FRAMES:
                cv2.putText(frame, "DROWSINESS DETECTED!",
                            (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 0, 255),
                            2)

                # Trigger alarm
                winsound.Beep(frequency, duration)
        else:
            counter = 0

    # Show output frame
    cv2.imshow("Drowsiness Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ================================
# CLEANUP
# ================================
cam.release()
cv2.destroyAllWindows()