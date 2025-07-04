#!/usr/bin/env python3
import os
import sys
import rospy
from std_msgs.msg import String

# 手动添加 scripts 到模块路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from price_config import PRICES

def main():
    rospy.init_node('checkout_logic_node')
    pub = rospy.Publisher('/checkout/receipt', String, queue_size=1)

    def cb(msg):
        data = msg.data
        if data == 'none':
            return
        total = 0.0
        details = []
        for part in data.split(','):
            name, cnt_str = part.split(':')
            cnt = int(cnt_str)
            price = PRICES.get(name, 0.0)
            subtotal = price * cnt
            total += subtotal
            details.append(f"{name} x{cnt} @ {price:.2f} = {subtotal:.2f}")
        receipt = "; ".join(details) + f"; Total = {total:.2f}"
        rospy.loginfo(f"Receipt: {receipt}")
        pub.publish(receipt)

    rospy.Subscriber('/detected_items', String, cb)
    rospy.loginfo("Checkout logic node started.")
    rospy.spin()

if __name__=='__main__':
    main()
