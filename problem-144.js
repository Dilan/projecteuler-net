function Ellipse(a, b, r) {
    this.a = a;
    this.b = b;
    this.r = r;
}
var ellipse = new Ellipse(4, 1, 100);

function Point(x, y) {
    this.x = x;
    this.y = y;
}

function Line(m, b) {
    this.m = m;
    this.b = b;
}

var perpendicularLine = function(point, line) {
    var m = -1 / line.m;
    return lineFunc(point, m);
};

var lineFunc = function(point, m) {
    var b = point.y - m * point.x; // y - y` = m (x - x`)
    return new Line(m, b);
}
var lineByPoints = function(point1, point2) {
    var m = (point2.y - point1.y) / (point2.x - point1.x);
    return lineFunc(point1, m);
}

var quadraticEquation = function(a, b, c) {
    var result = (-1 * b + Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
    var result2 = (-1 * b - Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
    return [result, result2];
};

var angle = function(line1, line2) {
    return (line1.m - line2.m) / (1 + line1.m * line2.m);
};

var secondIntersection = function(line, ellipse, point) {
    var a = line.m * line.m + ellipse.a;
    var b = 2 * line.m * line.b;
    var c = line.b * line.b - ellipse.r;

    var xx = quadraticEquation(a, b, c);

    var x = Math.abs(point.x - xx[0]) < Math.abs(point.x - xx[1]) ? xx[1] : xx[0];
    var y = x * line.m + line.b;
    return new Point(x, y);
};

var next = function(point, line) {
    var deg2rad = Math.PI/180;
    var rad2deg = 180/Math.PI;

    var m = point.x / point.y * -4;

    var tangent = lineFunc(point, m);
    var perpendicular = perpendicularLine(point, tangent);

    /*
    console.log('line =>', line);
    console.log('tangent =>', tangent);
    console.log('perpendicular =>',perpendicular);
    */

    var theAngle = Math.atan(perpendicular.m) * rad2deg;
    if (theAngle < 0) { theAngle = 180 + theAngle; }

    var t = angle(perpendicular, line);
    var newAngle = theAngle + Math.atan(t) * rad2deg;
    var mmm = Math.tan( newAngle * deg2rad);
    var reflected = lineFunc(point, mmm);

    return secondIntersection(reflected, ellipse, point);
};

var solution = function(point, sourcePoint) {
    var counter = 0;
    while (true) {
        counter++;
        // console.log('from ',sourcePoint, ' --> ', point)

        var line = lineByPoints(sourcePoint, point);
        var nextPoint = next(point, line);
        var npx = parseFloat(nextPoint.x.toFixed(2));
        var npy = parseFloat(nextPoint.y.toFixed(2));

        if (npx <= 0.01 && npx >= -0.01 &&
            npy <= 10.01 && npy >= 9.99 )
        {
            console.log('', counter, 'DONE ===>', nextPoint);
            break;
        }
        sourcePoint = point;
        point = nextPoint;
    }
    // 354
};

solution(new Point(1.4, -9.6), new Point(0.0, 10.1));
