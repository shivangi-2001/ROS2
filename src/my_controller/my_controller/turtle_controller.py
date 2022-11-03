#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtleController");
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.pose_subscriber = self.create_subscription(Pose, "/turtle1/pose", self.turtle_callback, 10)
        self.get_logger().info("Turtle Controller has been started")

    def turtle_callback(self, pose: Pose):
        cmd = Twist()
        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
             cmd.linear.x=1.0
             cmd.angular.z=0.9
        else:
            cmd.linear.x= 5.0
            cmd.angular.z= 0.0
        self.cmd_vel_pub_.publish(cmd)



def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__ == '__main__':
    main()
