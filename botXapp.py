from botXsrc.botXexport import botXexport
import time

"""
botXexport is a dictionary containing all the reusable components you
developed for the project, and you will use them in the main program.
"""
def main():
    print('starting app ...')
    robot = botXexport['gazebo_sim_robot']['module']()
    task = botXexport['pick_and_place']['module'](robot)
    print(task)
    robot.start()
    time.sleep(5)
    task.run(target_object='cup')
    # robot.shutdown()
    print('all tasks finished')

"""
This is the only script that should be running from terminal so that the
program can gather modules correctly, so we need to specify main as entry point.
"""
if __name__ == '__main__':
    main()
