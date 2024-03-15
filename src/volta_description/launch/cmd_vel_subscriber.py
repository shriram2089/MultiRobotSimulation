#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def cmd_vel_subscriber():
    rospy.init_node('cmd_vel_subscriber', anonymous=True)
    rospy.loginfo("Cmd_vel subscriber node started.")

    def callback(msg):
        rospy.loginfo("Received Twist message: linear x=%.2f, angular z=%.2f", msg.linear.x, msg.angular.z)

    rospy.Subscriber('/cmd_vel', Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    cmd_vel_subscriber()
