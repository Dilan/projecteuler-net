// A palindromic number reads the same both ways.
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
// Find the largest palindrome made from the product of two 3-digit numbers.
(function() {
    var isPalindromeNumber = function(n) {
        var n = '' + n; // to string
        for(var i=0; i<Math.floor(n.length/2); i++) {
            if(n[i] != n[n.length-(i+1)]) {
                return false;
            }
        }
        return true;
    };


    var find = function() {
        for(var i=999; i>900; i--) {
            for(var j=999; j>900; j--) {
                if(isPalindromeNumber(i * j)) {
                    return {x:i, y:j, result:(i*j)};
                }
            }
        }
    };
    console.log(find());

})(); // 993 x 913 = 906609