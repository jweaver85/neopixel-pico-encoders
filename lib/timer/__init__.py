from .loop import Loop

# Enable logging by setting builtins.timer_logging = True before importing the first time.
#
# import builtins
# builtins.timer_logging = True
# import timer

__global_event_loop = None

try:
    global timer_logging
    if timer_logging:
        print('Enabling timer instrumentation')
except NameError:
    # Set False by default to skip debug logging
    timer_logging = False


def get_loop(debug=timer_logging):
    """Returns the singleton event loop"""
    global __global_event_loop
    if __global_event_loop is None:
        __global_event_loop = Loop(debug=debug)
    return __global_event_loop


add_task = get_loop().add_task
schedule = get_loop().schedule
schedule_later = get_loop().schedule_later
sleep = get_loop().sleep
suspend = get_loop().suspend

run = get_loop().run
