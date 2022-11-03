from setuptools import setup

package_name = 'my_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ninjaladro',
    maintainer_email='ninjaladro@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = my_controller.TestNode:main",
            "drawCircle = my_controller.draw_circle:main",
            "pose_sub = my_controller.pose_subscriber:main",
            "turtle_controller = my_controller.turtle_controller:main",
            "service_client = my_controller.services_client:main"
        ],
    },
)
