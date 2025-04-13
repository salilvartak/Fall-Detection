import cv2
from fall_detector import FallDetector
from utils import draw_landmarks

def main():
    detector = FallDetector()
    cap = cv2.VideoCapture(1)

    print("[INFO] Fall Detection System initialized. Press 'q' to quit.\n")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("[ERROR] Failed to capture frame.")
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        landmarks = detector.detect_pose(frame_rgb)

        if landmarks:
            draw_landmarks(frame, landmarks)
            if detector.is_fall_detected():
                cv2.putText(frame, "FALL DETECTED!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1.2, (0, 0, 255), 3)
                print("[ALERT] Fall detected! Please check the camera feed immediately.")

        cv2.imshow("Fall Detection System", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            print("\n[INFO] Exiting Fall Detection System.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
