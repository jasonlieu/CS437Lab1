from ultrasonic import gpio_clean_up
from mapping import *

GOAL = (0, 0) # (0,0) - (19, 19)

MAX_DISTANCE = 300
DISTANCE_THRESHOLD = 300

def go():
    print("here we go")
    # while current_location != goal:
        # get next step in path
        # orient robot to move to next square
        # check for obstacle 1 square in front

        # if obstacle,
            # make 1 on grid, rerun a*
        # if no obstacle,
            # move forward 1 square
            # update grid with new robot location



# Example usage of the scan_360_to_grid function
grid_size = 20  # X and Y size
try:
    # TODO aim for ~20 steps
    SpiderG.move_init()
    grid = scan_360_to_grid(grid_size, degree_step=20, distance_threshold=DISTANCE_THRESHOLD, max_distance=MAX_DISTANCE)
    start = (grid_size // 2, grid_size // 2)  # Starting point in center
    path = a_star(grid, start, GOAL)
    print("\n\n")
    print_grid_with_path(grid, path)

    go()

finally:
    print("clean up")
    gpio_clean_up()
    SpiderG.servoStop()