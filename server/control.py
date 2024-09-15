import SpiderG
import time
from ultrasonic import measure_distance, gpio_clean_up
from directions import Directions

WALK_TIME = 5
TURN_TIME = 5
STOP_DISTANCE = 50

try:
    # Initial position
    SpiderG.move_init()
    while True:
        # If object detected by ultrasonic sensor, turn right
        distance = measure_distance()
        if measure_distance() < STOP_DISTANCE:
            print(f"obstacle in {distance}cm, turn right")
            SpiderG.walk(Directions.TURN_RIGHT.value)
            time.sleep(TURN_TIME)

        # Else, walk forward
        else:
            print("no obstacle, forward")
            SpiderG.walk(Directions.FORWARD.value)
            time.sleep(WALK_TIME)
except KeyboardInterrupt:
    print("clean up")
    gpio_clean_up()
    SpiderG.servoStop()
