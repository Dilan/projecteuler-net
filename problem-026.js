/*
 A unit fraction contains 1 in the numerator.
 The decimal representation of the unit fractions with denominators 2 to 10 are given:

 1/2	= 	0.5
 1/3	= 	0.(3)
 1/4	= 	0.25
 1/5	= 	0.2
 1/6	= 	0.1(6)
 1/7	= 	0.(142857)
 1/8	= 	0.125
 1/9	= 	0.(1)
 1/10	= 	0.1

 Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
 It can be seen that 1/7 has a 6-digit recurring cycle.

 Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
*/
(function(limit) {
    var addZeroWhenDividendLessDivider = function(a, b) {
        if(Number(a) >= Number(b) ) {
            return a;
        } else {
            return addZeroWhenDividendLessDivider(Number(a) * 10, Number(b));
        }
    };

    var recurringCycle = function(a, b, tail) {
        var index,
            y = addZeroWhenDividendLessDivider(a, b) % b;

        if(!y) {
            return [];
        } else if((index = tail.indexOf(y)) == -1) {
            tail.push(y);
            return recurringCycle(y, b, tail);
        }
        return tail.slice(index);
    }

    var find = function(limit) {
        var max = 0, number, currentCycleLength = 0;
        for(var i=2; i<limit; i++) {
            currentCycleLength = recurringCycle(1,i,[]).length;
            if(currentCycleLength > max) {
                max = currentCycleLength;
                number = i;
            }
        }
        return number;
    };

    console.log(find(limit));

})(1000); // 983
