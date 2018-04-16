from botX.robots import BaseRobot
from botX.components import BaseComponent
from botX.applications import botXimport

class GazeboSimKinect(BaseComponent):
    def setup(self):
        gz = botXimport('gazebo_api')['gazebo_api']['module']()
        
        gz.setup()

        # setup camera topics
        self.frame = "camera_link"
        self.topic_image_color = '/camera/image_raw' 
        self.topic_image_depth = '/camera/depth/image_raw'
        self.topic_info_camera = '/camera/camera_info' 

    def shutdown(self):
        gz.shutdown()
        """
        Here you need to stop the process started in the setup
        """
        # external_command_pool.end_command(self.camera_proc_id)

    @property
    def camera_info(self):
        self.frame = "camera_link"
        self.topic_image_color = '/camera/image_raw' 
        self.topic_image_depth = '/camera/depth/image_raw'
        self.topic_info_camera = '/camera/camera_info' 


class GazeboSimBot(BaseRobot):

    def __init__(self):
        super(GazeboSimBot, self).__init__()

        

        # import the gazebo api
        # gz = botXimport('gazebo_api')['gazebo_api']['module']()
        
        # gz.setup()

        # add api from gazebo_api to robot as components using
        # self.add_component(...)
        self.add_component('camera',GazeboSimKinect)

    def additional_setup(self):
        # do any additional setup other than the ones in component setup
        pass

    def additional_shutdown(self):
        # do any additional shutdown actions
        pass

    

