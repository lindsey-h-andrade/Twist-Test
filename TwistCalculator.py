from math import acos
from math import sqrt

def getSampleNumber():
	SAMPLE = input("Sample number in Data: ")

	try: # Check if number, if not number ask again. 
		SAMPLE = int(SAMPLE)
		return SAMPLE
	except: 
		print('Only enter intergers')
		getSampleNumber() # Ask again until an int is inputed


# def findSampleRow(data):
# 	# Ask for green data

# 	for row in data: 
# 		columns = [x.strip() for x in my_string.split(',')]
# 		for item in columns


def main(greenFileLoc = None, sinterFileLoc = None): 
	print('-----')

	if greenFileLoc == None and sinterFileLoc == None: 
		# Ask for green results file location
		greenFileLoc = input("Enter (or drag and drop) file location of green data: ")
		sinterFileLoc = input("Enter (or drag and drop) file location of sintered data: ")
	
	print('\n')
	SampleNum = getSampleNumber() # This returns an INT


	greenData = open(greenFileLoc.strip('"'), 'r').read().split('\n') #open for read only so we don't overwrite anything by accident
	greenData = list(filter(None, greenData)) # Remove any empty lines

	sinterData = open(sinterFileLoc.strip('"'), 'r').read().split('\n') 
	sinterData = list(filter(None, sinterData))

	greenAvgData =  averageSideData(greenData, SampleNum)
	sinteredAvgData = averageSideData(sinterData, SampleNum)

	print("-\n")
	angles = findAngleBetweenSides(greenAvgData, sinteredAvgData)
	print(angles)

	print("Average Twist (rad): %f" %((angles[0] + angles[1] + angles[2] + angles[3])/4))
	print("\n")

	AGAIN = input("Calculate another sample? [y/n]: ")
	print("\n")

	if AGAIN == "y": 
		SAMEDATA = input("Use same data? [y/n] ")
		if SAMEDATA == 'y': 
			main(greenFileLoc, sinterFileLoc)
		else: 
			main()
	elif AGAIN == "n": 
		return

def averageSideData(datalist, sample):

	greenRawSides = []

	sampleCount = 0

	for row in datalist: 
		column = row.split(',')
		# print(column[1].strip()[1])
		if str(sample) in column[1].strip()[0]: # Looking for the sample number in the first digit of the run number column
			side1 = [float(column[2].strip()), float(column[3].strip()), float(column[4].strip())]
			side2 = [float(column[5].strip()), float(column[6].strip()), float(column[7].strip())]
			side3 = [float(column[8].strip()), float(column[9].strip()), float(column[10].strip())]
			side4 = [float(column[11].strip()), float(column[12].strip()), float(column[13].strip())]

			greenRawSides.append([side1, side2, side3, side4])
			sampleCount = sampleCount + 1 # Count how many runs each sample has

	side1Sum = [0.0, 0.0, 0.0]
	side2Sum = [0.0, 0.0, 0.0]
	side3Sum = [0.0, 0.0, 0.0]
	side4Sum = [0.0, 0.0, 0.0]
	# for i in greenDataArray: 

	avgData = []
	greenRunsNum = len(greenRawSides) # Number of runs done per sample

	for i in range(greenRunsNum): 
		side1Sum = [x + y for x, y in zip(side1Sum, greenRawSides[i][0])]
		side2Sum = [x + y for x, y in zip(side1Sum, greenRawSides[i][1])]
		side3Sum = [x + y for x, y in zip(side1Sum, greenRawSides[i][2])]
		side4Sum = [x + y for x, y in zip(side1Sum, greenRawSides[i][3])]


	side1Avg = [x / greenRunsNum for x in side1Sum] 
	side2Avg = [x / greenRunsNum for x in side2Sum]
	side3Avg = [x / greenRunsNum for x in side3Sum]
	side4Avg = [x / greenRunsNum for x in side4Sum]

	avgData = [side1Avg, side2Avg, side3Avg, side4Avg]

	return avgData

def findAngleBetweenSides(greenAvgData, sinteredAvgData):
	angle1 = acos(dot(greenAvgData[0], sinteredAvgData[0])/(mag(greenAvgData[0])*mag(sinteredAvgData[0])))
	angle2 = acos(dot(greenAvgData[1], sinteredAvgData[1])/(mag(greenAvgData[1])*mag(sinteredAvgData[1])))
	# inside3 = dot(greenAvgData[2], sinteredAvgData[2])/(mag(greenAvgData[2])*mag(sinteredAvgData[2]))
	# print(inside3)
	angle3 = acos(dot(greenAvgData[2], sinteredAvgData[2])/(mag(greenAvgData[2])*mag(sinteredAvgData[2])))
	angle4 = acos(dot(greenAvgData[3], sinteredAvgData[3])/(mag(greenAvgData[3])*mag(sinteredAvgData[3])))

	return [angle1, angle2, angle3, angle4]
def dot(vect1, vect2): 
	return vect1[0] * vect2[0] + vect1[1] * vect2[1] + vect1[2] * vect2[2]

def mag(vect): 
	return sqrt(vect[0]**2 + vect[1]**2 + vect[2]**2)


if __name__ == '__main__':
	main()
	exitinput = input("")