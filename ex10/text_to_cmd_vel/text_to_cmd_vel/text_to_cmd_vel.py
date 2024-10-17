import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class TextToCmdVel(Node):
    def __init__(self):
        super().__init__('text_to_cmd_vel')
        
        # Подписка на текстовые команды
        self.subscription = self.create_subscription(
            String,
            'cmd_text',
            self.listener_callback,
            10)
        
        # Публикация в топик /turtle1/cmd_vel
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Скорости для черепахи
        self.linear_speed = 1.0  # м/с
        self.angular_speed = 1.5  # рад/с

    def listener_callback(self, msg):
        command = msg.data.lower().strip()
        twist = Twist()
        
        if command == "move_forward":
            twist.linear.x = self.linear_speed
        elif command == "move_backward":
            twist.linear.x = -self.linear_speed
        elif command == "turn_left":
            twist.angular.z = self.angular_speed
        elif command == "turn_right":
            twist.angular.z = -self.angular_speed
        else:
            self.get_logger().info(f"Unknown command: {command}")
            return
        
        self.publisher.publish(twist)
        self.get_logger().info(f"Executed command: {command}")

def main(args=None):
    rclpy.init(args=args)
    node = TextToCmdVel()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

