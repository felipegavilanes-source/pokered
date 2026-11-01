"""Original hand-pixeled Messi battle artwork (56x56 Game Boy palette).

Style: dynamic Pokémon-era trainer pose, Argentina striped #10 shirt,
short dark hair, distinctive thick beard and an upraised celebration hand.
This is a four-shade Gen 1-compatible approximation of the GBA look.
"""

import math


def messi_portrait():
    p = [[0 for _ in range(56)] for _ in range(56)]

    def pixel(x, y, c):
        if 0 <= x < 56 and 0 <= y < 56:
            p[y][x] = c

    def rect(x1, y1, x2, y2, c):
        for y in range(max(0, y1), min(55, y2) + 1):
            for x in range(max(0, x1), min(55, x2) + 1):
                pixel(x, y, c)

    def polygon(points, c):
        low = max(0, min(y for _, y in points))
        high = min(55, max(y for _, y in points))
        for y in range(low, high + 1):
            intersections = []
            for (xa, ya), (xb, yb) in zip(points, points[1:] + points[:1]):
                if (ya <= y + .5 < yb) or (yb <= y + .5 < ya):
                    intersections.append(xa + (y + .5 - ya) * (xb - xa) / (yb - ya))
            intersections.sort()
            for x1, x2 in zip(intersections[::2], intersections[1::2]):
                for x in range(math.ceil(x1), math.floor(x2) + 1):
                    pixel(x, y, c)

    def ellipse(cx, cy, rx, ry, c):
        for y in range(cy - ry, cy + ry + 1):
            for x in range(cx - rx, cx + rx + 1):
                if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1:
                    pixel(x, y, c)

    def line(x1, y1, x2, y2, c, thickness=1):
        n = max(abs(x2 - x1), abs(y2 - y1), 1)
        for i in range(n + 1):
            x = round(x1 + (x2 - x1) * i / n)
            y = round(y1 + (y2 - y1) * i / n)
            rect(x - thickness // 2, y - thickness // 2,
                 x + thickness // 2, y + thickness // 2, c)

    # One arm lifted in celebration: strong, legible outline.
    polygon([(16,36),(10,30),(7,23),(4,19),(2,20),(3,27),
             (7,35),(11,42),(17,44)], 3)
    polygon([(15,37),(10,33),(7,26),(5,23),(6,29),
             (10,37),(14,42),(17,41)], 1)
    # Raised hand and fingers.
    polygon([(2,20),(1,15),(2,12),(3,13),(4,17),
             (4,11),(6,10),(7,12),(7,18),(9,16),
             (11,17),(9,22),(6,25),(3,23)], 3)
    polygon([(3,19),(3,15),(4,20),(5,13),(6,14),
             (6,21),(8,19),(9,19),(7,23),(5,23)], 1)
    # Right bent arm, clenched hand near shoulder.
    polygon([(39,35),(46,38),(52,45),(55,49),(53,53),
             (48,53),(43,47),(39,45)], 3)
    polygon([(41,37),(46,40),(51,46),(52,50),
             (49,51),(44,44),(40,43)], 1)
    ellipse(49,49,4,4,3)
    ellipse(49,49,2,2,1)

    # Main shirt, outlined shoulder silhouette.
    polygon([(15,37),(21,34),(25,32),(35,32),(39,35),
             (45,39),(44,55),(12,55),(12,43)], 3)
    polygon([(17,39),(24,35),(35,35),(40,38),
             (42,42),(42,55),(15,55),(15,43)], 1)
    # Argentina national-team style vertical bands.
    polygon([(17,40),(21,37),(23,37),(22,55),(17,55)], 0)
    polygon([(27,37),(32,37),(33,55),(27,55)], 0)
    polygon([(37,38),(40,40),(40,55),(36,55)], 0)
    # Stripes and sleeves retain a dark border so GBC palette can separate them.
    line(22,38,23,55,2)
    line(34,37,35,55,2)
    rect(13,44,17,46,2)
    rect(41,44,44,46,2)
    # Shirt neckline/collar.
    polygon([(23,34),(25,31),(34,31),(36,34),(31,41),(27,41)],3)
    polygon([(25,35),(28,37),(31,37),(34,35),(31,39),(28,39)],0)
    line(20,36,26,40,2)
    line(38,36,32,40,2)

    # Neck shadow; then hair, ears, beard, face.
    polygon([(25,26),(35,26),(35,35),(32,38),(27,37),(24,33)],3)
    polygon([(26,26),(34,26),(33,33),(30,36),(27,33)],1)

    ellipse(18,20,3,5,3)
    ellipse(18,20,1,3,1)
    ellipse(41,20,3,5,3)
    ellipse(41,20,1,3,1)
    # Hair silhouette uneven at temple, cropped closely at sides.
    polygon([(18,11),(20,6),(24,4),(27,5),(31,3),(36,5),
             (40,7),(42,12),(42,19),(39,26),(38,30),
             (34,35),(28,36),(23,33),(20,29),(18,23)],3)
    # Skin and asymmetric face highlights.
    polygon([(21,13),(24,10),(29,11),(34,9),(38,12),
             (39,19),(38,25),(35,30),(31,32),
             (27,32),(24,29),(21,24),(20,17)],1)
    polygon([(22,15),(24,13),(27,14),(29,12),(31,13),
             (33,11),(37,14),(35,15),(30,15),(27,17)],2)
    # Forehead hair jagged front fringe.
    polygon([(19,14),(20,9),(24,6),(27,7),(30,5),
             (36,7),(39,10),(37,13),(34,10),
             (32,12),(29,10),(26,13),(22,12)],3)
    polygon([(21,10),(25,7),(28,9),(31,7),
             (35,9),(32,10),(29,8),(25,11)],2)
    rect(18,17,20,22,2)
    rect(39,17,41,23,2)
    # Face outline/hair merge into beard, not an oval stock character.
    polygon([(20,23),(23,26),(25,28),(28,29),(32,29),
             (36,27),(39,23),(39,30),(36,34),
             (33,36),(28,37),(24,35),(20,30)],3)
    polygon([(23,27),(25,29),(28,30),(32,30),
             (35,28),(35,32),(32,34),(28,34),(24,32)],2)
    # Moustache.
    polygon([(24,26),(27,25),(30,26),(33,25),(36,27),
             (33,29),(30,28),(27,29),(24,28)],3)
    rect(27,30,33,30,1)
    # Eyebrows & eye line; sharp focus.
    line(23,17,27,16,3,2)
    line(32,16,37,17,3,2)
    rect(24,20,26,21,3)
    rect(33,20,35,21,3)
    pixel(24,20,0)
    pixel(33,20,0)
    # Nose, highlight, mouth.
    line(29,20,28,24,2)
    line(28,24,31,25,3)
    line(28,30,32,30,3)
    pixel(21,25,2)
    pixel(37,24,2)
    # Beard stipple adds texture without ruining silhouette.
    for x,y in [(23,31),(26,32),(34,31),(31,34),(24,33),(35,30)]:
        pixel(x,y,3)

    # Shirt #10 in dark contrasting pixels on a light central badge.
    rect(26,45,34,53,0)
    glyph = {
        "1": ["010","110","010","010","111"],
        "0": ["111","101","101","101","111"],
    }
    for n, digit in enumerate("10"):
        for y, row in enumerate(glyph[digit]):
            for x, bit in enumerate(row):
                if bit == "1":
                    pixel(27 + n * 4 + x, 47 + y, 3)
    # Tiny captain band on raised sleeve.
    rect(11,39,14,41,2)
    line(11,39,14,39,0)
    return p
