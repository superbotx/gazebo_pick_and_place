from botX.robots import BaseRobot
from botX.components import BaseComponent
from botX.applications import botXimport

class GazeboSimBot(BaseRobot):

    def __init__(self):
        super(GazeboSimBot, self).__init__()

        # setup camera topics
        camera_info()

        # import the gazebo api
        gz = botXimport('gazebo_api')['gazebo_api']['module']()
        
        gz.setup()

        # add api from gazebo_api to robot as components using
        # self.add_component(...)

    def additional_setup(self):
        # do any additional setup other than the ones in component setup
        pass

    def additional_shutdown(self):
        # do any additional shutdown actions
        pass

    @property
    def camera_info(self):
        self.frame = "camera_link"
        self.topic_image_color = '/camera/image_raw' 
        self.topic_image_depth = '/camera/depth/image_raw'
        self.topic_info_camera = '/camera/camera_info' 