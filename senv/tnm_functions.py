#Train model functions file, to simplify calculations needed in Interface
from t_time import timing


#Function to delegate variables when Emergency Brake triggered
def EmergencyBraking(eBrake):
	if(self.eBrake != True):
		self.eBrake = True
		print(self.eBrake)
			


#Set Speed (MPH) Based on Power command from Train Controller
def set_curr_speed(timeSec, EmerBrake, SerBrake, Authority, Power, Occupancy, SpeedN1, AcclN1, CommSpeed):
	#Variables defined:
	AcclN1 = MiletoMeter(AcclN1)
	curr_accl = AcclN1										#Just an initialization, will be recalculated
	SpeedN1 = MiletoMeter(SpeedN1)							#Convert MPH to mps for calculations
	curr_speed = SpeedN1									#Just an initialization, will be recalculated
	max_speed = 43.5										#miles/hour , used at the end once converted back
	train_accl_max = 0.5006848		#actually the median (2/3 of load)#mps2 from max 1.12 miles/hour^2
	#train_accl_max = 0.75
	train_dec_service = MiletoMeter(1.2) 			#mph2 deceleration service
	train_dec_eBrake = MiletoMeter(2.73)				#mph2 decleration eBrake
	Empty_Mass = 5*40.9					#Tons
	Occupancy_Mass = ((Occupancy*56.699)/2000) #Number -> (125lb)Kg -> tons
	#current mass based on ticket sales and inital train mass
	curr_mass = (Empty_Mass + Occupancy_Mass)*907.185		#tons*kg const = kg <--	
	time_initial = 0


	#print(str(round(Power,0)) + " W of Power")
	#current acceleration = change in v/change in t			#acc continues to change changing
	#Force = M*A & Velocity = Power/M*A
	
	#First checking if emergency brake is triggered
	if(EmerBrake == True):
		Power = 0
		#check if train has stopped. Display 0 speed
		if(SpeedN1 == 0.0):
			force = 0.0
			curr_accl = 0.0
			curr_speed = 0.0
			#print("Train has stopped, eBrake")
		#Slow down train using eBrake deceleration till 0.0
		elif(SpeedN1 > 0.0):
			force = (Power/curr_speed)
			curr_accl = train_dec_eBrake
			curr_speed = meterToMile(SpeedN1 - ((time_initial + 1)/2)*(curr_accl))		#time_initial + 1 = currTime - currTime_n-1
			if(curr_speed < 0.0):
				curr_speed = 0.0
				print("Train has stopped, eBrake")
			
	#Second, check if train has authority to speed up and move forward
	elif(EmerBrake == False):
		#without eBrake, check authority, if 0 start stopping using service deceleration
		if(Authority == False and SerBrake == True):
			#Display stopping distance based on current speed
			#stopping_dist(curr_speed)
			if(SpeedN1 > 0.0 and Power == 0.0):
				force = (Power/curr_speed)
				curr_accl = train_dec_service
				curr_speed = meterToMile(SpeedN1 - ((time_initial + 1)/2)*(curr_accl))		#timeSec - time_initial 
				if(curr_speed < 0.0):
					curr_speed = 0.0
					print("Train has stopped, service")
			elif(SpeedN1 == 0.0):
				force = 0.0
				curr_accl = 0.0
				curr_speed = 0.0
				#print("Train has stopped, service")
		#if authority is true, calculate speed based on Power and Vn-1 speed, using Max accleration
		elif(Authority == True and SerBrake == True):
			#time_initial = 0
			if(timeSec == 0):
				force = 0.0
				curr_speed = 0.0
			elif(timeSec > 0 and SpeedN1 == 0.0):
				force = 0.0
				curr_accl = 0.0		#train_dec_service
				curr_speed = 0.0
				#print("Train has stopped, service")
			elif(timeSec > 0 and SpeedN1 > 0.0):
				force = (Power/curr_speed)
				curr_accl = train_dec_service
				curr_speed = meterToMile(SpeedN1 - ((time_initial + 1)/2)*(curr_accl))			#Calculate Vn = Vn-1 + T/2(an +an-1) and convert to mph
				if(curr_speed < 0.0):
					curr_speed = 0.0
					print("Train has stopped, service")
		#else if authority is true, calculate speed based on Power and Vn-1 speed, using Max accleration
		elif(Authority == True and SerBrake == False and SpeedN1 < CommSpeed):
			#time_initial = 0
			if(timeSec == 0):
				force = 0.0
				curr_speed = 0.0
			elif(timeSec > 0 and SpeedN1 == 0.0):
				#time_initial = timeSec
				force = 94400 #140000	at 0.75 mps2 max speed			#Max estimated force N for max accelertion
				curr_accl = (force/curr_mass) 							#max 0.50 mps2		set to max accl to start
				curr_speed = meterToMile(curr_accl/1)				#Calculate V = A/s and convert to mph	 #***Point of Failure
				#curr_speed = meterToMile(SpeedN1 + ((time_initial + 1)/2)*(curr_accl + AcclN1))
			elif(timeSec > 0 and SpeedN1 > 0.0):
				force = (Power/curr_speed)
				curr_accl = (force/curr_mass)
				curr_speed = meterToMile(SpeedN1 + ((time_initial + 1)/2)*(curr_accl + AcclN1))			#Calculate Vn = Vn-1 + T/2(an +an-1) and convert to mph
		elif(Authority == True and SerBrake == False and SpeedN1 > CommSpeed):
			force = (Power/curr_speed)
			curr_accl = train_dec_service
			curr_speed = meterToMile(SpeedN1 - ((time_initial + 1)/2)*(curr_accl))
			if(curr_speed < 0.0):
				curr_speed = 0.0
				print("Train has stopped, service")
		elif(Authority == True and SerBrake == False and SpeedN1 == CommSpeed):
			force = 0.0
			curr_accl = 0.0
			curr_speed = meterToMile(SpeedN1)

	#Check to make sure speed doesn't exceed Max
	if(curr_speed > max_speed):
		curr_speed = max_speed
		
	#round the speed to a integer
	print(str(round(curr_speed, 2)) + " mph curr speed at " + str(timeSec))
	curr_speed = round(curr_speed, 2)
	curr_accl = meterToMile(curr_accl)
	
	return curr_speed, curr_accl;


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
	print(str(service_stop_time) + " service stop time")
	print(str(round(service_stop_distance,0)) + " service brake stop dist")
	
	#For Emergency Braking
	eBrake_dec = 6.11		#MPH
	eBrake_dec_mps = (eBrake_dec/2.237)
	eBrake_stop_time = (curr_speed_mps/eBrake_dec_mps)	#seconds
	eBrake_stop_distance = ((curr_speed_mps/2)*eBrake_stop_time)
	#print(str(round(eBrake_stop_distance, 0)) + " eBrake stop dist")
	

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
	
