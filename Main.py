import inspect
import os
import sys
import math 

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

def is_d(frame):
    hand = frame.hands[0]

    #get a list of only the extended fingers
    ext_fingers = hand.fingers.extended()

    #if there is only one extended finger and it is the index finger
    if (len(ext_fingers) == 1 and ext_fingers[0].type == "TYPE_INDEX"):

        #get the floored x,y,z vals for finger direction
        x = math.floor(ext_fingers[0].direction.x)
        y = math.floor(ext_fingers[0].direction.y)
        z = math.floor(ext_fingers[0].direction.z)
        if (x == 0 and abs(y) == 1 and z == 0):
            return True
        else: return False
    else:
        return False

def is_l(frame):
    hand = frame.hands[0]

    #list of extended fingers
    ext_fingers = hand.fingers.extended()
    ext_fingers_types = [finger.type for finger in ext_fingers]

    #Check length of ext_fingers and types. 
    #Unsure of syntax, need to check. 
    if (len(ext_fingers) == 2 and "TYPE_THUMB" in ext_fingers_types and "TYPE_INDEX" in ext_fingers_types):
	thumb = 0
	index = 1
	#if the fingers are thumb and index
	if (ext_fingers[1].type == "TYPE_THUMB"):
	    thumb = 1
	    index = 0
        
	#Set co-ordinates for thumb and finger
	#Floor would just take it down to zero??
	x_thumb = int(round(ext_fingers[thumb].direction.x))
	y_thumb = int(round(ext_fingers[thumb].direction.y))
	z_thumb = int(round(ext_fingers[thumb].direction.z))

	x_index = int(round(ext_fingers[index].direction.x))
	y_index = int(round(ext_fingers[index].direction.y))
	z_index = int(round(ext_fingers[index].direction.z))
	
	if(abs(x_thumb) == 1 and y_thumb == 0 and z_thumb == 0
			and x_index == 0 and abs(y_index) == 1 and z_index == 0):
	    return True
        else:
	    return False
 

    else:
        return False

def is_w(frame):
	hand = frame.hands[0]
	
	#get a list of only the extended fingers
	ext_fingers = hand.fingers.extended()
	ext_fingers_types = [finger.type for finger in ext_fingers]
	
	# if there are three extended fingers and the fingers types are index, middle and ring
	if (len(ext_fingers) == 3 and ("TYPE_INDEX" in ext_fingers_types) 
		and ("TYPE_MIDDLE" in ext_fingers_types) and ("TYPE_RING" in ext_fingers_types):
		#floored x,y,z values for first extended finger
		x1 = math.floor(ext_fingers[0].direction.x)
        	y1 = math.floor(ext_fingers[0].direction.y)
        	z1 = math.floor(ext_fingers[0].direction.z)
		
		#floored x,y,z values for second extended finger
		x2 = math.floor(ext_fingers[1].direction.x)
        	y2 = math.floor(ext_fingers[1].direction.y)
        	z2 = math.floor(ext_fingers[1].direction.z)
		
		#floored x,y,z values for third extended finger
		x3 = math.floor(ext_fingers[2].direction.x)
        	y3 = math.floor(ext_fingers[2].direction.y)
        	z3 = math.floor(ext_fingers[2].direction.z)
		
		#x,y,z coordinates for three extended fingers should be (0,1,0)
		if(x1 == 0 and y1 == 1 and z1 == 0 and x2 == 0 and y2 == 1 
			and z2 == 0 and x3 == 0 and y3 == 1 and z3 == 0):
			return True
		else:
			return False
			
	else:
		return False

class SampleListener(Leap.Listener):
    
    def on_connect(self, controller):
        print "Connected"
        
        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
    
    def on_frame(self, controller):        
        #Get the most recent frame
        frame = controller.frame()
        prevFrame = controller.frame(1)

        detectSwipe(frame,prevFrame)
        print is_d(frame)
        # counter = 1
		
		
        # for gesture in frame.gestures():
        #     if gesture.type == Leap.Gesture.TYPE_SWIPE:
        #         #print "SWIPED!"
        #         counter += 1
			#
        #         for gesture in prevFrame.gestures():
        #             if gesture.type == Leap.Gesture.TYPE_SWIPE:
        #                 counter += 1
        #                 break
        #         if counter == 2:
        #             print "SWIPED!"
        #         else:
        #             break
        #     else:
        #         break
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
