from botX.robots import BaseRobot
from botX.components import BaseComponent
from botX.applications import botXimport
import rospy

class ManipulationController(BaseComponent):
    def setup(self):
        self.path = botXimport('manipulation_api')['manipulation_api']['module']()
        self.path.setup()

    def get_path(self, pose):
        planned_path = self.path.plan_path(pose)
        return planned_path

    def shutdown(self):
        self.path.shutdown()

class GraspController(BaseComponent):
    def setup(self):
        self.grasp = botXimport('grasp_api')['grasp_api']['module']()
        self.grasp.setup()

    def get_grasp(self, object_name='cup', bounding_box=None):
        grasp_pose = self.grasp.object_to_grasp(object_name, bounding_box)
        return grasp_pose

    def shutdown(self):
        self.grasp.shutdown()

class GazeboSimKinect(BaseComponent):
    def setup(self):
        self.gz = botXimport('gazebo_api')['gazebo_api']['module']()
        print("GazeboSimKinect setting up! ", self.gz)
        
        self.gz.setup()

        # setup camera topics
        self.frame = "camera_link"
        self.topic_image_color = '/camera/image_raw' 
        self.topic_image_depth = '/camera/depth/image_raw'
        self.topic_info_camera = '/camera/camera_info' 

    def shutdown(self):
        self.gz.shutdown()
        """
        Here you need to stop the process started in the setup
        """
        # external_command_pool.end_command(self.camera_proc_id)

    def get_image(self, *img_type):
        im = self.gz.get_image();
        return im

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
        self.add_component('camera',GazeboSimKinect())
        self.add_component('grasp', GraspController())
        self.add_component('path_planner', ManipulationController())
        # self.add_component('bridge', botXimport('rosbridge_api')['rosbridge_suit_component']['module']())
        # self.setup_components()

    def additional_setup(self):
        # do any additional setup other than the ones in component setup
        pass

    def additional_shutdown(self):
        # do any additional shutdown actions
        pass

    

