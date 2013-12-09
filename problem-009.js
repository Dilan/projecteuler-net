// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
// a2 + b2 = c2
// For example, 3x3 + 4x4 = 9 + 16 = 25 = 5x5.
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.
(function() {

    var find_a_b = function() {
        for(var i=1; i<500; i++) {
            for(var j=1; j<500; j++) {
                if( ((i + j) - (i*j/1000)) == 500) {
                    return [i, j];
                }
            }
        }
    };

    var find = function(ab) {
        return (1000 - ab[0] - ab[1]) * ab[0] * ab[1];
    };

    console.log(find(find_a_b()));

})();
// we can remove "c" as a result expression be following:
// 500 = (a + b) - (a * b / 1000)