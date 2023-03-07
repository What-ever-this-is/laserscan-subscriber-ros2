import rclpy as ros
from rclpy.node import node
from sensor_msgs.msg import LaserScan

laserData = None

class ReadLaser(Node):
    def __init__(self):
        super().__init__('lidarthingy_subscriber')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10
        )
        self.subscription
    def listener_callback(self,msg):
        print("I totally didn't hear something like this %f" % (msg.data[100]))
        laserData = msg

def main(args=None):
    ros.init(args=args)
    reader = ReadLaser()
    ros.spin(reader)
    reader.destroy_node()
    ros.shutdown()

if __name__ == '__main__':
    main()