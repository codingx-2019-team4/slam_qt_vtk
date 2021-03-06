#!/usr/bin/env python  

import sys, select, termios, tty
import rospy
import math

import roslib
roslib.load_manifest("rosparam")
import rosparam
import time
import os
#import rospkg

import geometry_msgs.msg
import turtlesim.srv

import socket

import rospy 
import rospkg 
from gazebo_msgs.msg import ModelState

from gazebo_msgs.srv import GetModelState 

#from gazebo_msgs.srv import Set

import sys

sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')




def getipaddrs(hostname):
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]



class local_server:
    def __init__(self):

        self.HOST = '172.20.10.7'
        self.PORT = 8004
        self.conn =None
        self.sock = socket.socket()
        try:
            print ('Connectting ')
            self.sock.bind((self.HOST, self.PORT))
            self.sock.listen(10)
            #self.sock.connect(self.HOST, self.PORT)
            self.conn, self.addr = self.sock.accept()
            print ('Connected by ', self.addr)
            print ('Connected by ', self.conn)
        except :
            print("Connect faild.")
            sys.exit(0)


        self.local_x = 0
        self.local_y = 0

        #print "load param success"
        #self.plocal(format(self.local_x),format(self.local_y))


        

    def plocal(self,X,Y):
        print ("**********************************************")
        print ("value:")
        print ("local { x %s , y %s }" % (X,Y))
        time.sleep(0.1)

    def update(self):
        try:
            self.model_coordinates = rospy.ServiceProxy( '/gazebo/get_model_state', GetModelState)
            self.state_msg = self.model_coordinates("dog2", "world")
            self.local_x = round(self.state_msg.pose.position.x,4)
            self.local_y = round(self.state_msg.pose.position.y,4)

            print ("**********************************************")
            #print("find local  x: %f , y: %f " % (trans[0],trans[1]))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print ("local not finded")

        time.sleep(0.1)

    def transfer(self):
        if(self.local_x>0):
       	    sx = "+"+format((int)(self.local_x*100)).zfill(4)
        else:
            sx = format((int)(self.local_x*100)).zfill(5)
        if(self.local_y>0):
       	    sy = "+"+format((int)(self.local_y*100)).zfill(4)
        else:
            sy = format((int)(self.local_y*100)).zfill(5)

        tran = sx+" "+sy

        message_to_send = tran.encode("UTF-8")
        self.conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
        self.conn.send(message_to_send)
        print(tran)


if __name__ == '__main__':
    rospy.init_node('tf_listener')
    up = local_server()
    while True:
        if not rospy.is_shutdown():
            up.update()
            up.transfer()
        else:
            print ("Shutting down")
            sys.exit(0)
