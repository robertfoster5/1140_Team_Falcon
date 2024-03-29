import xlrd
from tkm_class import Block
from tkm_class import Station
from tkm_class import Train 

#1 for 2 sig fig, other for 0
def m_to_f(num,r):
	if r == 1:
		feet = round(num*3.2808,2)
		return feet
		
	else:
		feet = round(num*3.2808,0)
		return feet

#farenthieght to celcius
def f_to_c(num):
	numb = num - 32
	numb = (numb*5)/9
	return numb

#kilometers per hour to miles per hour
def ms_to_mph(num):
	num = round(num*2.23694,2)	
	return num

#useless ignore
def up_x(x):
	x = x+62
	return x

#return train data
def make_data_t(train,blocks):
	
	if(blocks[int(train.block-1)].station.name != 0):
		sl = blocks[int(train.block-1)].station.name
		sb = train.dis
		sd = train.boar
	else:
		sl = sb = sd = 'n/a'	
	
	data = [
		['Train Number', train.num],
		['# Passengers', train.occ],
		['Block Location', train.block],
		['Direction of Travel', train.way],
		['Station Location', sl],
		['Disembarking', sb],
		['Boarding', sd]
	]
	return data

#return station data
def make_data_s(stat):	
	data = [
		['Station Name', stat.station.name],
		['Station Side', stat.station.side],
		['Ticket Sales', stat.station.sales],
		['# People at Station', stat.station.occ],
		['Station Block Number', stat.num]
	]
	return data

#return all station data
def make_data_sall(blocks):
	i = 0
	data = []
	while i < len(blocks):
		if blocks[i].station.name != 0:
			data.append([blocks[i].station.name,blocks[i].station.side,blocks[i].station.sales,blocks[i].station.occ,blocks[i].num])
		i = i+1
		
	return data


#return Block data
def make_data(blocks,j):	
	if blocks[j].station.name == 0:
		sn = "None"
	else:
		sn = blocks[j].station.name
		
	if blocks[j].switch.bottom == 0:
		sb = "None"
	else:
		if blocks[j].switch.state == 0:
			sb = blocks[j].switch.top
		else:
			sb = blocks[j].switch.bottom
	
	if blocks[j].cross == 0:
		c = "None"
	else:
		c = blocks[j].cross.state
		
	if blocks[j].beacon1 != 0:
		bid = bin(blocks[j].beacon1)
	else:
		bid = "N/a"
	
	if blocks[j].occ == 1:
		oc = "Occupied"
	else:
		oc = "Empty"
		
	if blocks[j].health == 1:
		er = "Malfunction"
	else:
		er = "Operational"
	
	
	data = [
	 ["Section", blocks[j].sect],
	 ["Number", blocks[j].num],
	 ["Length", m_to_f(blocks[j].length,0)],
	 ["Grade", blocks[j].grade],
	 ["Speed Limit", ms_to_mph(blocks[j].s_limit)],
	 ["Block Station", sn],
	 ["Switch", sb],
	 ["Switch State", blocks[j].switch.state],
	 ["Crossing", c],
	 ["Elevation", m_to_f(blocks[j].elev,1)],
	 ["Cumulative Elevation", m_to_f(blocks[j].c_elev,1)],
	 ["Underground", blocks[j].und],
	 ["Beacon ID", bid],
	 ["Occupancy", oc],
	 ["Block Error", er]
	]
	return data
	
#generate section of track data to display
def make_data_sect(blocks,sect):
	i = 0
	start = 0
	finish = 0
	while i < len(blocks):
		if str(sect) == blocks[i].sect:
			start = i
			finish = i
			while finish < len(blocks) and blocks[finish].sect == str(sect):
				finish = finish+1
			finish = finish-1
			i = len(blocks)
		i = i+1
	
	if start == 0 and finish == 0:
		return ["does not exist",0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	num = finish - start + 1
	data = []
	while start <= finish:
		if blocks[start].station.name == 0:
			sn = "None"
		else:
			sn = blocks[start].station.name
			
		if blocks[start].switch.bottom == 0:
			sb = "None"
		else:
			if blocks[start].switch.state == 0:
				sb = blocks[start].switch.top
			else:
				sb = blocks[start].switch.bottom
		
		if blocks[start].cross == 0:
			c = "None"
		else:
			c = blocks[start].cross.state
			
		if blocks[start].beacon1 != 0:
			bid = bin(blocks[start].beacon1)
		else:
			bid = "N/a"
		
		if blocks[start].occ == 1:
			oc = "Occupied"
		else:
			oc = "Empty"
			
		if blocks[start].health == 1:
			er = "Malfunction"
		else:
			er = "Operational"
			
		data.append([blocks[start].num,m_to_f(blocks[start].length,0),blocks[start].grade,ms_to_mph(blocks[start].s_limit),sn,sb,blocks[start].switch.state,c,m_to_f(blocks[start].elev,1),m_to_f(blocks[start].c_elev,1),blocks[start].und,bid,oc,er])
		start = start+1
		
	return data

#loading in a new track
def load_track(fileN):
	File = xlrd.open_workbook(fileN)
	j = 1
	
	t_file = File.sheet_by_index(0)
	
	track = []
	
	while t_file.cell(j,2).value != 0:
		if t_file.cell(j,6).value == xlrd.empty_cell.value:
			track.append(Block(t_file.cell(j,0).value,t_file.cell(j,1).value,t_file.cell(j,2).value,t_file.cell(j,3).value,t_file.cell(j,4).value,t_file.cell(j,5).value,0,[0,0],[0,0],0,t_file.cell(j,7).value,t_file.cell(j,8).value,t_file.cell(j,9).value,t_file.cell(j,10).value))
		#if station		
		else:	
			name = str(t_file.cell(j,6).value)
			if name[0:8] == "Station;" or name[0:8] == "STATION;":
				n = name[9:]
				
				track.append(Block(t_file.cell(j,0).value,t_file.cell(j,1).value,t_file.cell(j,2).value,t_file.cell(j,3).value,t_file.cell(j,4).value,t_file.cell(j,5).value,n,[0,0],[0,0],0,t_file.cell(j,7).value,t_file.cell(j,8).value,t_file.cell(j,9).value,t_file.cell(j,10).value))
			#if there is a yard switch
			elif name[7:11] == "FROM":
				swit_t = [int(name[23:25]),"YARD"]
				swit_b = [0,0]
				
				track.append(Block(t_file.cell(j,0).value,t_file.cell(j,1).value,t_file.cell(j,2).value,t_file.cell(j,3).value,t_file.cell(j,4).value,t_file.cell(j,5).value,0,swit_t,swit_b,0,t_file.cell(j,7).value,t_file.cell(j,8).value,t_file.cell(j,9).value,t_file.cell(j,10).value))
				
			elif name[7:9] == "TO":
				if name[21] == "9":
					swit_b = ["YARD",int(name[21])]
				else:
					swit_b = ["YARD",int(name[16:18])]
				swit_t = [0,0]
				
				track.append(Block(t_file.cell(j,0).value,t_file.cell(j,1).value,t_file.cell(j,2).value,t_file.cell(j,3).value,t_file.cell(j,4).value,t_file.cell(j,5).value,0,swit_t,swit_b,0,t_file.cell(j,7).value,t_file.cell(j,8).value,t_file.cell(j,9).value,t_file.cell(j,10).value))
			#if there is a switch
			elif name[0:6] == "Switch" or name[0:6] == "SWITCH":
				swit_t = [0,0]
				swit_b = [0,0]
				
				#first block of switch
				k = 8
				while 1:
					if name[k] == ';':
						break
					elif name[k] == '-':
						k = k+1
						ind = k
					else:
						k = k+1
				
				swit_t[0] = int(name[8:ind-1])
				swit_t[1] = int(name[ind:k])
				
				#second block of switch
				z = k+1
				while 1:
					if name[k] == ')':
						break
					elif name[k] == '-':
						k = k+1
						ind = k
					else:
						k = k+1
				
				swit_b[0] = int(name[z:ind-1])
				swit_b[1] = int(name[ind:k])
				
					
				track.append(Block(t_file.cell(j,0).value,t_file.cell(j,1).value,t_file.cell(j,2).value,t_file.cell(j,3).value,t_file.cell(j,4).value,t_file.cell(j,5).value,0,swit_t,swit_b,0,t_file.cell(j,7).value,t_file.cell(j,8).value,t_file.cell(j,9).value,t_file.cell(j,10).value))
			#if there is a crossing
			elif name == "RAILWAY CROSSING" or name == "Railway Crossing" or name == "Railway crossing" or name == "railway crossing":
				track.append(Block(t_file.cell(j,0).value,t_file.cell(j,1).value,t_file.cell(j,2).value,t_file.cell(j,3).value,t_file.cell(j,4).value,t_file.cell(j,5).value,0,[0,0],[0,0],1,t_file.cell(j,7).value,t_file.cell(j,8).value,t_file.cell(j,9).value,t_file.cell(j,10).value))
			
		j = j+1
		
	return track;
	

