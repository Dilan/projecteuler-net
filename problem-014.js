/*
 The following iterative sequence is defined for the set of positive integers:

 n → n/2 (n is even)
 n → 3n + 1 (n is odd)

 Using the rule above and starting with 13, we generate the following sequence:
 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

 It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
 Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

 Which starting number, under one million, produces the longest chain?

 NOTE: Once the chain starts the terms are allowed to go above one million.
*/
(function(limit) {
    var chainLength = function(number, cache) {
        if(number == 1) { return 1; }
        if(cache[number] != undefined) {
            return cache[number];
        } else {
            var next = (number % 2) ? (3 * number + 1) : number / 2;
            cache[next] = chainLength(next, cache);
            return 1 + cache[next];
        }
    };

    var find = function(limit, cache) {
        var number = 0; cache[0] = 0;
        for(var i=limit; i>0; i--) {
            if(cache[i] == undefined) {
                cache[i] = chainLength(i, cache);
            }
            if(cache[i] > cache[number]) {
                number = i;
            }
        }
        return number;
    };

    var _initial = new Date();
    console.log("Answer: " + find(limit, {}));
    console.log(((new Date()).getTime() - _initial.getTime())/1000 + " seconds left.");

})(1000000-1); // 837799