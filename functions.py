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
		
		if all(y == 0 for y in y_val):
			return True
		else:
			return False
	else:
		return False

def is_d(frame):
    hand = frame.hands[0]

    #get a list of only the extended fingers
    ext_fingers = hand.fingers.extended()

    #if there is only one extended finger and it is the index finger
    if (len(ext_fingers) == 1 and ext_fingers[0].type == "TYPE_INDEX"):

        #get the floored x,y,z vals for finger direction
        x = int(round(ext_fingers[0].direction.x))
        y = int(round(ext_fingers[0].direction.y))
        z = int(round(ext_fingers[0].direction.z))
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
		and ("TYPE_MIDDLE" in ext_fingers_types) and ("TYPE_RING" in ext_fingers_types)):
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
		
		#x,y,z coordinates for three extended fingers should be (0,1,0)
		if(x1 == 0 and y1 == 1 and z1 == 0 and x2 == 0 and y2 == 1 
			and z2 == 0 and x3 == 0 and y3 == 1 and z3 == 0):
			return True
		else:
			return False
			
	else:
		return False

