disp('Adrian Martinez Gomez');
disp('Problem 6 Project Euler');

vNumbers = [1:2000000];
Idx = isprime(vNumbers);
sResult = sum(vNumbers(Idx));

fprintf('The result is %d\n',sResult);