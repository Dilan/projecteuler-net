/*
 Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

 2^2=4, 2^3=8, 2^4=16, 2^5=32
 ...

 If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

 How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
*/
(function(from, to) {

    var summarize = function (a, b) {
        a = a.split("").reverse();
        b = b.split("").reverse();
        for (var i = 0; i < b.length; i++) {
            a[i] = parseInt(a[i] || 0) + parseInt(b[i]);
            if (a[i] >= 10) {
                a[i] -= 10;
                a[i + 1] = parseInt(a[i + 1] || 0) + 1;
            }
        }
        return a.reverse().join("");
    };
    var multiply = function (a, b) {
        a = a.split("").reverse();
        b = b.split("").reverse();
        var r = '', c = [];
        for (var j = 0; j < b.length; j++) {
            c = [];
            for (var k = 0; k <= j; k++) {
                c[k] = 0;
            }
            for (var i = 0; i < a.length; i++) {
                c[i + j] = parseInt(a[i]) * parseInt(b[j]);
            }
            for (var k = 0; k < c.length; k++) {
                if (c[k] >= 10) {
                    c[k + 1] = parseInt(c[k + 1] || 0) + (c[k] - c[k] % 10) / 10;
                    c[k] = c[k] % 10;
                }
            }
            r = summarize(r, c.reverse().join(""));
        }
        return r;
    };

    var pow = function(a, b) {
        var r = '1';
        for (var i = 0; i < b; i++) {
            r = multiply(r, a);
        }
        return r;
    }

    var find = function(from, to) {
        var sequence = [], result;
        for(var a=from; a<=to; a++) {
            for(var b=from; b<=to; b++) {
                result = pow(a.toString(), b.toString());
                if(sequence.indexOf(result) == -1) {
                    sequence.push(result);
                }
            }
        }
        return sequence.length;
    };

    console.log(find(2,100));

})(); // 9183