from botX.tasks import BaseTask
# from packaged_mask_rcnn import EZ

class LocateObject(BaseTask):
    def __init__(self, robot):
        super(LocateObject, self).__init__(robot)

    def setup(self, **kwargs):
        # anything this task needs to know upfront will be set here
        # for example initialize mask rcnn
        self.mask_rcnn = EZ()

    def run(self, **kwargs):
        target_object = kwargs['target_object']
        images = self.robot.components['camera'].get_image(['rgb', 'd'])
        annotated_img, statistic_res = self.mask_rcnn.detect(images[0])
        if target_object in set(statistic_res['class_names']):
            return 'found', statistic_res[target_object]
        else:
            return 'not_found', None

class PickObject(BaseTask):
    def __init__(self, robot):
        super(PickObject, self).__init__(robot)

    def setup(self, **kwargs):
        # anything this task needs to know upfront will be set here
        pass

    def run(self, **kwargs):
        target_location = kwargs['target_location']
        """
        this method will get target location from LocateObject task,
        then it should call gazebo api to convert the image coordinate
        to robot coordinate. After that it will call another gazebo api
        to pick up the object
        """
        pass

class FindAvailableSpace(BaseTask):
    def __init__(self, robot):
        super(FindAvailableSpace, self).__init__(robot)

    def setup(self, **kwargs):
        # anything this task needs to know upfront will be set here
        pass

    def run(self, **kwargs):
        """
        this method will use gazebo api to get a image and then use vision to
        find a empty space to place the picked up object
        """
        pass

class PlaceObject(BaseTask):
    def __init__(self, robot):
        super(PlaceObject, self).__init__(robot)

    def setup(self, **kwargs):
        # anything this task needs to know upfront will be set here
        pass

    def run(self, **kwargs):
        """
        this method will take the location we got from FindAvailableSpace
        and the call gazebo_api using self.robot.components['arm'] to place
        the object to the empty space
        """
        pass

class PickAndPlace(BaseTask):
    def __init__(self, robot):
        super(PickAndPlace, self).__init__(robot)
        self.add_subtask('locate_object', LocateObject())
        self.add_subtask('pick_object', PickObject())
        self.add_subtask('place_object', PlaceObject())
        self.add_subtask('find_space', PlaceObject())

    def setup(self, **kwargs):
        # anything this task needs to know upfront will be set here
        pass

    def run(self, **kwargs):
        """
        this method will perform the pick and place, by calling
        self.get_subtask('...')
        """
        pass
