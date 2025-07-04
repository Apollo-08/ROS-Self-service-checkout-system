#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from gtts import gTTS
from sound_play.libsoundplay import SoundClient

def main():
    rospy.init_node('tts_node')
    sound = SoundClient()

    def cb(msg):
        text = msg.data
        tts = gTTS(text=text, lang='en')
        path = '/tmp/receipt.mp3'
        tts.save(path)
        sound.playWave(path)

    rospy.Subscriber('/checkout/receipt', String, cb)
    rospy.loginfo("TTS node started.")
    rospy.spin()

if __name__=='__main__':
    main()
