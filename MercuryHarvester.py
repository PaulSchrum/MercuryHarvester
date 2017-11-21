
import urllib2
import BeautifulSoup

headURL = r'http://pds-geosciences.wustl.edu/messenger/mess-e_v_h-mla-3_4-cdr_rdr-data-v2/messmla_2101/rdr_radr/'

response = urllib2.urlopen(headURL)
contents = response.read()
response.close()
soup = BeautifulSoup.BeautifulSoup(contents)

for linkTag in soup.findAll('a'):
    if 'Parent' not in linkTag.contents[0]:
        print linkTag





