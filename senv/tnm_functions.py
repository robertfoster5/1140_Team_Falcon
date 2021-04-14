#Train model functions file, to simplify calculations needed in Interface
from t_time import timing


#Function to delegate variables when Emergency Brake triggered
def EmergencyBraking(eBrake):
	if(self.eBrake != True):
		self.eBrake = True
		print(self.eBrake)
			


#Set Speed (MPH) Based on Power command from Train Controller
def set_curr_speed(timeSec, EmerBrake, SerBrake, Authority, Power, Occupancy, Velocity):
	#Variables defined:
	Velocity = MiletoMeter(Velocity)		#Convert MPH to mps for calculations
	curr_speed = Velocity
	max_speed = 43.5			#miles/hour
	train_accl_max = 0.5006848		#mps2 from max 1.12 miles/hour^2
	train_dec_service = 1.2 		#mph2 deceleration service
	train_dec_eBrake = 2.73			#mph2 decleration eBrake
	Empty_Mass = 5*40.9			#Tons
	Occupancy_Mass = ((Occupancy*56.699)/2000) #Number -> (125lb)Kg -> tons
	#current mass based on ticket sales and inital train mass
	curr_mass = (Empty_Mass + Occupancy_Mass)*907.185		#tons*kg const = kg <--	


	#current acceleration = change in v/change in t			#acc continues to change changing
	#Force = M*A & Velocity = Power/M*A
	
	#First checking if emergency brake is triggered
	if(EmerBrake == True):
		#check if train has stopped. Display 0 speed
		if(Velocity == 0.0):
			force = 0.0
			curr_accl = 0.0
			curr_speed = 0.0
		#Slow down train using eBrake deceleration till 0.0
		elif(Velocity > 0.0):
			force = (curr_mass*train_dec_eBrake)
			curr_accl = train_dec_eBrake
			curr_speed = meterToMile(curr_accl/timeSec)
	#Second, check if train has authority to speed up and move forward
	elif(EmerBrake == False):
		#without eBrake, check authority, if 0 start stopping using service deceleration
		if(Authority == False and SerBrake == True):
			if(Velocity > 0.0 and Power == 0.0):
				force = (curr_mass*train_dec_service)
				curr_accl = train_dec_service
				curr_speed = meterToMile(curr_accl/timeSec)
			elif(Velocity == 0.0):
				force = 0.0
				curr_accl = 0.0
				curr_speed = 0.0
		#if authority is true, calculate speed based on Power and Vn-1 speed, using Max accleration
		elif(Authority == True and SerBrake == False):
			if(timeSec == 0):
				force = 0.0
				curr_speed = 0.0
			elif(timeSec > 0 and Velocity == 0.0):
				force = (curr_mass*train_accl_max)
				curr_accl = train_accl_max 			#max mps2 from 1.12 mph2		set to max accl to start
				curr_speed = meterToMile(curr_accl/timeSec)						#Calculate V = A/s and convert to mph	 #***Point of Failure
			elif(timeSec > 0 and Velocity > 0.0):
				force = (Power/Velocity)
				curr_accl = (force/curr_mass)
				curr_speed = meterToMile(curr_accl/timeSec)				#Calculate V = A/s and convert to mph

	if(curr_speed > max_speed):
		curr_speed = max_speed
		
	#round the speed to a integer
	print(str(curr_speed) + " curr speed at " + str(timeSec))
	curr_speed = round(curr_speed, 2)
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
	

#Function to convert between mps and MPH
def meterToMile(curr_speed):
	
	#Use commanded speed on the track KPH, but convert to Miles/Hour
	speed_MPH = (curr_speed * 2.23694)
	
	return speed_MPH

#Function to convert between MPH and mps
def MiletoMeter(curr_speed):
	
	#Use commanded speed on the track KPH, but convert to Miles/Hour
	speed_mps = (curr_speed / 2.23694)
	
	return speed_mps
	
