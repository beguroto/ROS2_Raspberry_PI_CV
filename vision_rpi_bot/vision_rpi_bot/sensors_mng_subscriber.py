import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Int16

import RPi.GPIO as GPIO
from time import sleep

class SensorsManagerSubscriber(Node):

    def __init__(self):
        super().__init__('sensors_mng_rpi_subscriber')
        self.subscription = self.create_subscription(
            Int16,
            '/line_following_error',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        #self.error_msg = Int16()
        self.error_msg = 0

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

    def listener_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)

        self.error_msg = msg.data
        print("Delta line: ", self.error_msg)

        
        GPIO.output(self.mr_a, self.error_msg < 0)
        GPIO.output(self.mr_b, self.error_msg < 0)
        GPIO.output(self.ml_a, self.error_msg > 0)
        GPIO.output(self.ml_b, self.error_msg > 0)


def main(args=None):
    rclpy.init(args=args)

    sensors_manager_subscriber = SensorsManagerSubscriber()

    rclpy.spin(sensors_manager_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    sensors_manager_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()