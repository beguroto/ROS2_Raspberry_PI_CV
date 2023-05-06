import rclpy
from rclpy.node import Node

import cv2 as cv
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

class VideoPublisher(Node):

    def __init__(self):
        super().__init__('rpi_video_publisher')
        self.publisher_ = self.create_publisher(Image, '/surveillance_feed', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.camera_callback)
        self.cap = cv.VideoCapture(0)
        # Ottimizziamo la larghezza di banda occupata
        # Modifichiamo la risoluzione dell'immagine per ridurre la banda occupata
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
        self.bridge = CvBridge()

    def camera_callback(self):
        
        # Capture frame-by-frame
        ret, frame = self.cap.read()

        # Dobbiamo convertire l'immagine OpenCv (OpenCv data) nel formato ROS2 encoding

        # Inviamo le immagini a colori
        #frame = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        
        # Ottimizziamo la larghezza di banda occupata:
        # Convertiamo l'immagine in scala di grigi prima di pubblicarla
        # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #frame = self.bridge.cv2_to_imgmsg(frame, 'mono8')

        frame = self.bridge.cv2_to_imgmsg(frame, 'bgr8')
        self.publisher_.publish(frame)

def main(args=None):
    rclpy.init(args=args)

    video_publisher = VideoPublisher()
    
    print("Nodo VideoPublisher avviato!")
    
    rclpy.spin(video_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    video_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()