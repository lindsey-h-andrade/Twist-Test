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
	#TODO: Add option for testing all samples in the file. Might run into an issue if some samples don't have sintered results yet. 


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

	twistDirection = findTwistDirection(greenAvgData, sinteredAvgData)
	if twistDirection == 1: 
		print('CCW')
	elif twistDirection == 0: 
		print('CW')
	elif twistDirection == None:
		print('Error in twist direction')
	print('\n')

	#TODO: Should probably output all data into a file at somepoint instead of having to manually copy down values. 

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

	# Go through each row and pull out the user specified samples. Stick the vectors for the wanted samples into a raw data array. 
	for row in datalist: 
		column = row.split(',')

		if str(sample) in column[1].strip()[:-1]: # Looking for the sample number in the first digits of the run number column (ignoring the last digit)
			side1 = [float(column[2].strip()), float(column[3].strip()), float(column[4].strip())]
			side2 = [float(column[5].strip()), float(column[6].strip()), float(column[7].strip())]
			side3 = [float(column[8].strip()), float(column[9].strip()), float(column[10].strip())]
			side4 = [float(column[11].strip()), float(column[12].strip()), float(column[13].strip())]

			greenRawSides.append([side1, side2, side3, side4])


	# Initalize side arrays with floats
	side1Sum = [0.0, 0.0, 0.0]
	side2Sum = [0.0, 0.0, 0.0]
	side3Sum = [0.0, 0.0, 0.0]
	side4Sum = [0.0, 0.0, 0.0]

	avgData = []
	greenRunsNum = len(greenRawSides) # Number of runs done per sample. Will usually be 3
	#TODO: Test if samples have more/less than 3 runs. I'm pretty sure it'll work but who knows...

	# Add all the X, Y, and Z values for a given side. (Add all the X's for side 1. Add all the X's for side 2....)
	for i in range(greenRunsNum): 
		side1Sum = [x + y for x, y in zip(side1Sum, greenRawSides[i][0])]
		side2Sum = [x + y for x, y in zip(side2Sum, greenRawSides[i][1])]
		side3Sum = [x + y for x, y in zip(side3Sum, greenRawSides[i][2])]
		side4Sum = [x + y for x, y in zip(side4Sum, greenRawSides[i][3])]

	# Divide each sum by the number of runs (taking an average)
	side1Avg = [x / greenRunsNum for x in side1Sum] 
	side2Avg = [x / greenRunsNum for x in side2Sum]
	side3Avg = [x / greenRunsNum for x in side3Sum]
	side4Avg = [x / greenRunsNum for x in side4Sum]

	#Stick it all into an array! 
	avgData = [side1Avg, side2Avg, side3Avg, side4Avg]

	return avgData

def findAngleBetweenSides(greenAvgData, sinteredAvgData):
	# Just uses vector math to find the angle between the two vectors. Source for math: http://onlinemschool.com/math/library/vector/angl/ 
	angle1 = acos(dot(greenAvgData[0], sinteredAvgData[0])/(mag(greenAvgData[0])*mag(sinteredAvgData[0])))
	angle2 = acos(dot(greenAvgData[1], sinteredAvgData[1])/(mag(greenAvgData[1])*mag(sinteredAvgData[1])))
	angle3 = acos(dot(greenAvgData[2], sinteredAvgData[2])/(mag(greenAvgData[2])*mag(sinteredAvgData[2])))
	angle4 = acos(dot(greenAvgData[3], sinteredAvgData[3])/(mag(greenAvgData[3])*mag(sinteredAvgData[3])))

	return [angle1, angle2, angle3, angle4]

def findTwistDirection(greenAvgData, sinteredAvgData):
	# Find z component of the cross product of {greenSide1 x sinteredSide1}. 
	# Positive = CCW Twist -- 1
	# Negavtive = CW Twist -- 0

	print(greenAvgData)

	greenSide1 = greenAvgData[0]
	sinteredSide1 = sinteredAvgData[0]

	direction = greenSide1[1]*sinteredSide1[2] - greenSide1[2]*sinteredSide1[1]

	if direction > 0: 
		return 1
	elif direction < 0: 
		return 0


def dot(vect1, vect2): 
	# Just a function to find the dot product between two vectors
	return vect1[0] * vect2[0] + vect1[1] * vect2[1] + vect1[2] * vect2[2]

def mag(vect): 
	# Just a function to find magnitudes of vectors
	return sqrt(vect[0]**2 + vect[1]**2 + vect[2]**2)


if __name__ == '__main__':
	main()
	exitinput = input("")