

def point(x, y, z):
    print 'Point ({x}, {y}, {z})'.format(x=x, y=y, z=z)
    
    
def write_point(*args):
    point(*args)
    
    
write_point(1, 2, 3)