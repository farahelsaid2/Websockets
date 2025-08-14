#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from std_msgs.msg import Float32
import asyncio
import websockets

connected_devices = set()

async def websocket_handler(websocket, path): 
    #first parameter to send or recieve from front end
    #second parameter is the edited if there is diff devices connected
    connected_devices.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        connected_devices.remove(websocket)
        #try waits until device is disconnected and finally remove device 

async def broadcast (message):
    if connected_devices:
        await asyncio.wait([device.send(message) for device in connected_devices])
        #await waits until all msg are sent 
        #asyncio.wait sends to all devices at same time
        
class Depth_sub(Node):
    def __init__(self):
        super().__init__('depth_subscriber')
        self.subscription = self.create_subscription(Float32,'/depth',self.listener,10)

    def listener(self,msg):
        self.get_logger().info(f"Recieved {msg.data:.3f} meters")
        asyncio.create_task(broadcast(str(msg.data)))



def main(args=None):
    rclpy.init(args=args)
    node=Depth_sub()
    start = websockets.serve(websocket_handler,'10.0.2.15', 8765)
    asyncio.get_event_loop().run_until_complete(start)
    #start server

    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt: pass
    finally:
     node.destroy_node()
     rclpy.shutdown()
    
if __name__ == '__main__':
    main ()
 