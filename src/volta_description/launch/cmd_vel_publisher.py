#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def cmd_vel_publisher():
    rospy.init_node('cmd_vel_publisher', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    rospy.loginfo("Cmd_vel publisher node started.")

    while not rospy.is_shutdown():
        
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = 0.5  
        cmd_vel_msg.angular.z = 0.2  


        pub.publish(cmd_vel_msg)

        rospy.loginfo("Published Twist message: linear x=%.2f, angular z=%.2f", cmd_vel_msg.linear.x, cmd_vel_msg.angular.z)

        rate.sleep()

if __name__ == '__main__':
    try:
        cmd_vel_publisher()
    except rospy.ROSInterruptException:
        pass
