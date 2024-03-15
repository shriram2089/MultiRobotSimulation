#!/usr/bin/env python3

import os
import roslaunch
import rospkg
import rospy

def main():
    rospy.init_node('my_launch_node', anonymous=True)
    rospack = rospkg.RosPack()
    urdf_bot = os.path.join(rospack.get_path('volta_description'), 'urdf', 'volta.xacro')
    robot_description_cmd = roslaunch.core.Node(
        package='xacro',
        node_type='xacro',
        name='robot_description_cmd',
        args=['--inorder', urdf_bot],
        output='screen'
    )
    empty_world_launch = roslaunch.core.Node(
        package='gazebo_ros',
        node_type='spawn_model',
        name='empty_world_launch',
        respawn=False,
        output='screen',
        args='-urdf -model volta -x 1 -y 1 -z 0 -param robot_description'
    )
    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()
    ld = [robot_description_cmd, empty_world_launch]
    process = launch.launch(ld)
    process.spin()

if __name__ == '__main__':
    main()
