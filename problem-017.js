/*
 If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

 If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

 NOTE: Do not count spaces or hyphens.
 For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
 The use of "and" when writing out numbers is in compliance with British usage.
*/
(function(limit) {

    var numbers = {
        '1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5':'five',
        '6':'six',
        '7':'seven',
        '8':'eight',
        '9':'nine',
        '10':'ten',
        '11':'eleven',
        '12':'twelve',
        '13':'thirteen',
        '14':'fourteen',
        '15':'fifteen',
        '16':'sixteen',
        '17':'seventeen',
        '18':'eighteen',
        '19':'nineteen',
        '20':'twenty',
        '30':'thirty',
        '40':'forty',
        '50':'fifty',
        '60':'sixty',
        '70':'seventy',
        '80':'eighty',
        '90':'ninety'
    };

    var writtenOutInWords = function(number, specialNumbers) {
        if (number > 0 && number < 20) {
            return specialNumbers[number];
        }
        else if (number >= 20 && number < 100) {
            return (specialNumbers[(number - number % 10)]).toString() +
                ((number % 10) ? '-' + writtenOutInWords(number % 10, specialNumbers) : '');
        }
        else if (number >= 100 && number < 1000) {
            return writtenOutInWords((number - number % 100)/100, specialNumbers) + ' hundred' +
                ((number % 100) ? ' and ' + writtenOutInWords(number % 100, specialNumbers) : '');
        }
        else if (number >= 1000) {
            return writtenOutInWords((number - number % 1000)/1000, specialNumbers) + ' thousand' +
                ((number % 1000) ? ' ' + writtenOutInWords(number % 1000, specialNumbers) : '');
        }
    };

    var countLetters = function(number) {
        return number.toString().replace(/[-\s]/g,'').length;
    };

    var find = function(limit, specialNumbers) {
        var sum = 0;
        for (var i=1; i<=limit; i++) {
            sum += countLetters(writtenOutInWords(i,numbers));
        }
        return sum;
    };

    console.log(find(limit, numbers));

})(1000); // 21124