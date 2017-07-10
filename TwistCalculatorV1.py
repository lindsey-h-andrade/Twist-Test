import csv
import sys

initialDataFileLocation = input('Green Data: ').strip('\"')

initialDataFile = csv.reader(open(initialDataFileLocation))

initialDataDict = {}

testruns = 0

for row in initialDataFile: 
	# if len(row) == 15: # 4 cornered shape
	# 	corners = {1: [float(row[2]), float(row[3])], 
	# 				2: [float(row[4]), float(row[5])], 
	# 				3: [float(row[6]), float(row[7])], 
	# 				4: [float(row[8]), float(row[9])]}
	if len(row) == 15: 
		sideVectors = {1: [float(row[2]), float(row[3]), float(row[4])], 
					2: [float(row[5]), float(row[6]), float(row[7])], 
					3: [float(row[8]), float(row[9]), float(row[10])],
					4: [float(row[11]), float(row[12]), float(row[13])]}
	else: 
		print("Not a recognized shape.")

	samples = samples + 1

	initialDataDict[row[1].strip()] = sideVectors

print('raw: ')
print(initialDataDict)



# # -----------------------------
# # Vector Stuff

# initialVectorDict = {}
# # Sample: {
# # 	Corner: {X, Y}
# # 	Corner: {X, Y}
# # 	Corner: {X, Y}
# # 	Corner: {X, Y}
# # }

# for sample in initialDataDict.keys():
# 	sideVectors = {}
# 	for corner in initialDataDict[sample]: 
# 		if corner != 4: 
# 			# print(corner)
# 			# print(initialDataDict[sample][corner])
# 			# print(initialDataDict[sample][corner+1])
# 			# print('--------')

# 			x1 = initialDataDict[sample][corner][0]
# 			y1 = initialDataDict[sample][corner][1]

# 			x2 = initialDataDict[sample][corner+1][0]
# 			y2 = initialDataDict[sample][corner+1][1]

# 			vect = [(x2 - x1), (y2 - y1)]
# 			# print("Vector %i: %f, %f" % (corner, vect[0], vect[1]))

# 			sideVectors[corner] = vect
			
			
			

# 		else: 
# 			# print(corner)
# 			# print(initialDataDict[sample][corner])
# 			# print(initialDataDict[sample][1])
# 			# print('--------')
# 			x1 = initialDataDict[sample][corner][0]
# 			y1 = initialDataDict[sample][corner][1]

# 			x2 = initialDataDict[sample][1][0]
# 			y2 = initialDataDict[sample][1][1]

# 			vect = [(x2 - x1), (y2 - y1)]

# 			sideVectors[corner] = vect
# 	print('------')
# 	initialVectorDict[sample] = sideVectors


# print(initialVectorDict)

