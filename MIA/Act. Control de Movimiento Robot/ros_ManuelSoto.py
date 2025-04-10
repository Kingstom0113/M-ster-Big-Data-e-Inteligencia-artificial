#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math

def move_turtlebot():
    rospy.init_node('move_turtlebot', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Movimiento en línea recta
    vel_msg.linear.x = 0.2
    vel_msg.angular.z = 0
    for _ in range(50):
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

    # Giro de 90 grados
    vel_msg.linear.x = 0
    vel_msg.angular.z = math.pi/2
    for _ in range(25):
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

    # Detener el robot
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move_turtlebot()
    except rospy.ROSInterruptException:
        pass