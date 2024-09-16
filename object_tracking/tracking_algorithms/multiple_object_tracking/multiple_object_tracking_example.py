# -*- coding: utf-8 -*-
"""
@author: Esma
"""
import cv2
import time

# OpenCV'deki takip algoritmaları
OPENCV_OBJECT_TRACKERS = {
    "csrt": cv2.legacy.TrackerCSRT_create,
    "kcf": cv2.legacy.TrackerKCF_create,
    "boosting": cv2.legacy.TrackerBoosting_create,
    "mil": cv2.legacy.TrackerMIL_create,
    "tld": cv2.legacy.TrackerTLD_create,
    "medianflow": cv2.legacy.TrackerMedianFlow_create,
    "mosse": cv2.legacy.TrackerMOSSE_create
}

# Takip algoritması adı
tracker_name = "csrt"
trackers = cv2.legacy.MultiTracker_create()

# Video yolu ve FPS
video_path = "MOT17-04-DPM.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video dosyası açılamadı!")
    exit()

fps = 30
f = 0

# Başarı oranı hesaplamak için değişkenler
success_count = 0
total_frame_count = 0

while True:
    # Videonun akış hızını ayarlama
    time.sleep(1 / fps)
    
    ret, frame = cap.read()
    if not ret:
        break

    # Video boyutunu ayarlama
    (H, W) = frame.shape[:2]
    frame = cv2.resize(frame, dsize=(960, 540))

    # Takip algoritmasını güncelle
    (success, boxes) = trackers.update(frame)

    # Toplam kare sayısını artır
    total_frame_count += 1

    # Her kutu için başarı durumunu kontrol et
    if len(boxes) > 0:
        if success:
            success_count += 1

    # Ekranda başarı durumunu göster
    info = [("Tracker", tracker_name),
            ("Success", "Yes" if success else "No")]
    
    string_text = ""
    for (i, (k, v)) in enumerate(info):
        text = "{}:{}".format(k, v)
        string_text += text + " "
    
    cv2.putText(frame, string_text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    
    # Takip edilen kutuları çiz
    if success:
        for box in boxes:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    # Kareyi göster
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # Yeni bir kutu seçmek için 't' tuşuna basın
    if key == ord("t"):
        box = cv2.selectROI("Frame", frame, fromCenter=False)
        if box[2] > 0 and box[3] > 0:  # ROI boyutlarını kontrol et
            tracker = OPENCV_OBJECT_TRACKERS[tracker_name]()
            trackers.add(tracker, frame, box)
    
    # 'q' tuşuna basarak çık
    elif key == ord("q"):
        break

    f += 1

# Video serbest bırakma ve pencereleri kapatma
cap.release()
cv2.destroyAllWindows()

# Başarı oranını hesapla
if total_frame_count > 0:
    success_rate = (success_count / total_frame_count) * 100
    print(f"{tracker_name } Başarı oranı: {success_rate:.2f}%")
else:
    print("Başarı oranı hesaplanamadı, toplam kare sayısı sıfır.")
