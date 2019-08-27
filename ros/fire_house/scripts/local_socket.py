#!/usr/bin/env python  

import sys, select, termios, tty
import rospy
import math
import tf
import roslib
roslib.load_manifest("rosparam")
import rosparam
import time
import os
#import rospkg

import geometry_msgs.msg
import turtlesim.srv

import socket


def getipaddrs(hostname):
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]



class local_server:
    def __init__(self):

        self.HOST = '192.168.1.100'
        self.PORT = 8001
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.sock.connect((self.HOST, self.PORT))
        try:
            self.sock.connect((self.HOST, self.PORT))
        except :
            print("Connect faild.")
            sys.exit(0)


        self.local_x = 0
        self.local_y = 0

        #print "load param success"
        #self.plocal(format(self.local_x),format(self.local_y))


        self.listener = tf.TransformListener()

    def plocal(self,X,Y):
        print ("**********************************************")
        print ("value:")
        print ("local { x %s , y %s }" % (X,Y))
        time.sleep(0.1)

    def update(self):
        try:
            (trans,rot) = self.listener.lookupTransform('/odom', '/ar_marker_0', rospy.Time(0))
            trans[0] = round(trans[0],2)
            trans[1] = round(trans[1],2)
            self.local_x = trans[0]
            self.local_y = trans[1]
            print ("**********************************************")
            print("find local  x: %f , y: %f " % (trans[0],trans[1]))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print ("local not finded")

        time.sleep(0.1)

    def transfer(self):
        sx = format((int)(self.local_x*10)).zfill(3)
        sy = format((int)(self.local_y*10)).zfill(3)
        self.sock._sock.send(sx+" "+sy)
        #self.plocal(sx,sy)

if __name__ == '__main__':
    rospy.init_node('tf_listener')
    up = local_server()
    while True:
        if not rospy.is_shutdown():
            up.update()
            up.transfer()
        else:
            print "Shutting down"
            sys.exit(0)
