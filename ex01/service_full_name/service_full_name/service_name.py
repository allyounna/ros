#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from full_name_package.srv import FullNameSumService

class MinimalService(Node):
    def __init__(self):
            super().__init__('minimal_service')
            self.srv = self.create_service(FullNameSumService, 'full_name', self.handle_summ_full_name)


    def handle_summ_full_name(self, request, response):
        response.full_name = request.last_name + " " + request.name + " " + request.first_name
        return response

def main():
    rclpy.init()
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()


if __name__ == '__main__':
    main()