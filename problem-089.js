// Find the number of characters saved by writing each of these in their minimal form.
// Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

var getDigit = function(c) {
    var hm = { 'i':1, 'v':5, 'x':10, 'l':50, 'c':100, 'd':500, 'm':1000 };
	return hm[c.toLowerCase()];
};

var convertToInt = function(x) {
	var y = 0;
	var len = x.length;
    
    x.split('').forEach(function(c1, i) {
        d1 = getDigit(c1);
		op = 0;
		if (i < len-1) {
			c2 = x.charAt(i+1);
			d2 = getDigit(c2);
			if (d1 < d2)
                op = 1;
		}
		
        if (d1 == 0)
			throw new Error('Invalid: ' + x);

        y = y + (d1 * (op ? -1 : 1));
    });
    
    if (y < 1 || y > 4999)
        throw new Error('Invalid: ' + x);

	return y;
}
var convertToRoman = function(x) {
	var n = ['i', 'iv', 'v', 'ix', 'x', 'xl', 'l', 'xc', 'c', 'cd', 'd', 'cm', 'm'];
	var v = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000];
	
	if( x < 1 || x > 4999)
	   throw new Error('Invalid: ' + x);

	var y = '';
    var i = (v.length - 1)
    while (i >= 0) {
        if( v[i] <= x) {
			y += n[i];
			x -= v[i];
		} else {
			i--;
		}
    }
    return y.toUpperCase();
};      

(function(filePath) {
    require('fs').readFile(filePath, 'utf8', function (err, content) {
        var lines = content.split('\n');
        
        counter = 0
        lines.forEach(function(rNum) {
            var iNum = convertToInt(rNum);
            var rNumMin = convertToRoman(iNum);

            if (rNumMin.length !== rNum.length) {
                counter += (rNum.length - rNumMin.length);
            }
        });
        console.log('Answer is:', counter);
    });
})('./data/p089_roman.txt');
