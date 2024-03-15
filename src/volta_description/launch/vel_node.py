#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState
import rospkg
import os

def spawn_robot():
    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_model_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

        rospack = rospkg.RosPack()
        urdf_bot = os.path.join(rospack.get_path('volta_description'), 'urdf', 'volta.xacro')
        
        model_state = ModelState()
        model_state.model_name = 'volta_robot'
        model_state.reference_frame = 'world'
        model_state.pose.position.x = 1
        model_state.pose.position.y = 1
        model_state.pose.position.z = 0

        with open(urdf_bot, 'r') as file:
            model_state.model_xml = file.read()

        resp = set_model_state(model_state)
        if resp.success:
            rospy.loginfo("Robot spawned successfully")
        else:
            rospy.logerr("Failed to spawn robot")

    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

def publish_velocity():
    pub = rospy.Publisher('/volta_robot/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velocity_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        vel_msg = Twist()
        vel_msg.linear.x = 0.5  # Linear velocity in the x-axis (m/s)
        vel_msg.angular.z = 0.1  # Angular velocity around the z-axis (rad/s)
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        spawn_robot()
        publish_velocity()
    except rospy.ROSInterruptException:
        pass
