/*
 In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

 It is possible to make £2 in the following way:
 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

 How many different ways can £2 be made using any number of coins?
*/
(function(coins, total) {

    var coins = [1,2,5,10,20,50,100,200];

    var find = function(coins, total) {
        var res = [1];
        for(var i = 0; i<coins.length; i++) {
            for(var j = coins[i]; j<=(total); j++) {
                res[j] = (res[j] || 0) + (res[j - coins[i]] || 0);
            }
        }
        return res[total];
    };
    console.log(find(coins, total));

})([1,2,5,10,20,50,100,200], 200);