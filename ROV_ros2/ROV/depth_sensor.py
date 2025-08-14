#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from std_msgs.msg import Float32
import random
import time

class Depth_sensor(Node): 

    def __init__(self):
        super().__init__("publish_depth") #node name initialization
        self.publisher_ = self.create_publisher(Float32,'/depth',10) 
        #node will publish Float data type to depth topic (10 is number of message that can wait if subscriber is slow)
        self.timer = self.create_timer(1.0,self.timer_callback)
        #send reading cont. "calls timer_callback each sec"

    def timer_callback (self):
        depth = random.uniform (0.0,10.0) #random value from 0 to 10
        msg = Float32()
        msg.data = depth #fill msg with reading
        self.publisher_.publish (msg)
        self.get_logger().info(f'Depth = {depth:.3f} meters')


    
def main (args=None):
    rclpy.init(args=args)
    #call node
    node = Depth_sensor()
    try: 
        rclpy.spin(node)
    except KeyboardInterrupt: pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main() # useful for executing from terminal
