// By considering the terms in the Fibonacci sequence whose values do not exceed four million,
// find the sum of the even-valued terms.
(function (limit) {

    var fibonacciSum = function (first, second, limit) {
        var next = first + second;
        if (next > limit) {
            return 0;
        }
        return (!(next % 2) ? next : 0) + fibonacciSum(second, next, limit);
    }
    console.log(2 + fibonacciSum(1, 2, limit));

})(4000000); // 4613732