#Fingers:
#Type of thumb = 0
#Type of index = 1
#Type of middle = 2
#Type of ring = 3
#Type of pinky = 4

#Bones:
#Note: Tip of finger is Distal & Thumb has no metacarpal
#Type of Metacarpal = 0
#Type of Proximal = 1
#Type of Intermediate = 2
#Type of Distal = 3

#The letter b requires a lot of checking the array for the same letter
#I got bored of writing it so i made a function
def checkArray(arr, num):
	if all(item == num for item in arr):
		return True
	else:
		return False

def reset(frame):
	hand = frame.hands[0]

	#list of extended fingers
	ext_fingers = hand.fingers.extended()
	#types of extended fingers
	ext_fingers_type = [finger.type for finger in ext_fingers]
	
	if(len(ext_fingers_type) == 5):
		#put y values for everything into an array
		y_val = [ int(round(ext_fingers[0].direction.y)), 
			  int(round(ext_fingers[1].direction.y)), 
			  int(round(ext_fingers[2].direction.y)),
			  int(round(ext_fingers[3].direction.y)),
			  int(round(ext_fingers[4].direction.y))]
		if checkArray(y_val, 0):
			return True 	#only return True in this case, return False by default

	return False

def is_a(frame):
	hand = frame.hands[0]
	ext_fingers = hand.fingers.extended()

	if (len(ext_fingers) == 1 and ext_fingers[0].type == 0):
		x = int(round(ext_fingers[0].direction.x))
		y = int(round(ext_fingers[0].direction.y))
		z = int(round(ext_fingers[0].direction.z))

		if (x == 0 and y == 1 and z == 0):
			return True
	return False

def is_b(frame):
	hand = frame.hands[0]
	#list of extended fingers:
	ext_fingers = hand.fingers.extended()
	
	#If there are four extended fingers and thumb is not one of them
	if (len(ext_fingers) == 4 and ext_fingers[0].type != 0):
		#rounded co-ordinates for all fingers, stored in respective arrays
		x = [int(round(ext_fingers[0].direction.x)), int(round(ext_fingers[1].direction.x)), int(round(ext_fingers[2].direction.x)), int(round(ext_fingers[3].direction.x))]
		y = [abs(int(round(ext_fingers[0].direction.y))), abs(int(round(ext_fingers[1].direction.y))), abs(int(round(ext_fingers[2].direction.y))), abs(int(round(ext_fingers[3].direction.y)))]
		z = [int(round(ext_fingers[0].direction.z)), int(round(ext_fingers[1].direction.z)), int(round(ext_fingers[2].direction.z)), int(round(ext_fingers[3].direction.z))]

		if (checkArray(x, 0) and checkArray(y, 1) and checkArray(z, 0)):
			return True #Only return True in this case, return False by default
	return False

def is_d(frame):
	hand = frame.hands[0]
	#get a list of only the extended fingers
	ext_fingers = hand.fingers.extended()
	# if debug:
	# 	print "length of array = " + str(len(ext_fingers))
	# 	print "types in the array = " + str([finger.type for finger in ext_fingers])
		#print "types array" + str(ext_fingers_types)

	#if there is only one extended finger and it is the index finger
	if (len(ext_fingers) == 1 and ext_fingers[0].type == 1):
		#get the floored x,y,z vals for finger direction
		#int ensures no decimal places
		#round rounds up number to 1 dp
		x = int(round(ext_fingers[0].direction.x))
		y = int(round(ext_fingers[0].direction.y))
		z = int(round(ext_fingers[0].direction.z))
		if debug: print "D " + str(x) + ", " + str(y) + ", " + str(z)
		if (x == 0 and abs(y) == 1 and z == 0):
			return True #Only True in this case, returns False by default
	return False

def is_l(frame):
	# debug = True
	hand = frame.hands[0]
	
	#list of extended fingers
	ext_fingers = hand.fingers.extended()
	ext_fingers_types = [finger.type for finger in ext_fingers]
	
	# if debug:
		# 	print "length of array = " + str(len(ext_fingers))
		# 	print "types in the array = " + str([finger.type for finger in ext_fingers])
	# 	print "types array" + str(ext_fingers_types)

	#Check length of ext_fingers and types. 
	if len(ext_fingers) == 2 and ext_fingers_types[0] == 0 and ext_fingers_types[1] == 1 :
		# if debug == True:
		#     print "Inside the function"

		#Set co-ordinates for thumb and finger
		#For the thumb, get the direction for distal bones
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

		if(abs(x_thumb) == 1 and y_thumb == 0 and z_thumb == 0
				and x_index == 0 and abs(y_index) == 1 and z_index == 0):
				return True #Only True in this case, return False by default
	return False

def is_h(frame):
	# debug = True
	hand = frame.hands[0]
	ext_fingers = hand.fingers.extended()
	#ext_finger_types = [finger.type for finger in ext_fingers]
	
	# if(debug == True):
	# 	print "Length of ext_fingers" + str(len(ext_fingers))
	# 	print "ext_fingers types " + str([finger.type for finger in ext_fingers])
	
	if(len(ext_fingers) == 2 and ext_fingers[0].type == 1 and ext_fingers[1].type == 2):
		# if debug == True:
		# 	print "Inside the function"
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

		if((abs(x_index) == 1 and y_index == 0 and z_index == 0 and abs(x_middle) == 1 and y_middle == 0 and z_middle == 0) or (x_index == 0 and y_index == 0 and abs(z_index) == 1 and x_middle == 0 and y_middle == 0 and abs(z_middle) == 1 and abs(x_palm) == 1)):
			return True #only true in this case, returns false by default
	return False

def is_g(frame):
	# debug = True
	hand = frame.hands[0]
	ext_fingers = hand.fingers.extended()
	#ext_finger_types = [finger.type for finger in ext_fingers]

	# if(debug == True):
	# 	print "Length of ext_fingers" + str(len(ext_fingers))
	# 	print "ext_fingers types " + str([finger.type for finger in ext_fingers])

	if(len(ext_fingers) == 1 and ext_fingers[0].type == 1):
		# if debug == True:
		# 	print "Inside the function"
		x_index = int(round(ext_fingers[0].direction.x))
		y_index = int(round(ext_fingers[0].direction.y))
		z_index = int(round(ext_fingers[0].direction.z))

		x_palm = int(round(hand.palm_normal.x))

		if debug:
			print "Index values [x,y,z]: " + str(x_index) + ", " + str(y_index) + ", " + str(z_index)
			print hand.palm_normal

		if((abs(x_index) == 1 and y_index == 0 and z_index == 0) or (x_index == 0 and y_index == 0 and abs(z_index) == 1 and abs(x_palm) == 1)):
			return True #only true in this case, returns false by default
	return False

def is_w(frame):
		# debug = True
	hand = frame.hands[0]
	
	#get a list of only the extended fingers
	ext_fingers = hand.fingers.extended()
	ext_fingers_types = [finger.type for finger in ext_fingers]
	
	# if there are three extended fingers and the fingers types are index, middle and ring
	if (len(ext_fingers) == 3 and (ext_fingers_types[0] == 1) and (ext_fingers_types[1] == 2) and (ext_fingers_types[2] == 3)):
		#floored x,y,z values for first extended finger
		x1 = int(round(ext_fingers[0].direction.x))
		y1 = int(round(ext_fingers[0].direction.y))
		z1 = int(round(ext_fingers[0].direction.z))
		
		#floored x,y,z values for second extended finger
		x2 = int(round(ext_fingers[1].direction.x))
		y2 = int(round(ext_fingers[1].direction.y))
		z2 = int(round(ext_fingers[1].direction.z))
		
		#floored x,y,z values for third extended finger
		x3 = int(round(ext_fingers[2].direction.x))
		y3 = int(round(ext_fingers[2].direction.y))
		z3 = int(round(ext_fingers[2].direction.z))

		if debug == True:
			print "Thumb values [x,y,z]: " + str(x1) + ", " + str(y1) + ", " + str(z1)
			print "Index values [x,y,z]: " + str(x2) + ", " + str(y2) + ", " + str(z2)
			print "Middle values [x,y,z]: " + str(x3) + ", " + str(y3) + ", " + str(z3)
	
		#x,y,z coordinates for three extended fingers should be (0,1,0)
		if(x1 == 0 and y1 == 1 and z1 == 0 and x2 == 0 and y2 == 1 
			and z2 == 0 and x3 == 0 and y3 == 1 and z3 == 0):
			return True	#only returns true in this case, returns false by default
	return False

def is_r_1(frame):
		# debug = True
	hand = frame.hands[0]
	
	#get a list of only the extended fingers
	ext_fingers = hand.fingers.extended()
	ext_fingers_types = [finger.type for finger in ext_fingers]
	
	# if there are three extended fingers and the fingers types are index, middle and ring
	if (len(ext_fingers) == 2 and (ext_fingers_types[0] == 1) and (ext_fingers_types[1] == 2)):
		#x,y,z values for first extended finger
		x1 = int(ext_fingers[0].direction.x)
		y1 = int(round(ext_fingers[0].direction.y))
		z1 = int(round(ext_fingers[0].direction.z))
		
		#x,y,z values for second extended finger
		x2 = int(ext_fingers[1].direction.x)
		y2 = int(round(ext_fingers[1].direction.y))
		z2 = int(round(ext_fingers[1].direction.z))
		
	
		if debug == True:
			print "Index values [x,y,z]: " + str(x1) + ", " + str(y1) + ", " + str(z1)
			print "Middle values [x,y,z]: " + str(x2) + ", " + str(y2) + ", " + str(z2)
	
	
		#y,z coordinates for index and middle fingers should be 1,0 respectively. Difference between x values of two fingers should not be zero.
		if hand.is_right:
			if(y1 == 1 and z1 == 0 and y2 == 1 
				and z2 == 0 and (x1-x2)>0.25): 
				return True
			else:
				return False
		elif hand.is_left:
			if(y1 == 1 and z1 == 0 and y2 == 1 
				and z2 == 0 and (x2-x1)>0.25): 
				return True
			else:
				return False		
	else:
		return False

def is_r_2(frame):
		# debug = True
	hand = frame.hands[0]
	
	#get a list of only the extended fingers
	ext_fingers = hand.fingers.extended()
	ext_fingers_types = [finger.type for finger in ext_fingers]
	
	# if there are three extended fingers and the fingers types are index, middle and ring
	if (len(ext_fingers) == 2 and (ext_fingers_types[0] == 1) and (ext_fingers_types[1] == 2)):
		#x,y,z values for first extended finger
		#x1 = int(ext_fingers[0].direction.x))
		y1 = int(round(ext_fingers[0].direction.y))
		z1 = int(round(ext_fingers[0].direction.z))
		
		#x,y,z values for second extended finger
		#x2 = int(ext_fingers[1].direction.x))
		y2 = int(round(ext_fingers[1].direction.y))
		z2 = int(round(ext_fingers[1].direction.z))
		
	
		if debug == True:
			print "Index values [y,z]: " + ", " + str(y1) + ", " + str(z1)
			print "Middle values [y,z]: " + ", " + str(y2) + ", " + str(z2)
	
		#y and z coordinates for both extended fingers should be 1 and 0 respectively. 
		if(y1 == 1 and z1 == 0 and y2 == 1 and z2 == 0):
			#if right hand, finger with largest x co-ordinate should be index finger
			if hand.is_right:
				if (ext_fingers.rightmost.type==0 or ext_fingers.rightmost.type==1):
					return True
				else:
					return False
				
			#if left hand, finger with smallest x co-ordinate should be index finger
			elif hand.is_left:
				if (ext_fingers.leftmost.type==0 or ext_fingers.leftmost.type==1):
					return True
				else:
					return False		
		else:
			return False

