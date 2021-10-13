def intersection(r1, r2):
    r1xmin, r1ymin,r1xmax, r1ymax = r1
    r2xmin, r2ymin,r2xmax, r2ymax = r2

    xdiff = min(r1xmax,r2xmax) - max(r1xmin, r2xmin)
    ydiff = min(r1ymax,r2ymax) - max(r1ymin, r2ymin)
    print('{} {}'.format(xdiff, ydiff))
    return xdiff * ydiff if xdiff > 0 else 0

print(intersection(r2=(1,1,4,4), r1=(2,2,8,8)))
