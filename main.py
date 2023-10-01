import csv,string, requests, time
from bs4 import BeautifulSoup as bs

BASE_URL = 'https://www.itb.ac.id/staff/listby/'
TIMEOUT = 30

s = requests.Session()
s.get(BASE_URL)
html = s.get(BASE_URL, timeout=TIMEOUT).content
soup = bs(html,'html.parser')
with open('data_dosen.csv','w',newline='') as f:
    writer = csv.writer(f)
    header = 'Name', 'Expertise', 'School/Faculty', 'Title', 'S1', 'S2', 'S3', 'Email'
    writer.writerow(header)

    for _ in list(string.ascii_uppercase):
        try:
            url = BASE_URL+_
            html = s.get(url, timeout=TIMEOUT).content
            time.sleep(5)
            soup = bs(html,'html.parser')
            tbody = soup.find('tbody')
            rows = tbody.find_all('tr')
            for i,row in enumerate(rows):
                try:
                    tr = row.find('td').find('a',href=True)
                    docent_url = tr['href']
                    docent_name = tr.text
                    html = s.get(docent_url, timeout=TIMEOUT).content
                    soup = bs(html,'html.parser')
                    full_name = soup.find('span', class_='font-size-06 font-weight-bold mb-5')
                    keahlian, sekolah, jabatan = soup.find_all('div', class_='col-8 font-weight-bold')
                    #print(full_name.text, keahlian.text, jabatan.text)
                    education = soup.find('ul', class_='list-unstyled')
                    education_dict = {}
                    for e in education.find_all('p'):
                        try:
                            level = e.find('span').text
                            education_dict[level] = e.text.split(level)[1].strip()
                            #print(education_dict[level])
                            institution, year = education_dict[level].split('\n')
                            institution = institution.strip()
                            year = year.strip()
                            if level == 'S1':
                                s1 = f'{institution} {year}'
                            elif level == 'S2':
                                s2 = f'{institution} {year}' 
                            elif level == 'S3':
                                s3 = f'{institution} {year}' 
                            #print(level,institution,year)
                        except:pass
                    email = soup.find('a', class_='btn btn-light btn-sm', href=True)['href'].replace('mailto:','')
                    #print(email)
                    row = full_name.text, keahlian.text, sekolah.text, jabatan.text, s1, s2, s3, email
                    if row:
                        writer.writerow(row)
                        print(row)
                    f.flush()
                except:pass
        except:pass