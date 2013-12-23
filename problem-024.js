/*
 A permutation is an ordered arrangement of objects.
 For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
 If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.

 The lexicographic permutations of 0, 1 and 2 are:
 012   021   102   120   201   210

 What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
*/
(function(breakStep, numbers) {

    var separate = function(number) {
        for(var i=(number.length-1); i>0; i--) {
            if(parseInt(number[i]) > parseInt(number[i-1])) {
                return i-1;
            }
        }
        return -1;
    };

    var getNextNumberInNumericallyOrderedList = function(current, list) {
        for(var i = 0; i<=list.length; i++) {
            if(list[i]>current) {
                return i;
            }
        }
        return -1;
    };

    var replace = function(number, index, list) {
        list.splice(index, 1, number);
        return list;
    };

    var findTheSmallestNumberByReplacingTopRankNumberAndReshufflingTailNumbers = function(originalNumber) {
        var numbers = originalNumber.split(''); // to array
        var top = numbers[0];
        var tail = numbers.slice(1); tail.sort();
        var index = getNextNumberInNumericallyOrderedList(top, tail);

        return tail[index] + replace(top, index, tail).join('');
    };

    var next = function(originalNumber) {
        var separateIndex = separate(originalNumber);

        if(separateIndex != -1) {
            return originalNumber.slice(0,separateIndex) +
                   findTheSmallestNumberByReplacingTopRankNumberAndReshufflingTailNumbers(
                       originalNumber.slice(separateIndex)
                   );
        }
        return originalNumber;
    };

    var find = function(breakStep, initialNumber) {
        var currentNumber = initialNumber, nextNumber;
        while(true) {
            breakStep--;
            if(breakStep == 0) break;
            nextNumber = next(currentNumber);
            if(nextNumber == currentNumber) break;
            currentNumber = nextNumber;
        }
        return currentNumber;
    }

    console.log(find(breakStep, numbers.join('')));

})(1000000, [0,1,2,3,4,5,6,7,8,9]); // 2783915460

