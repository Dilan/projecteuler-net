/*
 Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
 If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

 For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
 The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

 Evaluate the sum of all the amicable numbers under 10000.
*/
(function(limit) {
    // Решето Эратосфена
    var sieveOfEratosthenes = function (limit) {
        var s = [undefined, undefined];
        for (var k = 2; k <= limit; k++) {
            s[k] = 1;
        }
        for (k = 2; k * k <= limit; k++) {
            if (s[k] == 1) {
                for (var l = k * k; l <= limit; l += k) {
                    s[l] = 0;
                }
            }
        }
        return s;
    };

    var nonPrimeNumbers = function (limit) {
        return sieveOfEratosthenes(limit).reduce(function (result, value, index) {
            if (value == 0) {
                result.push(index);
            }
            return result;
        }, []);
    };

    var findDivisors = function(number) {
        var i = 1, limit = number, result = [];
        while(i<limit) {
            if(0 == (number % i)) {
                result.push(i);
                if(i > 1) {
                    result.push(number / i);
                }
                limit = number / i;
            }
            i++;
        }
        result.sort(function(x,y) { return x - y; }); // sort as a numbers
        return result;
    };

    var numberToDivisorsSumMap = function(numbers) {
        var res = [];
        for(var i = 0; i<numbers.length; i++) {
            res[numbers[i]] = findDivisors(numbers[i]).reduce(function(x,y) { return x+y; })
        }
        return res;
    };

    var sumAmicableNumbers = function(list) {
        var res = 0;
        for(var number=0; number<list.length; number++) {
            var sum = list[number];
            if(typeof sum != 'undefined') {
                if(number!=sum && list[sum] == number) {
                    res += number;
                }
            }
        }
        return res;
    };

     console.log(sumAmicableNumbers(
         numberToDivisorsSumMap(
             nonPrimeNumbers(limit)
         )
     ));


})(10000);