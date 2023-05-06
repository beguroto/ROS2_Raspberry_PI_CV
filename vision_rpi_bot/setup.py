from setuptools import setup
import os
from glob import glob

package_name = 'vision_rpi_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='as',
    maintainer_email='as@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'publisher_rpi_node = vision_rpi_bot.publisher:main',
                'subscriber_rpi_node = vision_rpi_bot.subscriber:main',
                'cmdVel_to_pwm_node = vision_rpi_bot.cmd_to_pwm_driver:main',
                'image_publisher_gry_node = vision_rpi_bot.image_publisher_gry:main',
                'image_publisher_rgb_node = vision_rpi_bot.image_publisher_rgb:main',
                'sensors_mng_subscriber_node = vision_rpi_bot.sensors_mng_subscriber:main',
                            ],
                },
)
