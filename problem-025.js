/*
 What is the first term in the Fibonacci sequence to contain 1000 digits?
*/
(function(limit) {

    var summarize = function (x, y) {
        x = x.toString().split('').reverse();
        y = y.toString().split('').reverse();

        var sum = [], maxLength = Math.max(x.length, y.length);

        for (var i = 0; i < maxLength; i++) {
            var res = (parseInt(x[i] || 0) + parseInt(y[i] || 0)) + (parseInt(sum[i] || 0));
            sum[i]   = (res >=10) ? res%10 : res;
            sum[i+1] = (res >=10) ? 1 : '';
        }
        return sum.reverse().join("");
    };

    var fibonacciSum = function (first, second, nextIndex, limit) {
        var next = summarize(first,second);
        if (next.length >= limit) {
            return nextIndex;
        }
        return fibonacciSum(second, next, (++nextIndex), limit);
    }

    console.log(fibonacciSum(1,1,3,limit))

})(1000);