// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// Find the sum of all the primes below two million.
(function(limit) {

    // Решето Эратосфена
    var sieveOfEratosthenes = function (limit) {
        var s = [undefined, 0];
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

    var primeNumbers = function (limit) {
        return sieveOfEratosthenes(limit).reduce(function (result, value, index) {
            if (value == 1) {
                result.push(index);
            }
            return result;
        }, []);
    };

    var res = primeNumbers(2000100).reduce(function(x, y) {
        return (y < limit) ? x + y : x;
    });

    console.log(res);

})(2000000); // 142913828922