# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:00:30 2024

@author: Esma
"""

from ultralytics import YOLO
import os
import cv2
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
class ObjecTracking:
    def __init__(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        weights_path=os.path.join(dir,'yolov8s.pt')
        self.video_path=os.path.join(dir,'match.mp4')
        self.bytertrack_yaml_path=os.path.join(dir,'bytetrack.yaml')
        self.model=YOLO(weights_path)
        
    def detect_object(self):
        result =self.model.predict(source=self.video_path,show=True,line_width=1)
        
    def track_object(self):
        frame_count=0
        n_frames=1
        image_scale =1
        cap =cv2.VideoCapture(self.video_path)
        
        while True:
            ret,frame =cap.read()
            height,width=frame.shape[:2]
            new_width=round(width/image_scale)
            new_height=round(height/image_scale)
            frame=cv2.resize(frame,(new_width,new_height))
            
            if not ret:
                break
            frame_count +=1
            if frame_count % n_frames != 0:
                continue
            
            result =self.model.track(source=frame,persist=True,tracker=self.bytertrack_yaml_path)
            boxes=result[0].boxes.xyxy.cpu().numpy().astype(int)
            ids =result[0].boxes.id.cpu().numpy().astype(int)
            for box ,id in zip(boxes,ids):
                cv2.rectangle(frame, (box[0],box[1]), (box[2],box[3]),(255,0,255),2)
                cv2.putText(frame,f"Id{id}",(box[0],box[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)
            cv2.imshow("frame", frame)
            if cv2.waitKey(1)& 0xFF == ord("q"):
                break

def run_detect_object():
   ot= ObjecTracking()
   ot.detect_object()
def run_track_object():
    ot= ObjecTracking()
    ot.track_object()

if __name__ == '__main__':
  #run detect object
  run_track_object()           
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                