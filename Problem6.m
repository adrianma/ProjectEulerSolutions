disp('Adrian Martinez Gomez');
disp('Problem 6 Project Euler');

sNPowers = 100;

sSumOfPowers = sum((1:sNPowers).^2);
sPowerOfSums = sum(1:sNPowers)^2;
sResult = sPowerOfSums - sSumOfPowers;
fprintf('The result is: %d \n',sResult);