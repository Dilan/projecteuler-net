function Ellipse(a, b, r) {
    this.a = a;
    this.b = b;
    this.r = r;
    this.slopeOfTangentLine = function(x, y) {
        return this.a * x / (this.b * y) * (-1);
    }
};

function Point(x, y) {
    this.x = x;
    this.y = y;
}

function Line(m, b) {
    this.m = m;
    this.b = b;
}

const deg2rad = Math.PI/180;
const rad2deg = 180/Math.PI;

const reflection = function(point, line, ellipse) {
    var tangent = lineFunc(
        point,
        ellipse.slopeOfTangentLine(point.x, point.y)
    );
    var perpendicular = perpendicularLine(point, tangent);

    var theAngle = Math.atan(perpendicular.m) * rad2deg;
    if (theAngle < 0) { theAngle = 180 + theAngle; }

    var t = angle(perpendicular, line);
    var newAngle = theAngle + Math.atan(t) * rad2deg;
    var m = Math.tan(newAngle * deg2rad);
    var reflected = lineFunc(point, m);

    var intersectionPoint = secondIntersection(reflected, ellipse, point);

    return [intersectionPoint, reflected];
};

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
};

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

var next = function(nextPoint, line, ellipse, counter) {
    counter++;
    var result = reflection(nextPoint, line, ellipse);

    nextPoint = result[0];
    line = result[1];

    if (nextPoint.x <= 0.01 && nextPoint.x >= -0.01 &&
        nextPoint.y <= 10.01 && nextPoint.y >= 9.99)
    {
        return counter;
    }
    return next(nextPoint, line, ellipse, counter);
}

var startPoint = new Point(0.0, 10.1);
var nextPoint = new Point(1.4, -9.6);
var ellipse = new Ellipse(4, 1, 100);
var line = lineByPoints(startPoint, nextPoint);

console.log('Anser is:', next(nextPoint, line, ellipse, 0));
