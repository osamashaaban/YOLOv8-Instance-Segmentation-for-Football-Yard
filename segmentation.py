from ultralytics import YOLO
import os

os.chdir(r"D:\ITI\CV Projects\Segmentation")
model = YOLO("../best.pt")
model.predict(source='goal.mp4',save=True, show=True, conf=0.25)
