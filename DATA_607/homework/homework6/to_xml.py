import pandas as pd

df = pd.read_csv('books.df')

xml_data = ['<root>']
for column in df.columns:
    xml_data.append('<{}>'.format(column))  # Opening element tag
    for field in df.index:
        # writing sub-elements
        xml_data.append('<{0}>{1}</{0}>'.format(field, df[column][field]))
    xml_data.append('</{}>'.format(column))  # Closing element tag
xml_data.append('</root>')

with open('books.xml', 'w') as f:  # Writing in XML file
    for line in xml_data:
        f.write(line)
