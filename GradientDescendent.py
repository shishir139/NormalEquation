data = csvread('AirQualityUCI.csv');
X = data(:, 2);
y = data(:, 3);
m = length(y);
Z = X;
X = [ones(m, 1) X];
transposeX = X';
disp("Value of theta is")
numIterations= 100000
alpha = 0.0005
theta = [1;1]

function theta = calculateGradientDescent(X, y, theta, alpha, m, numIterations)
    transposeOfX = X'
    for i = 0:numIterations
        h = X*theta;
        l = h - y;
       
        #computeCost = np.sum(l ** 2) / (2 * m);
        
       
        gradient = (transposeOfX * l) / m;
   
        theta = theta - alpha * gradient;
    return
    end
end

theta = calculateGradientDescent(X, y, theta, alpha, m, numIterations)
disp("The values of theta are")
disp(theta);
xx = input("Enter the x coordinate corresponding to which you want to find the y value")
mm = theta(1,1);
b = theta(2,1);
yy = (mm*xx) + b

xline = 0:100;
plot(Z, y,'.', xline, ((mm*xline)) + b,'*',xx,yy) ;
#plot(X,y)