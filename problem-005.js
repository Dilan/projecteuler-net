// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
(function() {
    var find = function() {
        for(var i=2*3*5*7*11*13*17*19;;i+=2*3*5*7*11*13*17*19) {
            if(i%16==0&&i%9==0) {
                return i;
            }
        }
        return null;
    };
    console.log(find());

})(); // 232792560