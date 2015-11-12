#!/usr/bin/env python
import roslib; roslib.load_manifest('ardrone_1')
import rospy


from geometry_msgs.msg import Twist
from std_msgs.msg import Empty       	 # for land/takeoff/emergency
from ardrone_autonomy.msg import Navdata # for receiving navdata feedback

def despegar():
    rospy.init_node('ardrone_1')
    pubTakeoff = rospy.Publisher('/ardrone/takeoff',Empty)
    rospy.sleep(1) 
    rospy.loginfo("Take off...")
    pubTakeoff.publish(Empty())
    rospy.sleep(3) 



def roll(x):
    
    pubMove = rospy.Publisher('cmd_vel', Twist)

    twist=Twist()
    rospy.sleep(1)
    if (x<>0):
      	twist.linear.x=1
      	pubMove.publish(twist)
      	rospy.sleep(abs(x))

def pitch(y):
   
    pubMove = rospy.Publisher('cmd_vel', Twist)

    twist=Twist()
    rospy.sleep(1)
    if (y<>0):
      	twist.linear.y=y/abs(y)
      	pubMove.publish(twist)
      	rospy.sleep(abs(y))

def velocidad_z(z):
   
    pubMove = rospy.Publisher('cmd_vel', Twist)

    twist=Twist()
    rospy.sleep(1)
    if (z<>0):
      	twist.linear.z=z/abs(z)
      	pubMove.publish(twist)
      	rospy.sleep(abs(z))

def aterrizar():
    pubLand = rospy.Publisher('/ardrone/land',Empty)
    pubMove = rospy.Publisher('cmd_vel', Twist)

    twist=Twist()
    twist.linear.z=0;
    pubMove.publish(twist)
    rospy.sleep(1)
    
    rospy.loginfo("Land...")
    pubLand.publish(Empty())
    rospy.sleep(3)

def ruta():
    despegar()
	roll(4)
    aterrizar()
    

if __name__ == '__main__':
    try:
        ruta()
    except rospy.ROSInterruptException: pass
