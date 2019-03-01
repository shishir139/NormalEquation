data = csvread('AirQualityUCI.csv');
X = data(:, 2);
y = data(:, 3);
m = length(y);
X = [ones(m, 1) X];
transposeX = X'
tempProductOfXtX = transposeX*X
#print(tempProductOfXtX)
inverse = inv(tempProductOfXtX)
tempProductInv = inverse*transposeX
theta = tempProductInv*y
disp("Value of theta is")
disp(theta)
