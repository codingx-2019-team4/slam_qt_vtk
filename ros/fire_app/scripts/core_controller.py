#!/usr/bin/python

#reference http://wiki.ros.org/roslaunch/API%20Usage

import roslaunch
import rospy
import rospkg

#get pkg dir & get to param
rospack = rospkg.RosPack()

dirpath_core = rospack.get_path('fire_app')

class core_control:
    def __init__(self):
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)

        rospy.set_param('start_mapping', 1)
        
        self.mapping_launch = roslaunch.parent.ROSLaunchParent(uuid, [dirpath_core+"/launch/fack.launch"])
        self.mapping_launch_already = 0



    def update(self):
        if rospy.get_param('start_mapping')==1:
            #rospy.sleep(0.5)
            if self.mapping_launch_already == 0:
                rospy.sleep(0.3)
                self.mapping_launch.start()
                self.mapping_launch_already = 1
                rospy.loginfo("slam started")
            else:
                rospy.loginfo("slam have already launched")
                rospy.sleep(0.3)

        else:
            if self.mapping_launch_already == 1:
                rospy.sleep(0.3)
                self.mapping_launch.shutdown()
                self.mapping_launch_already = 0
                self.init_again()
                rospy.loginfo("slam closed")
            else:
                rospy.loginfo("slam have already closed")
                rospy.sleep(0.3)

      

if __name__ == '__main__':
    rospy.init_node('Core_controller', anonymous=False)
    core = core_control()
    while True:
        if not rospy.is_shutdown():
            core.update()
        else:
            print "Shutting down"
            sys.exit(0)
