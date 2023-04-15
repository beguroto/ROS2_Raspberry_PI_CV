import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

import RPi.GPIO as GPIO
import time

class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('cmd_rpi_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_to_pwm_callback,
            10)
        #self.subscription  # prevent unused variable warning

        #Pin gestione motori
        right_motor_a = 24
        right_motor_b = 23
        right_motor_en = 25

        left_motor_a = 17
        left_motor_b = 27
        left_motor_en = 22

        GPIO.setmode(GPIO.BCM)
        #GPIO.setmode(GPIO.BOARD)
        
        GPIO.cleanup()

        GPIO.setup(right_motor_a, GPIO.OUT)
        GPIO.setup(right_motor_b, GPIO.OUT)
        GPIO.setup(right_motor_en, GPIO.OUT)

        GPIO.setup(left_motor_a, GPIO.OUT)
        GPIO.setup(left_motor_b, GPIO.OUT)
        GPIO.setup(left_motor_en, GPIO.OUT)

        self.pwr_r = GPIO.PWM(right_motor_en, 1000)
        self.pwr_l = GPIO.PWM(left_motor_en, 1000)

        #Creiamo gli oggetti che seguono
        #Non possiamo usare il self direttamente sulla definizione dei pin
        self.pwr_r.start(75)
        self.pwr_l.start(75)

        self.mr_a = right_motor_a
        self.mr_b = right_motor_b
        self.ml_a = left_motor_a
        self.ml_b = left_motor_b

    def cmd_to_pwm_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)

        right_wheel_vel = (msg.linear.x + msg.angular.z)/2
        left_wheel_vel = (msg.linear.x - msg.angular.z)/2

        print(right_wheel_vel, " / ", left_wheel_vel)

        GPIO.output(self.mr_a, right_wheel_vel > 0)
        GPIO.output(self.mr_b, right_wheel_vel < 0)
        GPIO.output(self.ml_a, left_wheel_vel > 0)
        GPIO.output(self.ml_b, left_wheel_vel < 0)

def main(args=None):
    rclpy.init(args=args)

    velocity_subscriber = VelocitySubscriber()

    rclpy.spin(velocity_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    GPIO.cleanup()
    velocity_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()