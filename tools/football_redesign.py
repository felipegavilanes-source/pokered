"""Hand-drawn 56x56 Game Boy trainer portraits: Neymar, Messi and CR7.

No runtime dependencies; pixel values are indices into the four Game Boy shades.
These are stylized portraits for an unofficial Challenge Edition game modification.
"""
import math

def football_portrait(name):
    if name not in ("neymar", "messi", "cr7"):
        raise ValueError("Unsupported special portrait: " + name)
    pixels = [[0] * 56 for _ in range(56)]

    def dot(x, y, value):
        if 0 <= x < 56 and 0 <= y < 56:
            pixels[y][x] = value

    def rect(x1, y1, x2, y2, color):
        for y in range(max(0, y1), min(56, y2 + 1)):
            for x in range(max(0, x1), min(56, x2 + 1)):
                pixels[y][x] = color

    def ellipse(cx, cy, rx, ry, color):
        for y in range(max(0, cy - ry), min(56, cy + ry + 1)):
            for x in range(max(0, cx - rx), min(56, cx + rx + 1)):
                if ((x-cx) / max(1, rx)) ** 2 + ((y-cy) / max(1, ry)) ** 2 <= 1:
                    pixels[y][x] = color

    def polygon(points, color):
        for y in range(max(0, min(p[1] for p in points)),
                       min(56, max(p[1] for p in points) + 1)):
            crosses = []
            for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
                if (y1 <= y < y2) or (y2 <= y < y1):
                    crosses.append(x1 + (y + .5 - y1) * (x2 - x1) / (y2 - y1))
            crosses.sort()
            for a, b in zip(crosses[::2], crosses[1::2]):
                for x in range(max(0, math.ceil(a)), min(56, math.floor(b) + 1)):
                    dot(x, y, color)

    def line(x1, y1, x2, y2, color, width=1):
        steps = max(abs(x2-x1), abs(y2-y1), 1)
        for i in range(steps + 1):
            x = round(x1 + (x2 - x1) * i / steps)
            y = round(y1 + (y2 - y1) * i / steps)
            rect(x - width // 2, y - width // 2,
                 x + width // 2, y + width // 2, color)

    def number(value, x, y, color):
        glyphs = {
            "1": ["010", "110", "010", "010", "111"],
            "0": ["111", "101", "101", "101", "111"],
            "7": ["111", "001", "010", "010", "010"],
        }
        for n, digit in enumerate(value):
            for dy, row in enumerate(glyphs[digit]):
                for dx, pixel in enumerate(row):
                    if pixel == "1":
                        dot(x + n * 5 + dx, y + dy, color)

    # Chest and neckline are shared; identity comes from hair, face and shirt.
    polygon([(0,55),(2,46),(10,40),(19,37),(24,35),(32,35),
             (37,37),(47,40),(54,46),(55,55)], 3)
    polygon([(2,55),(5,47),(12,42),(20,39),(25,38),(31,38),
             (37,39),(45,42),(51,47),(54,55)], 2)
    polygon([(20,35),(22,30),(34,30),(36,35),(33,41),(28,44),(23,41)], 3)
    polygon([(23,34),(23,29),(33,29),(33,34),(28,40)], 1)

    if name == "neymar":
        # Fade haircut, playful brow, lighter beard/goatee, earring, jersey 10.
        ellipse(15,23,3,5,3);ellipse(41,23,3,5,3)
        ellipse(28,20,14,18,3);ellipse(28,20,12,16,1)
        polygon([(15,18),(14,12),(17,8),(16,6),(22,5),(25,2),
                 (33,3),(38,5),(41,10),(40,16),(37,12),(32,10),
                 (27,11),(22,10),(18,15)],3)
        rect(15,12,18,17,2);rect(38,12,40,17,2)
        polygon([(21,6),(25,4),(29,5),(33,4),(37,8),
                 (33,7),(28,8),(24,7),(20,10)],2)
        line(20,18,25,17,3,2);line(31,17,36,18,3,2)
        rect(22,20,24,22,3);rect(32,20,34,22,3)
        dot(22,20,0);dot(32,20,0)
        rect(27,23,28,26,2);rect(27,27,30,27,3)
        rect(23,29,26,29,3);rect(30,29,33,29,3)
        line(25,32,31,32,3);rect(27,34,29,35,3)
        rect(42,25,43,26,3);dot(43,27,0)
        line(5,44,17,43,1,2);line(39,43,50,45,1,2)
        line(20,42,28,46,3,2);line(36,42,28,46,3,2)
        number("10",26,49,0)
    elif name == "messi":
        # Short hair, full beard, stripes, captain's band and jersey 10.
        ellipse(15,23,3,5,3);ellipse(41,23,3,5,3)
        ellipse(28,20,14,18,3);ellipse(28,20,12,16,1)
        polygon([(15,16),(15,9),(20,5),(25,5),(29,4),(34,5),
                 (40,9),(41,16),(38,16),(37,12),(34,11),
                 (29,12),(24,11),(18,13)],3)
        polygon([(20,8),(25,6),(30,7),(33,6),
                 (38,9),(35,11),(29,10),(24,10)],2)
        rect(17,15,18,18,2)
        polygon([(16,25),(20,28),(22,31),(26,32),(30,32),
                 (34,30),(38,26),(40,25),(39,33),(35,37),
                 (29,40),(25,39),(20,36),(17,31)],3)
        polygon([(22,28),(25,30),(31,30),(34,28),
                 (33,33),(29,35),(25,34)],2)
        rect(27,33,30,34,3)
        line(20,18,25,18,3,2);line(31,18,36,18,3,2)
        rect(22,21,24,22,3);rect(32,21,34,22,3)
        rect(27,24,28,27,2);rect(28,28,30,28,3)
        line(25,31,31,31,3)
        rect(10,43,13,55,0);rect(19,43,22,55,0)
        rect(34,43,37,55,0);rect(43,43,46,55,0)
        line(21,42,28,47,1,2);line(35,42,28,47,1,2)
        rect(5,48,11,49,1)
        number("10",26,50,3)
    else:
        # Ronaldo: swept hairstyle, angular jaw, sharp brows and jersey 7.
        ellipse(16,24,2,4,3);ellipse(40,24,2,4,3)
        polygon([(18,8),(25,4),(34,5),(39,9),(41,15),
                 (40,28),(36,35),(28,39),(20,35),(16,28),(15,15)],3)
        polygon([(19,10),(25,7),(34,8),(37,11),(39,16),
                 (38,28),(34,33),(28,36),(22,33),(18,28),(17,16)],1)
        polygon([(15,16),(15,11),(18,8),(19,5),(26,4),
                 (31,2),(37,4),(41,8),(40,14),
                 (36,11),(30,10),(24,12),(18,14)],3)
        polygon([(20,8),(27,5),(34,5),(38,7),
                 (31,8),(26,10),(19,11)],2)
        line(19,17,25,17,3,2);line(31,17,37,16,3,2)
        rect(22,20,24,22,3);rect(32,20,34,22,3)
        line(21,24,24,25,2);line(32,25,35,24,2)
        line(28,23,27,27,2);line(27,28,30,28,3)
        line(25,31,31,31,3)
        line(22,34,27,36,2);line(29,36,34,34,2)
        rect(22,38,34,40,1)
        line(6,46,19,42,0,2);line(38,42,50,46,0,2)
        line(20,41,28,45,3,2);line(36,41,28,45,3,2)
        rect(25,47,32,54,1)
        number("7",27,49,3)
    return pixels
