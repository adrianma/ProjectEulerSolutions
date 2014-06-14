disp('Adrian Martinez Gomez');
disp('Problem 6 Project Euler');

nPowers = 100;

nSum_of_powers = sum((1:100).^2);
nPower_of_sum = sum(1:100)^2;
nResult = nPower_of_sum - nSum_of_powers;
fprintf('The result is: %d \n',nResult);