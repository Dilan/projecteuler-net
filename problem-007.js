// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
// What is the 10 001st prime number?
(function(serialNumber) {
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

    console.log(primeNumbers(150000)[serialNumber-1]);

})(10001); // 104743