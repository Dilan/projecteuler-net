/*
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
*/
(function(limit) {
    var findDivisors = function(number) {
        var i = 1, limit = number, result = [];
        while(i<limit) {
            if(0 == (number % i)) {
                result.push(i);
                result.push(number / i);
                limit = number / i;
            }
            i++;
        }
        result.sort(function(x,y) { return x - y; }); // sort as a numbers
        return result;
    };

    var find = function(limit) {
        var triangleNumber = 1;
        for(var i=2; ; i++) {
            triangleNumber += i;
            if(triangleNumber < limit) continue;

            if(findDivisors(triangleNumber).length > limit) {
                return triangleNumber;
            }
        }
    };

    console.log(find(limit));

})(500); // 76576500