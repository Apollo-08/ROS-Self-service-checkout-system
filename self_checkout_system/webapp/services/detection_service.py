# webapp/services/detection_service.py

import cv2
from ultralytics import YOLO
import numpy as np

class DetectionService:
    def __init__(self, model_path: str = "yolov8n.pt"):
        self.model = YOLO(model_path)

    def capture_frame(self, cam_index=2):
        cap = cv2.VideoCapture(cam_index)
        ret, frame = cap.read()
        cap.release()
        if not ret:
            raise RuntimeError("CAMERA_ERROR")
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def detect(self, frame_rgb: np.ndarray):
        results = self.model(frame_rgb)
        boxes = results[0].boxes.xyxy.cpu().numpy()
        cls_ids = results[0].boxes.cls.cpu().numpy().astype(int)
        confs = results[0].boxes.conf.cpu().numpy()
        return boxes, cls_ids, confs
