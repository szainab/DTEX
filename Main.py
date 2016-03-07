import inspect
import os
import sys
import math 
import functions
from timeit import default_timer as timer

# src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# arch_dir = '../lib/x64' if sys.maxsize > 2**3 else '../lib/x86'
# sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

sys.path.append('lib')
sys.path.append('lib/x64')
sys.path.append('lib/x86')

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


def detectSwipe(frame, prevFrame):
    counter = 1
    for gesture in frame.gestures():
        if gesture.type == Leap.Gesture.TYPE_SWIPE:
            #print "SWIPED!"
            counter += 1

            for gesture in prevFrame.gestures():
                if gesture.type == Leap.Gesture.TYPE_SWIPE:
                    counter += 1
                    break
            if counter == 2:
                print "SWIPED!"
            else:
                break
        else:
            break

    return

def detectLetter(frame, letter, start_time):
	debug = True
	end_time = timer()
	time_taken = end_time - start_time
	if debug:
		print "End_time: " + str(end_time)
		print "Time_taken: " + str(time_taken)

	if functions.is_l(frame):
		if letter != L or time_taken>2.0:
			letter = "L"
			print letter
			return letter
		else:
			return letter
	elif functions.is_d(frame):
		if letter != D or time_taken>2.0:
			letter = "D"
			print letter
			return letter
		else:
			return letter
	elif functions.is_w(frame):
		if letter != W or time_taken>2.0:
			letter = "W"
			print letter
			return letter
		else:
			return letter
	elif functions.is_h(frame):
		if letter != H or time_taken>2.0:
			letter = "H"
			print letter
			return letter
		else:
			return letter
	else:
		print "Unidentified Letter"

class SampleListener(Leap.Listener):
    
    def on_connect(self, controller):
        print "Connected"
        
        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
    
    def on_frame(self, controller):
	debug = True
	#Get the most recent frame
	start_time = timer()
	frame = controller.frame()
	prevFrame = controller.frame(1)
        detectSwipe(frame,prevFrame)
        #print functions.is_h(frame)
	#print functions.is_l(frame)
	#print functions.is_d(frame)
	if functions.reset(prevFrame):
		if debug:
			print "reset triggered"
		letter = ""
		letter = detectLetter(frame, letter, start_time)
	# counter = 1
		
		
       
def main():
    listener = SampleListener()
    controller = Leap.Controller()
    
    controller.add_listener(listener)
    
    #Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally: 
        #Remove the sample listener when done
        controller.remove_listener(listener)
    
if __name__ == "__main__":
    main()
