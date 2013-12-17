/*
 A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
 For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
 which means that 28 is a perfect number.

 A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
 if this sum exceeds n.

 As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
 the smallest number that can be written as the sum of two abundant numbers is 24.
 By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two
 abundant numbers.
 However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest
 number that cannot be expressed as the sum of two abundant numbers is less than this limit.

 Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
*/
(function(limit) {
    var findDivisors = function(number) {
        var i = 2, limit = number, result = [1];
        while(i<limit) {
            if(0 == (number % i)) {
                result.push(i);
                if(i  != number / i) {
                    result.push(number / i);
                }
                limit = number / i;
            }
            i++;
        }
        result.sort(function(x,y) { return x - y; }); // sort as a numbers
        return result;
    };

    var divisorsSum = function(number) {
        return findDivisors(number).reduce(function(x,y) { return x+y; }, 0);
    }

    var isAbundantNumber = function(number) {
        return number < divisorsSum(number);
    };

    var abundantNumbers = function(limit) {
        var numbers = []
        for(var i=1; i<=limit; i++) {
            if(isAbundantNumber(i)) {
                numbers.push(i);
            }
        }
        return numbers;
    };

    var isNumberCanBeWrittenAsTheSumOfTwoAbundantNumbers = function(number, abundantNumbers) {
        for(var i=0; i<=abundantNumbers.length; i++) {
            if(abundantNumbers[i] > number) return false;

            if(abundantNumbers.indexOf(number - abundantNumbers[i]) != -1) {
                return true;
            }
        }
        return false;
    };

    var isNumberCanNotBeWrittenAsTheSumOfTwoAbundantNumbers = function(number, abundantNumbers) {
        return !isNumberCanBeWrittenAsTheSumOfTwoAbundantNumbers(number, abundantNumbers);
    }

    var find = function(limit, abundantNumbers) {
        var sum = 0;
        for(var i=limit; i>0; i--) {
            if(isNumberCanNotBeWrittenAsTheSumOfTwoAbundantNumbers(i, abundantNumbers)) {
                sum += i;
            }
        }
        return sum;
    };

    console.log(find(limit, abundantNumbers(limit)));

})(28123); // 4179871