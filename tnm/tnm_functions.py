#Train model functions file, to simplify calculations needed in Interface

#Function to delegate variables when Emergency Brake triggered
def EmergencyBraking(eBrake):
	if(self.eBrake != True):
		self.eBrake = True
		print(self.eBrake)
			


#Set Speed (MPH) Based on Power command from Train Controller
def set_curr_speed(Power, Occupancy):
	max_speed = 43.5	#miles/hour
	train_accl = 1.12 		#miles/hour
	Empty_Mass = 5*40.9		#Tons
	Occupancy_Mass = ((Occupancy*56.699)/2000) #Number -> Kg -> tons
	
	
	#Force = M*A & Velocity = Power/M*A
	curr_mass = (Empty_Mass + Occupancy_Mass)*907.185		#tons*kg const = kg <--
	force = (curr_mass*train_accl)
	curr_speed = (Power / force)
	
	if(curr_speed > max_speed):
		curr_speed = max_speed
	
	#round the speed to a integer
	curr_speed = round(curr_speed, 1)
	return curr_speed

#Setting internal temperature of the train 
def temp_control(set_temp, curr_temp):
	#initialize current temperature to 68 deg.
	
	#if there is a disparity in temperature, calculate the difference and increase/decrease the curr temp accordingly
	if(set_temp != curr_temp):
		if(set_temp >= curr_temp):
			temp_diff = (set_temp - curr_temp)
			for x in range(temp_diff):
				curr_temp = curr_temp + 1
		elif(set_temp < curr_temp):
			temp_diff = (curr_temp - set_temp)
			for x in range(temp_diff):
				curr_temp = curr_temp - 1	
		else:
			set_temp = curr_temp
			curr_temp = curr_temp
	
	#set Max and Min temperature range for the Cabin
	if(curr_temp < 60):
		curr_temp = 60
	elif(curr_temp > 80):
		curr_temp = 80
	
	return curr_temp
	
#function to determine the current occupancy of a single train
def pass_crew_count(p, c):
	
	#initialize pass_count and crew_count
	pass_count = p
	crew_count = c
	
	Occupancy = pass_count + crew_count
	
	return Occupancy
	

#function to calculate stopping distance
def stopping_dist(curr_speed):
	
	#For Service Braking
	curr_speed_mps = (curr_speed/2.237)
	service_dec = 2.84		#MPH
	service_dec_mps = (service_dec/2.237)
	service_stop_time = (curr_speed_mps/service_dec_mps)	#seconds
	service_stop_distance = ((curr_speed_mps/2)*service_stop_time)
	print(round(service_stop_distance,0))
	
	#For Emergency Braking
	eBrake_dec = 6.11		#MPH
	eBrake_dec_mps = (eBrake_dec/2.237)
	eBrake_stop_time = (curr_speed_mps/eBrake_dec_mps)	#seconds
	eBrake_stop_distance = ((curr_speed_mps/2)*eBrake_stop_time)
	print(round(eBrake_stop_distance, 0))
	

#Function to convert between KPH and MPH
def KilotoMile(comm_speed):
	
	#Use commanded speed on the track KPH, but convert to Miles/Hour
	speed_MPH = (comm_speed / 1.60934)
	
	return speed_MPH
	

