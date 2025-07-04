#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from ultralytics import YOLO

def main():
    rospy.init_node('yolo_detect_node')
    model = YOLO(rospy.get_param('~model_path','models/yolov8n.pt'))
    pub = rospy.Publisher('/detected_items', String, queue_size=1)
    bridge = CvBridge()

    def cb(img_msg):
        img = bridge.imgmsg_to_cv2(img_msg,'bgr8')
        res = model(img)[0]
        counts = {}
        for box in res.boxes.data.cpu().numpy():
            name = res.names[int(box[5])]
            counts[name] = counts.get(name,0)+1
        msg = ','.join(f"{k}:{v}" for k,v in counts.items()) or 'none'
        pub.publish(msg)

    rospy.Subscriber('/camera/image_raw', Image, cb)
    rospy.loginfo("YOLO detection node started.")
    rospy.spin()

if __name__=='__main__':
    main()
