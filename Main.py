import inspect, os, sys, math, functions, time, subprocess, __builtin__

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

"""
function detectGesture
params:
	frame: current frame detected by Leap
	prevFrame: frame before the current frame
	gesture_type: the type of gesture the Leap is expecting
return values: N/A
usage:
	detect gestures performed by the hand opposite to the hand used for letters
	the "swipe" gesture denotes the end of a word
	the "circle" gesture indicates backspace
	the "tap" gesture tells the program to call the eSpeak program
"""
def detectGesture(frame, prevFrame, gesture_type):
	hand = frame.hands[0]
	global hand_type
	#should run only if the hand in current frame is opposite to the one used for letters
	if ((hand_type == "Right" and hand.is_left==True) or (hand_type=="Left" and hand.is_right==True)):

		#check if this frame's gesture and the previous frame's gesture are the same
		counter = 1
		for gesture in frame.gestures():
			if gesture.type == gesture_type:
				counter += 1
				for gesture in prevFrame.gestures():
					if gesture.type == gesture_type:
						counter += 1
						break

				#if the gestures are the same, do stuff
				if counter == 2:
					if gesture_type == Leap.Gesture.TYPE_CIRCLE:
						if len(words) > 0:
							print "BACKSPACE!"
							if words[len(words) - 1] == "_":
								#if the last character in the array is an underscore,
								#delete the underscore and the letter before it as well
								del words[-1]
							#otherwise, just delete the letter
							del words[-1]
							print ''.join(filter(lambda a: a != "_", words))
					elif gesture_type == Leap.Gesture.TYPE_SWIPE:
						print "SWIPED!"
						words.append("-")
						print ''.join(filter(lambda a: a != "_", words))

					# elif gesture_type == Leap.Gesture.TYPE_KEY_TAP:
					# 	print "ESPEAK!"		#eSpeak will also run if both hands are detected at the same time
					# 	print words
					# 	#empty string in between then espeak it
					# 	subprocess.call("espeak %s" % ''.join(words))
					# 	#reset the words string
					# 	del words[:]
				else:
					break
			else:
				break
		return


"""
function detectLetter
params:
	frame: current frame detected by Leap
	prevFrame: frame before the current frame
return values: N/A
usage:
	go through the list of possible letters and check which letter it is
	do the same for the previous frame
	if both frames detect different letters, append the letter to the words array
	otherwise, just exit (to avoid spamming a letter if the user leaves their hand out)
"""
def detectLetter(frame,prevFrame):
	hand = frame.hands[0]
	if hand.is_right:
		new_hand_type = "Right"
	else:
		new_hand_type = "Left"
		
	#should only run if initial hand (hand_type) is the same as the hand in current frame
	if hand_type == new_hand_type:
				
		new_letter = ''
		old_letter = ''

		#old code
		"""
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
		elif functions.is_i(frame):
			new_letter = "I"
			if functions.is_i(prevFrame):
				return new_letter
		elif functions.is_v(frame):
			new_letter = "V"
			if functions.is_v(prevFrame):
				return new_letter
		#elif functions.two_hands(frame):
		#	print "ESPEAK"
		#	subprocess.call("espeak %s" % ''.join(words))
		#	del words[:]
		"""

		#new code
		#find what the current frame's letter is
		if functions.is_l(frame): new_letter = "L"
		elif functions.is_d(frame): new_letter = "D"
		elif functions.is_w(frame): new_letter = "W"
		elif functions.is_h(frame): new_letter = "H"
		elif functions.is_b(frame): new_letter = "B"
		elif functions.is_r(frame): new_letter = "R"
		elif functions.is_a(frame): new_letter = "A"
		elif functions.is_e(frame):	new_letter = "E"
		elif functions.is_o(frame):	new_letter = "O"
		elif functions.is_i(frame):	new_letter = "I"
		elif functions.is_v(frame):	new_letter = "V"

		if functions.is_l(prevFrame): old_letter = "L"
		elif functions.is_d(prevFrame): old_letter = "D"
		elif functions.is_w(prevFrame): old_letter = "W"
		elif functions.is_h(prevFrame): old_letter = "H"
		elif functions.is_b(prevFrame): old_letter = "B"
		elif functions.is_r(prevFrame): old_letter = "R"
		elif functions.is_a(prevFrame): old_letter = "A"
		elif functions.is_e(prevFrame):	old_letter = "E"
		elif functions.is_o(prevFrame):	old_letter = "O"
		elif functions.is_i(prevFrame):	old_letter = "I"
		elif functions.is_v(prevFrame):	old_letter = "V"

		#this code will run only if the letter changes
		# this avoids letters being spammed if the user leaves their hand in the same position
		# if new_letter != '':
		if new_letter != '' and new_letter != old_letter:
			print new_letter
			words.append(new_letter)
			print ''.join(filter(lambda a: a != "_", words))
	return


"""
function detectLetter
params:
	frame: current frame detected by Leap
	prevFrame: frame before the current frame
return values: N/A
usage:
	if the reset gesture is detected, put an underscore in the words array
	this underscore will be removed when eSpeak is called
"""
def detectReset(frame, prevFrame):
	if functions.reset(frame):
		if functions.reset(prevFrame):
			words.append("_")
	return

class SampleListener(Leap.Listener):
	
	def on_connect(self, controller):
		print "Connected"
		#Enable Gestures
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
		#controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)

	def on_frame(self, controller):

		global iter
		global hand_type
		global words
		frame = controller.frame()
		prevFrame = controller.frame(1)
		hand = frame.hands[0]
		
		#gets the intial hand that will be used for letters
		if iter==1:		
			if hand.is_right:
				hand_type = "Right"
			else:
				hand_type = "Left"
		
		hand_speed = hand.palm_velocity

		#detectSwipe(frame,prevFrame)
		#detectCircle(frame,prevFrame)
		#detectTap(frame,prevFrame)

		detectGesture(frame, prevFrame, Leap.Gesture.TYPE_SWIPE)
		detectGesture(frame, prevFrame, Leap.Gesture.TYPE_CIRCLE)
		#this line is useless because eSpeak is handled by the two_hands function
		# detectGesture(frame, prevFrame, Leap.Gesture.TYPE_KEY_TAP)

		#only detects a letter if the speed of the hand is not more than 70. (can adjust this number)
		#Prevents recognizing letters while moving hand to setup for the next letter
		if len(words) == 0 or words[len(words) - 1] == "_":
			if (abs(hand_speed.x)<150.0 and (abs(hand_speed.y)<150.0 and abs(hand_speed.z)<150.0)):
				detectLetter(frame,prevFrame)
		else:
			detectReset(frame,prevFrame)
		
		iter+=1

		#run eSpeak if both hands are detected at the same time
		if functions.two_hands(frame):
			# if len(words) == 0:
			# 	print "Nothing to say"
			# else:
			if len(words) > 0:
				print "Espeak"
				#filter out all the underscores from the words array
				words = filter(lambda a: a != "_", words)
				print ''.join(words)
				subprocess.call("espeak %s" % ''.join(words))
				del words[:]


def main():
	global iter
	iter = 1	#this global variable is used to set the hand_type only once in 'on_frame' function
	global words
	words = []

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
