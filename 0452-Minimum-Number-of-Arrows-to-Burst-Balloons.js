var findMinArrowShots = function(points) {
    points.sort((p1, p2) => p1[1] - p2[1]);

    let numArrows = 1;
    let currentEnd = points[0][1];

    for (let i = 1; i < points.length; i++) {
        if (points[i][0] > currentEnd) {
            numArrows ++;
            currentEnd = points[i][1];
        }
    }

    return numArrows;
};
