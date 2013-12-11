/*
 Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
 there are exactly 6 routes to the bottom right corner.

 How many such routes are there through a 20×20 grid?
*/
(function(amount) {
    var find = function (amount) {
        var n, m; n = m = amount; var grid = [];

        for (var i = 0; i <= m; i++) {
            grid[i] = [1];
        }
        for (var j = 1; j <= n; j++) {
            grid[0][j] = 1;
        }

        for (var i = 1; i <= m; i++) {
            for (var j = 1; j <= n; j++) {
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1];
            }
        }
        return grid[m][n];
    };

    console.log(find(amount));
    
})(20); // 137846528820