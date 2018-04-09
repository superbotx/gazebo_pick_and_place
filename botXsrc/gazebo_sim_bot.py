from botX.robots import BaseRobot
from botX.components import BaseComponent
from botX.applications import botXimport

class GazeboSimBot(BaseRobot):

    def __init__(self):
        super(GazeboSimBot, self).__init__()

        # import the gazebo api
        gazebo_apis = botXimport('gazebo_api')

        # add api from gazebo_api to robot as components using
        # self.add_component(...)

    def additional_setup(self):
        # do any additional setup other than the ones in component setup
        pass

    def additional_shutdown(self):
        # do any additional shutdown actions
        pass
