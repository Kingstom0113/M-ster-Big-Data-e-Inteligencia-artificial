FROM osrf/ros:noetic-desktop-full

RUN apt-get update && apt-get install -y \
    ros-noetic-turtlebot3 \
    ros-noetic-turtlebot3-gazebo \
    ros-noetic-turtlebot3-fake \
    python3-pip

RUN pip3 install rospy

COPY ros_ManuelSoto.py /root/ros_ManuelSoto.py

CMD ["bash", "-c", "source /opt/ros/noetic/setup.bash && chmod +x /root/ros_ManuelSoto.py && rosrun --prefix='gnome-terminal -- bash -c' /root/ros_ManuelSoto.py"]