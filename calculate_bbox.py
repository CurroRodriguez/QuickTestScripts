import sys

def calculate_bbox(coords):
    x1, y1, x2, y2 = order_coords(coords)
    dx = x2 - x1
    dy = y2 - y1
    ratio = 0.05
    ix = dx * ratio
    iy = dy * ratio
    return (x1 + ix, y1 + iy, x2 - ix, y2 - iy)
    
    
def order_coords(coords):    
    x1, y1, x2, y2 = [float(coord) for coord in coords]
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)
    return (x1, y1, x2, y2)


if __name__=='__main__':
    x1, y1, x2, y2 = calculate_bbox(sys.argv[1:])
    print x1, y1, x2, y2
    
    