import inspect, os, sys, math, functions, time, subprocess, __builtin__
from timeit import default_timer as timer

#output file
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'testfile.txt')
letterFile=open(filename, "w")

# src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# arch_dir = '../lib/x64' if sys.maxsize > 2**3 else '../lib/x86'
# sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

sys.path.append('lib')
sys.path.append('lib/x64')
sys.path.append('lib/x86')

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

#set the debug variable here, it will be global across all import
__builtin__.debug = False
__builtin__.words = []

'''
def detectSwipe(frame, prevFrame):
	counter = 1
	for gesture in frame.gestures():
		if gesture.type == Leap.Gesture.TYPE_SWIPE:
 			counter += 1
			for gesture in prevFrame.gestures():
				if gesture.type == Leap.Gesture.TYPE_SWIPE:
					counter += 1
					break
			if counter == 2:
				print "SWIPED!"
				words.append("-")
			else:
				break
		else:
			break

	return


def detectCircle(frame, prevFrame):
	counter = 1
	for gesture in frame.gestures():
		if gesture.type == Leap.Gesture.TYPE_CIRCLE:
			counter += 1
			for gesture in prevFrame.gestures():
				if gesture.type == Leap.Gesture.TYPE_CIRCLE:
					counter += 1
					break
			if counter == 2:
				print "BACKSPACE!"
				del words[-1]
			else:
				break
		else:
			break
	return


def detectTap(frame, prevFrame):
	counter = 1
	for gesture in frame.gestures():
		if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
			counter += 1
			for gesture in prevFrame.gestures():
				if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
					counter += 1
					break
			if counter == 2:
				print "ESPEAK!"
				print words
				subprocess.call("espeak %s" % ''.join(words))
				del words[:]
			else:
				break
		else:
			break
	return
'''

def detectGesture(frame, prevFrame, gestType):
	counter = 1
	gesture_type = ''
	if gestType == "Swipe":
		gesture_type = Leap.Gesture.TYPE_SWIPE
	elif gestType == "Tap":
		gesture_type = Leap.Gesture.TYPE_KEY_TAP
	elif gestType == "Circle":
		gesture_type = Leap.Gesture.TYPE_CIRCLE

	for gesture in frame.gestures():
		if gesture.type == gesture_type:
 			counter += 1
			for gesture in prevFrame.gestures():
				if gesture.type == gesture_type:
					counter += 1
					break
			if counter == 2:
				if gestType == "Swipe":
					print "SWIPED!"
					words.append("-")
				elif gestType == "Circle":
					print "BACKSPACE!"
					del words[-1]
				elif gestType == "Tap":
					print "ESPEAK!"
					#Join words together to form a string with
					#empty string in between then espeak it
					subprocess.call("espeak %s" % ''.join(words))
			else:
				break
		else:
			break

	return


def detectLetter(frame,prevFrame):
	#timing stuff
	#end_time = timer()
	#time_taken = end_time - start_time
	#print "End_time: " + str(end_time)
	#print "Time_taken: " + str(time_taken)

	# if debug: print "Waiting for letter"
	#hand = frame.hands[0]
	#ext_fingers = hand.fingers.extended()
	
	
	'''

	print "Length of ext_fingers " + str(len(ext_fingers))
	print "ext_fingers types " + str([finger.type for finger in ext_fingers])
	for finger in ext_fingers:
		print "Finger type = " + str(finger.type) + ", direction = " + str(finger.direction.x) + "," + str(finger.direction.y) + "," + str(finger.direction.z)
		

	(inzi)
		
	'''

	new_letter = ''

	if functions.is_l(frame):
		new_letter = "L"
		if functions.is_l(prevFrame):
			return new_letter			
	elif functions.is_d(frame):
		new_letter = "D"
		if functions.is_d(prevFrame):
			return new_letter
	elif functions.is_w(frame):
		new_letter = "W"
		if functions.is_w(prevFrame):
			return new_letter
	elif functions.is_h(frame):
		new_letter = "H"
		if functions.is_h(prevFrame):
			return new_letter
	elif functions.is_b(frame):
		new_letter = "B"
		if functions.is_b(prevFrame):
			return new_letter		
	elif functions.is_r(frame):
		new_letter = "R"
		if functions.is_r(prevFrame):
			return new_letter
	elif functions.is_a(frame):
		new_letter = "A"
		if functions.is_a(prevFrame):
			return new_letter
	elif functions.is_e(frame):
		new_letter = "E"
		if functions.is_e(prevFrame):
			return new_letter
	elif functions.is_o(frame):
		new_letter = "O"
		if functions.is_o(prevFrame):
			return new_letter
		
	if new_letter != '':
		print new_letter
		words.append(new_letter)
		return new_letter 

#	elif functions.is_g(frame):
#		new_letter = "G"
#	elif functions.is_r(frame):
#		new_letter = "R"
#	elif functions.is_a(frame):
#		new_letter = "A"
#	print new_letter
#	return new_letter



	# if functions.is_l(frame) and letter != 'L': letter = "L"
	# 	if letter != 'L': # or time_taken>7.0:
	# 		letter = "L"
	# elif functions.is_d(frame) and letter != "D": letter = "D"
	# 	if letter != 'D': # or time_taken>7.0:
	# 		letter = "D"
	# elif functions.is_w(frame) and letter != "W": letter = "W"
	# 	if letter != 'W': # or time_taken>7.0:
	# 		letter = "W"
	# elif functions.is_h(frame) and letter != "H": letter = "H"
	# 	if letter != 'H': # or time_taken>7.0:
	# 		letter = "H"
	# else:
	# 	letter = ''
	# 	print "Unidentified Letter"
	# print letter
	# return letter

class SampleListener(Leap.Listener):


	def on_connect(self, controller):
		print "Connected"
		#Enable Gestures
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		#controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)


	def on_frame(self, controller):
		

		#kind of useless now
		#start_time = timer()

		#do the loop while the letter is the same or if the Leap is reset
		# while self.letter == new_letter:
		# 	print "in loop"
		# 	#get the newest frame
		#frame = controller.frame()
		# 	print "frame id: " + str(frame.id)

		#if functions.reset(frame): new_letter = ''
		#else: new_letter = detectLetter(frame)


		#if self.letter != new_letter:			
		#    print new_letter
                #    letterFile.write(new_letter) #writes letter to the file
		#set the old letter to the new letter
		#self.letter = new_letter
		#wait for a bit, to "debounce"
		
		#time.sleep(1)    (inzi)
		
		# print frame.hands[0].grab_strength

		#ext_fingers = frame.hands[0].fingers.extended() (inzi)
		#print "thumb direction = " + str(ext_fingers[0].bone(3).direction.x) (inzi)



		# ext_fingers = frame.hands[0].fingers.extended()
		# print "rightmost" + str(ext_fingers.rightmost.type)

		#Get the most recent frame
		#start_time = timer() (inzi - and this line has nothing to do with recent frame) 


		#frame = controller.frame()
		#prevFrame = controller.frame(1)
        
		# print "Detecting swipe"
		#detectSwipe(frame,prevFrame)

		# start_time = timer()
		#frame = controller.frame()
		#prevFrame = controller.frame(1)
        	# print "Detecting swipe"
		#detectSwipe(frame,prevFrame)

		# #if functions.reset(prevFrame):
		# if debug: print "reset triggered"
		# #time.sleep(5.0)
		# self.letter = detectLetter(frame, self.letter, start_time)

		#inzi code
		
		frame = controller.frame()
		prevFrame = controller.frame(1)
		#detectSwipe(frame,prevFrame)
		#detectCircle(frame,prevFrame)
		#detectTap(frame,prevFrame)
		detectGesture(frame, prevFrame, "Swipe")
		detectGesture(frame, prevFrame, "Tap")
		detectGesture(frame, prevFrame, "Circle")
		detectLetter(frame,prevFrame)


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
