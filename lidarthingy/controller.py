import RPi.GPIO as g
import rclpy as ros
from rclpy.node import Node

class Drivetrain():
    def __init__(self,ena,enb,in1,in2,in3,in4):
        g.setmode(g.BOARD)
        self.ena = ena
        self.enb = enb
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        g.setup(self.ena,g.OUT)
        g.setup(self.enb,g.OUT)
        g.setup(self.in1,g.OUT)
        g.setup(self.in2,g.OUT)
        g.setup(self.in3,g.OUT)
        g.setup(self.in4,g.OUT)
        self.motors = [
            g.PWM(self.ena,1000),
            g.PWM(self.enb,1000)
        ]
        g.output(self.in1,g.LOW)
        g.output(self.in2,g.LOW)
        g.output(self.in3,g.LOW)
        g.output(self.in4,g.LOW)
        self.motors[0].start(100)
        self.motors[1].start(100)
    def setspeed(self,motor,speed):
        self.motors[motor-1].ChangeDutyCycle(speed)
    def changedirection(self,motor=1,forward=True):
        if(forward):
            if(motor == 1):
                g.output(self.in1,g.HIGH)
                g.output(self.in2,g.LOW)
            else:
                g.output(self.in3,g.HIGH)
                g.output(self.in4,g.LOW)
        else:
            if(motor == 1):
                g.output(self.in1,g.LOW)
                g.output(self.in2,g.HIGH)
            else:
                g.output(self.in3,g.LOW)
                g.output(self.in4,g.HIGH)
    def stop(self,motor):
        if(motor==1):
            g.output(self.in1,g.LOW)
            g.output(self.in2,g.LOW)
        else:
            g.output(self.in3,g.LOW)
            g.output(self.in4,g.LOW)


class ControllerNode(Node):
    def __init__(self):
        super().__init__("controller_node")
        self.get_logger().info("You ran the controller.py")
        self.get_logger().info("Creating Drivetrain...")
        drivetrain = Drivetrain(11,12,13,15,16,18)
        drivetrain.changedirection(1,1)
        drivetrain.changedirection(2,1)


def main(args=None):
    ros.init(args=args)
    node = ControllerNode()

    ros.shutdown()   

if __name__ == '__main__':
    main()