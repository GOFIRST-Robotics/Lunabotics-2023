from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    joystick_node = Node(
        package="joy",
        executable="joy_node",
        parameters=["config/joy_node.yaml"],
    )

    rovr_control = Node(
        package="rovr_control",
        executable="main_control_node",
        name="main_control_node",
        parameters=["config/rovr_control.yaml"],
        output="screen",
        emulate_tty=True,
    )

    motor_control = Node(
        package="motor_control",
        executable="motor_control_node",
        name="motor_control_node",
        parameters=["config/motor_speeds.yaml"],
    )

    ld.add_action(rovr_control)
    ld.add_action(motor_control)
    ld.add_action(joystick_node)

    return ld
