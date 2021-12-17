import rotaryio
import digitalio
import board
import time

encoder = rotaryio.IncrementalEncoder(board.GP16, board.GP17)
button = digitalio.DigitalInOut(board.GP18)
button.switch_to_input(pull=digitalio.Pull.DOWN)

last_position = -1
count = 0
while True:
    position = encoder.position
    if position != last_position:
        last_position = position
        # print(int(position))
    if button.value:
        count += 1
        # print("button is pressed!")
