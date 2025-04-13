import mediapipe as mp

class FallDetector:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.landmarks = None

    def detect_pose(self, frame_rgb):
        results = self.pose.process(frame_rgb)
        self.landmarks = results.pose_landmarks
        return self.landmarks

    def is_fall_detected(self):
        if not self.landmarks:
            return False

        lm = self.landmarks.landmark
        shoulder_y = lm[self.mp_pose.PoseLandmark.LEFT_SHOULDER].y
        hip_y = lm[self.mp_pose.PoseLandmark.LEFT_HIP].y
        knee_y = lm[self.mp_pose.PoseLandmark.LEFT_KNEE].y

        # Logic: all 3 landmarks in near-horizontal line
        if abs(shoulder_y - hip_y) < 0.1 and abs(hip_y - knee_y) < 0.1:
            return True
        return False
