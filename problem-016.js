/*
 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

 What is the sum of the digits of the number 2^1000?
 */
(function(pow) {
    var redouble = function (x) {
        x = x.toString();
        var increment= 0, res, total = '';
        for(var i=x.length-1; i>=0; i--) {
            res = 2 * parseInt(x[i]) + increment;
            increment = (res.toString().length>1) ? 1 : 0;
            total = res.toString().substr(-1) + total;
            if(i == 0 && increment) total = '1' + total;
        }
        return total;
    };

    var twoInPow = function(pow) {
        var result = '1';
        for(var i=0; i<pow; i++) {
            result = redouble(result);
        }
        return result;
    };

    var find = function(pow) {
        var s = 0; var result = twoInPow(pow);
        for(var i=0; i < result.length; i++) {
            s += parseInt(result[i]);
        }
        return s;
    }

    console.log(find(pow));

})(1000); // 1366