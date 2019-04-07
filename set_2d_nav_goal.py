#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped

def set_pose_stamped():
    pose = PoseStamped()
    ## Header
    pose.header.stamp = rospy.Time.now()
    pose.header.frame_id = "odom"
    
    ## Position
    pose.pose.position.x = -0.7
    pose.pose.position.y = 14.0
    pose.pose.position.z = 0.00

    ## Orientation
    #quaternion = tf.transformations.quaternion_from_euler(0, 0, self.theta)
    pose.pose.orientation.x = 0
    pose.pose.orientation.y = 0
    pose.pose.orientation.z = 0
    pose.pose.orientation.w = 1

    return pose

def set_goal_pos():
    pub = rospy.Publisher('/move_base_simple/goal',PoseStamped,queue_size=10)
    rospy.init_node('set_goal_pos', anonymous=True)
    p = 0
    rospy.loginfo("Setting goal position")
    rate = rospy.Rate(10)
    #while not rospy.is_shutdown():
    while (p < 20):
        pose = set_pose_stamped()

        pub.publish(pose)
        p = p + 1
        rate.sleep()

if __name__ == '__main__':
    try:
        set_goal_pos()
    except rospy.ROSInterruptException:
        pass

