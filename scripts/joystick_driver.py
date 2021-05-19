#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from jetbot_ros.msg import motor_drive_input


class joystick_driver:
    def __init__(self):
        rospy.init_node("joystick_driver")
        self.pub = rospy.Publisher("~/cmd_raw", motor_drive_input, queue_size=1)
        self.sub = rospy.Subscriber("/joy", Joy, self.callback, queue_size=1)

    def callback(self, data):
        rospy.loginfo("speed- = [%f, %f]" % (data.axes[1], data.axes[4]))
        msg = Float32Array()
        msg.data = [data.axes[1], data.axes[4]]
        self.pub.publish(msg)

    def listen(self):
        rospy.spin()


def main():
    driver = joystick_driver()
    driver.listen()


if __name__ == '__main__':
    main()
