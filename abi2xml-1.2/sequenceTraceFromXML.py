from xml.dom import minidom
import csv


def getXMLFile(filename):
    
##import the xml file into python using the xmldoc module
    xmldoc = minidom.parse(filename)
##read each data tag of interest into the buffer. We only care about the data found in tags 9-12, which correpond to indices 8-11
    datatag9  = xmldoc.getElementsByTagName('DATA')[8]
    datatag10 = xmldoc.getElementsByTagName('DATA')[9]
    datatag11 = xmldoc.getElementsByTagName('DATA')[10]
    datatag12 = xmldoc.getElementsByTagName('DATA')[11]

##take the first sample_size items (not including 'common_data_struct') in the respective data tags and stick them in lists.
    sample_size = 1000
    tag9values  = datatag9.getElementsByTagName('int16') [:sample_size]
    tag10values = datatag10.getElementsByTagName('int16')[:sample_size]
    tag11values = datatag11.getElementsByTagName('int16')[:sample_size]
    tag12values = datatag12.getElementsByTagName('int16')[:sample_size]

##place the actual data points (Y values) into lists for each data tag

    data9  = []
    data10 = []
    data11 = []
    data12 = []

    for item in tag9values:
        data9.append(item.attributes['value'].value)
    for item in tag10values:
        data10.append(item.attributes['value'].value)
    for item in tag11values:
        data11.append(item.attributes['value'].value)
    for item in tag12values:
        data12.append(item.attributes['value'].value)

#as a checkpoint, these should all return 1000

    print('data9 has '  + str(len(data9))  +' elments.')
    print('data10 has ' + str(len(data10)) +' elments.')
    print('data11 has ' + str(len(data11)) +' elments.')
    print('data12 has ' + str(len(data12)) +' elments.')

##this creates a CSV file based on the name of the input xml file in teh same directory as this program (sequenceTraceFromXML.py) was called
    output_file = filename[:-4] + '_export_from_XML.csv'

    with open(output_file, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        #csvwriter.writerow('DATA_Tag 9','DATA_Tag 10','DATA_Tag 11','DATA_Tag 12')
        csvwriter.writerows(zip(range(1,sample_size+1),data9,data10,data11,data12))




