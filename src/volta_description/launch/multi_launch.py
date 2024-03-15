#!/usr/bin/env python3

import rospy
import roslaunch
import os
import rospkg

def spawn_robot(num_bots):
  
    empty_world_launch = roslaunch.parent.ROSLaunchParent(uuid, ["/opt/ros/noetic/share/gazebo_ros/launch/empty_world.launch"])
    empty_world_launch.start()
    
    # Loop through to spawn each robot
    for bot_index in range(num_bots):
        ns = "volta" + str(bot_index)
        ns_sep = "/"
        

        urdf_bot = os.path.join(rospkg.RosPack().get_path('volta_description'), 'urdf', 'volta.xacro')

        robot_description_param = "/{}/robot_description".format(ns)
        urdf_command = "xacro --inorder {}".format(urdf_bot)
        robot_description = os.popen(urdf_command).read().strip()


        spawn_model_node = roslaunch.core.Node(package='gazebo_ros', 
                                                node_type='spawn_model', 
                                                name='spawn_model_{}'.format(bot_index),
                                                args='-urdf -model volta_robot_{} -x {} -y 1 -z 0 -param {}'.format(bot_index, bot_index, robot_description_param),
                                                output='screen')
        launch = roslaunch.scriptapi.ROSLaunch()
        launch.start()
        launch.launch(spawn_model_node)

if __name__ == '__main__':
    rospy.init_node('spawn_multi_robots')
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)

    num_bots = rospy.get_param('~num_bots', 3) # Variable
    spawn_robot(num_bots)
