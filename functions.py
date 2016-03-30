# Fingers:
# Type of thumb = 0
# Type of index = 1
# Type of middle = 2
# Type of ring = 3
# Type of pinky = 4

# Bones:
# Note: Tip of finger is Distal & Thumb has no metacarpal
# Type of Metacarpal = 0
# Type of Proximal = 1
# Type of Intermediate = 2
# Type of Distal = 3

"""
function checkArray
params:
	arr: the array to check
	num: the number of elements to check for
return values: boolean
usage:
	check if all elements in an array are equal to num
"""


def checkArray(arr, num):
	if all(item == num for item in arr):
		return True
	else:
		return False


"""
function reset
params:
	frame: current frame detected by Leap
return values: boolean
usage:
	return True only if all the fingers are extended and none of them is pointing upwards
"""


def reset(frame):
	hand = frame.hands[0]
	# list of extended fingers
	ext_fingers = hand.fingers.extended()
	# types of extended fingers
	ext_fingers_type = [finger.type for finger in ext_fingers]

	if (len(ext_fingers_type) == 5):
		# put y values for everything into an array
		y_val = [int(round(ext_fingers[0].direction.y)),
				 int(round(ext_fingers[1].direction.y)),
				 int(round(ext_fingers[2].direction.y)),
				 int(round(ext_fingers[3].direction.y)),
				 int(round(ext_fingers[4].direction.y))]
		if checkArray(y_val, 0):
			return True  # only return True in this case
	# return False by default
	return False


"""
function two_hands
params:
	frame: current frame detected by Leap
return values: boolean
usage:
	check if the Leap detects two hands
"""


def two_hands(frame):
	if len(frame.hands) == 2:
		return True
	return False


"""
all letter functions
params:
	frame: current frame detected by Leap
return values: boolean
usage:
	return True if the Leap detects a certain letter
"""


def is_i(frame):
	# pinky finger is straight up, all other fingers are closed
	hand = frame.hands[0]
	ext_fingers = hand.fingers.extended()
	if len(ext_fingers) == 1 and ext_fingers[0].type == 4:
		x = int(round(ext_fingers[0].direction.x))
		y = int(round(ext_fingers[0].direction.y))
		z = int(round(ext_fingers[0].direction.z))
		if abs(y) == 1 and x == 0:
			return True
	return False


def is_v(frame):
	# index and middle finger are straight, pointing upwards, slightly apart
	# thumb covers the ring finger
	hand = frame.hands[0]
	ext_fingers = hand.fingers.extended()
	if len(ext_fingers) == 2 and ext_fingers[0].type == 1 and ext_fingers[1].type == 2:
		x = int(round(ext_fingers[0].direction.x))
		y = int(round(ext_fingers[0].direction.y))
		z = int(round(ext_fingers[0].direction.z))
		x1 = int(round(ext_fingers[1].direction.x))
		y1 = int(round(ext_fingers[1].direction.y))
		z1 = int(round(ext_fingers[1].direction.z))
		if abs(y) == 1 and abs(y1) == 1 and x == 0 and x1 == 0:
			return True
	return False


def is_a(frame):
	# fist with straight thumb pointing upwards
	hand = frame.hands[0]
	ext_fingers = hand.fingers.extended()
	x_palm = int(round(hand.palm_normal.x))
	y_palm = int(round(hand.palm_normal.y))
	if len(ext_fingers) == 1 and ext_fingers[0].type == 0 and x_palm == 0 and y_palm == 0:
		x = int(round(ext_fingers[0].direction.x))
		y = int(round(ext_fingers[0].direction.y))
		z = int(round(ext_fingers[0].direction.z))

		if x == 0 and y == 1:
			return True
	return False


def is_b(frame):
	# "talk to the hand" with thumb covering palm instead of beside the other fingers
	hand = frame.hands[0]
	# list of extended fingers:
	ext_fingers = hand.fingers.extended()

	# If there are four extended fingers and thumb is not one of them
	if len(ext_fingers) == 4 and ext_fingers[0].type != 0:
		# rounded co-ordinates for all fingers, stored in respective arrays
		x = [int(round(ext_fingers[0].direction.x)), int(round(ext_fingers[1].direction.x)),
			 int(round(ext_fingers[2].direction.x)), int(round(ext_fingers[3].direction.x))]
		y = [abs(int(round(ext_fingers[0].direction.y))), abs(int(round(ext_fingers[1].direction.y))),
			 abs(int(round(ext_fingers[2].direction.y))), abs(int(round(ext_fingers[3].direction.y)))]
		z = [int(round(ext_fingers[0].direction.z)), int(round(ext_fingers[1].direction.z)),
			 int(round(ext_fingers[2].direction.z)), int(round(ext_fingers[3].direction.z))]

		if checkArray(x, 0) and checkArray(y, 1):
			return True  # Only return True in this case, return False by default
	return False


def is_d(frame):
	# index finger pointing straight up, all other fingers closed
	hand = frame.hands[0]
	# get a list of only the extended fingers
	ext_fingers = hand.fingers.extended()
	# if debug:
	# 	print "length of array = " + str(len(ext_fingers))
	# 	print "types in the array = " + str([finger.type for finger in ext_fingers])
	# print "types array" + str(ext_fingers_types)

	# if there is only one extended finger and it is the index finger
	if len(ext_fingers) == 1 and ext_fingers[0].type == 1:
		# get the floored x,y,z vals for finger direction
		# int ensures no decimal places
		# round rounds up number to 1 dp
		x = int(round(ext_fingers[0].direction.x))
		y = int(round(ext_fingers[0].direction.y))
		z = int(round(ext_fingers[0].direction.z))
		if debug: print "D " + str(x) + ", " + str(y) + ", " + str(z)
		if x == 0 and abs(y) == 1:
			return True  # Only True in this case, returns False by default
	return False


def is_l(frame):
	# literally an L shape with index and thumb
	hand = frame.hands[0]

	# list of extended fingers
	ext_fingers = hand.fingers.extended()
	ext_fingers_types = [finger.type for finger in ext_fingers]
	# if debug:
	# 	print "length of array = " + str(len(ext_fingers))
	# 	print "types in the array = " + str([finger.type for finger in ext_fingers])
	# 	print "types array" + str(ext_fingers_types)

	# Check length of ext_fingers and types.
	if len(ext_fingers) == 2 and ext_fingers_types[0] == 0 and ext_fingers_types[1] == 1:
		# Set co-ordinates for thumb and finger
		# For the thumb, get the direction for distal bones
		x_thumb = int(round(ext_fingers[0].bone(3).direction.x))
		y_thumb = int(round(ext_fingers[0].bone(3).direction.y))
		z_thumb = int(round(ext_fingers[0].bone(3).direction.z))
		# x_thumb = int(round(ext_fingers[0].direction.x))
		# y_thumb = int(round(ext_fingers[0].direction.y))
		# z_thumb = int(round(ext_fingers[0].direction.z))

		x_index = int(round(ext_fingers[1].direction.x))
		y_index = int(round(ext_fingers[1].direction.y))
		z_index = int(round(ext_fingers[1].direction.z))

		if debug:
			print "thumb values (x y z) " + str(x_thumb) + ", " + str(y_thumb) + ", " + str(z_thumb)
			print "index values (x y z) " + str(x_index) + ", " + str(y_index) + ", " + str(z_index)

		if abs(x_thumb) == 1 and y_thumb == 0 and x_index == 0 and abs(y_index) == 1:
			return True  # Only True in this case, return False by default
	return False


def is_h(frame):
	# index and middle finger pointing horizontally, other fingers are closed
	hand = frame.hands[0]
	ext_fingers = hand.fingers.extended()
	# ext_finger_types = [finger.type for finger in ext_fingers]
	# if(debug == True):
	# 	print "Length of ext_fingers" + str(len(ext_fingers))
	# 	print "ext_fingers types " + str([finger.type for finger in ext_fingers])

	if len(ext_fingers) == 2 and ext_fingers[0].type == 1 and ext_fingers[1].type == 2:
		x_index = int(round(ext_fingers[0].direction.x))
		y_index = int(round(ext_fingers[0].direction.y))
		z_index = int(round(ext_fingers[0].direction.z))

		x_middle = int(round(ext_fingers[1].direction.x))
		y_middle = int(round(ext_fingers[1].direction.y))
		z_middle = int(round(ext_fingers[1].direction.z))

		x_palm = int(round(hand.palm_normal.x))
		if debug:
			print "Index values [x,y,z]: " + str(x_index) + ", " + str(y_index) + ", " + str(z_index)
			print "Middle values [x,y,z]: " + str(x_middle) + ", " + str(y_middle) + ", " + str(z_middle)
			print hand.palm_normal

		if ((abs(x_index) == 1 and y_index == 0 and z_index == 0 and abs(
			x_middle) == 1 and y_middle == 0 and z_middle == 0) or (x_index == 0 and y_index == 0 and abs(
			z_index) == 1 and x_middle == 0 and y_middle == 0 and abs(z_middle) == 1 and abs(x_palm) == 1)):
			return True  # only true in this case, returns false by default
	return False


def is_g(frame):
	# index finger pointing horizontally, other fingers are closed
	hand = frame.hands[0]
	ext_fingers = hand.fingers.extended()
	# ext_finger_types = [finger.type for finger in ext_fingers]

	# if(debug == True):
	# 	print "Length of ext_fingers" + str(len(ext_fingers))
	# 	print "ext_fingers types " + str([finger.type for finger in ext_fingers])

	if len(ext_fingers) == 1 and ext_fingers[0].type == 1:
		x_index = int(round(ext_fingers[0].direction.x))
		y_index = int(round(ext_fingers[0].direction.y))
		z_index = int(round(ext_fingers[0].direction.z))

		x_palm = int(round(hand.palm_normal.x))

		if debug:
			print "Index values [x,y,z]: " + str(x_index) + ", " + str(y_index) + ", " + str(z_index)
			print hand.palm_normal

		if ((abs(x_index) == 1 and y_index == 0 and z_index == 0) or (
								x_index == 0 and y_index == 0 and abs(z_index) == 1 and abs(x_palm) == 1)):
			return True  # only true in this case, returns false by default
	return False


def is_w(frame):
	# index, middle and ring fingers straight, slightly apart, pointing upwards
	# thumb connects with closed pinky finger
	hand = frame.hands[0]

	# get a list of only the extended fingers
	ext_fingers = hand.fingers.extended()
	ext_fingers_types = [finger.type for finger in ext_fingers]

	# if there are three extended fingers and the fingers types are index, middle and ring
	if (len(ext_fingers) == 3 and (ext_fingers_types[0] == 1) and (ext_fingers_types[1] == 2) and (
				ext_fingers_types[2] == 3)):
		# floored x,y,z values for first extended finger
		x1 = int(round(ext_fingers[0].direction.x))
		y1 = int(round(ext_fingers[0].direction.y))
		z1 = int(round(ext_fingers[0].direction.z))

		# floored x,y,z values for second extended finger
		x2 = int(round(ext_fingers[1].direction.x))
		y2 = int(round(ext_fingers[1].direction.y))
		z2 = int(round(ext_fingers[1].direction.z))

		# floored x,y,z values for third extended finger
		x3 = int(round(ext_fingers[2].direction.x))
		y3 = int(round(ext_fingers[2].direction.y))
		z3 = int(round(ext_fingers[2].direction.z))

		if debug == True:
			print "Thumb values [x,y,z]: " + str(x1) + ", " + str(y1) + ", " + str(z1)
			print "Index values [x,y,z]: " + str(x2) + ", " + str(y2) + ", " + str(z2)
			print "Middle values [x,y,z]: " + str(x3) + ", " + str(y3) + ", " + str(z3)

		# x,y,z coordinates for three extended fingers should be (0,1,0)
		if x1 == 0 and y1 == 1 and x2 == 0 and y2 == 1 and x3 == 0 and y3 == 1:
			return True  # only returns true in this case, returns false by default
	return False


def is_r(frame):
	# index and middle finger straight and crossed over each other, other fingers are closed
	hand = frame.hands[0]

	# get a list of only the extended fingers
	ext_fingers = hand.fingers.extended()
	ext_fingers_types = [finger.type for finger in ext_fingers]

	# if there are three extended fingers and the fingers types are index, middle and ring
	if (len(ext_fingers) == 2 and (ext_fingers_types[0] == 1) and (ext_fingers_types[1] == 2)):
		# x,y,z values for first extended finger
		# x1 = int(ext_fingers[0].direction.x))
		y1 = int(round(ext_fingers[0].direction.y))
		z1 = int(round(ext_fingers[0].direction.z))

		# x,y,z values for second extended finger
		# x2 = int(ext_fingers[1].direction.x))
		y2 = int(round(ext_fingers[1].direction.y))
		z2 = int(round(ext_fingers[1].direction.z))

		if debug == True:
			print "Index values [y,z]: " + ", " + str(y1) + ", " + str(z1)
			print "Middle values [y,z]: " + ", " + str(y2) + ", " + str(z2)

		# y and z coordinates for both extended fingers should be 1 and 0 respectively.
		if y1 == 1 and z1 == 0 and y2 == 1 and z2 == 0:
			# if right hand, finger with largest x co-ordinate should be index finger
			if hand.is_right:
				if ext_fingers.rightmost.type == 0 or ext_fingers.rightmost.type == 1:
					return True
				else:
					return False

			# if left hand, finger with smallest x co-ordinate should be index finger
			elif hand.is_left:
				if ext_fingers.leftmost.type == 0 or ext_fingers.leftmost.type == 1:
					return True
				else:
					return False
		else:
			return False


def is_e(frame):
	# all fingers closed in a loose fist, with tips of fingers all touching the thumb
	hand = frame.hands[0]
	ext_fingers = hand.fingers.extended()
	# get the x direction of normal vector to the palm
	x_palm = int(round(hand.palm_normal.x))
	fingers = hand.fingers

	# gets the x direction of the distal bone of thumb
	x_thumb = int(round(fingers[0].bone(3).direction.x))
	# none of the fingers should be extended and x direction of normal vector should be 0.
	if (len(ext_fingers) == 0 and x_palm == 0 and abs(x_thumb) == 1):
		return True
	else:
		return False


def is_o(frame):
	# an O sign with the hand
	hand = frame.hands[0]
	ext_fingers = hand.fingers.extended()
	# get the x direction of normal vector to the palm
	x_palm = int(round(hand.palm_normal.x))

	# none of the fingers should be extended and x direction of normal vector should be either 1 or -1.
	if (len(ext_fingers) == 0 and abs(x_palm) == 1):
		return True
	else:
		return False
