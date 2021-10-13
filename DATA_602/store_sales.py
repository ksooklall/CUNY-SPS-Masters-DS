sales = []

for i in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']:
    sales.append(int(input('{} sales'.format(i))))

print('Weekly sales: {}'.format(sum(sales)/len(sales)))
