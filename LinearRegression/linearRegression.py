import matplotlib.pyplot as plt

sampleX = [1 ,2, 3, 4, 5, 6, 7, 8, 9]
sampleY = [1, 4, 5, 4, 6, 10, 15, 14, 16]
hypoOutput = []
theta0 = 1
theta1 = 1
learningRate = 0.02
sampleSize = 9

#adjust by the partial derivative of the cost function J(t_0, t_1) with respect to theta 0
def adjustmentTheta0():
	totalSum = 0
	for i in range(sampleSize):
		totalSum += hypothesisFun(sampleX[i]) - sampleY[i]
	return learningRate * totalSum / sampleSize 
	
def adjustmentTheta1():
	totalSum = 0
	for i in range(sampleSize):
		totalSum += (hypothesisFun(sampleX[i]) - sampleY[i])*sampleX[i]
	return learningRate * totalSum / sampleSize
	
def updateParams():
	global theta0
	global theta1
	theta0 = theta0 - adjustmentTheta0()
	theta1 = theta1 - adjustmentTheta1()

#one half of the mean of the squared differences, H(X) = T_0 + T_1*x
def linearRegressionGradientDiscent():
	for i in range(10):
		drawPlot()
		updateParams()
		
	
def hypothesisFun(x):
	return theta0 + theta1*x
	
	
def drawPlot():
	global hypoOutput
	plt.scatter(sampleX, sampleY)
	plt.ylabel('y')
	plt.xlabel('x')
	for i in range(sampleSize):
		hypoOutput.append(hypothesisFun(i))
	plt.plot(sampleX, hypoOutput)
	plt.show()
	print(hypoOutput)
	hypoOutput = []

linearRegressionGradientDiscent()