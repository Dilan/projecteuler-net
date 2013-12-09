// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
(function(limit) {

    var squaresSum = 0, sum = 0;
    for(var i=1; i<=limit; i++) {
        squaresSum += (i * i);
        sum += i ;
    }
    console.log((sum * sum) - squaresSum);

})(100); // 25164150
