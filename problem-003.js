// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?
(function (number) {
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

    var findPrimeDivider = function (number, primeNumbers) {
        for (var i = 0; i < primeNumbers.length; i++) {
            if (0 == (number % primeNumbers[i])) {
                return primeNumbers[i];
            }
        }
        return null;
    }

    var findPrimeFactors = function (number, primeNumbers) {
        var primeDivider = findPrimeDivider(number, primeNumbers);

        return (primeDivider) ?
            [].concat(primeDivider, findPrimeFactors(number / primeDivider, primeNumbers)) :
            [];
    }

    console.log(
        Math.max.apply(
            Math,
            findPrimeFactors(number, primeNumbers(100000))
        )
    );

})(600851475143); // 6857
