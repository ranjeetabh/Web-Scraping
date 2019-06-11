## json_parsing_selectscience.py
## Author: Ranjeeta Bhattacharya

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Importing libraries

import requests
import urllib.request
from bs4 import BeautifulSoup
import json
import csv


counter = 0

# Inserting header column names in the file

fileHeader = ["Product_Name","Product_Description","Product_URL","Product_Review","Product_Rating"]

# Opening outputfile file for writing data

oFile = open("rochePdtReviewsSelectScience.csv","w")

#oFile = open("abbottPdtReviewsSelectScience.csv","w")

#oFile = open("orthoPdtReviewsSelectScience.csv","w")

#oFile = open("siemensPdtReviewsSelectScience.csv","w")

#oFile = open("beckmanPdtReviewsSelectScience.csv","w")

# Open output CSV file and write header

writer = csv.writer(oFile)
writer.writerow(fileHeader) 

# URL List for all companies
# Uncomment the URL's for which data need to be extracted

# For Roche

urlList = ["https://www.selectscience.net/products/cobas-8100-automated-workflow-series/?prodID=180045#reviewstab",
           "https://www.selectscience.net/products/magna-lyser-instrument/?prodID=14082",
           "https://www.selectscience.net/products/roche+hitachi-902/?prodID=12971",
           "https://www.selectscience.net/products/coaguchek---pro-ii/?prodID=205949",
           "https://www.selectscience.net/products/e-170-module-for-modular---analytics-/?prodID=79602"]

'''

# For Abbott

urlList = ['https://www.selectscience.net/products/alere-pbp2a-sa-culture-colony-test/?prodID=173108',
           'https://www.selectscience.net/products/binaxnow---streptococcus-pneumoniae-urinary-antigen-card/?prodID=173106',  
           'https://www.selectscience.net/products/cell-dyn-ruby-hematology-analyzer/?prodID=113802',
           'https://www.selectscience.net/products/i-stat-total--hcg/?prodID=205948',
           'https://www.selectscience.net/products/alere-i-rsv-is-now-id-now-rsv/?prodID=207494',
           'https://www.selectscience.net/products/binaxnow---influenza-a-and-b-card-2/?prodID=173107',
           'https://www.selectscience.net/products/cell-dyn-emerald-hematology-system/?prodID=207202',
           'https://www.selectscience.net/products/alere-i-strep-a-is-now-id-now-strep-a-2/?prodID=205955',
           'https://www.selectscience.net/products/cell-dyn-1800/?prodID=79601',
           'https://www.selectscience.net/products/cell-dyn-sapphire-hematology-analyzer/?prodID=113801',
           'https://www.selectscience.net/products/c-diff-quik-chek-complete--/?prodID=173109',
           #'https://www.selectscience.net/products/alere-i-instrument-is-now-id-now-instrument/?prodID=203785',
           'https://www.selectscience.net/products/alere-cholestech-ldx---system/?prodID=92667',
           'https://www.selectscience.net/products/afinion-crp/?prodID=173105',
           'https://www.selectscience.net/products/cell-dyn-3700/?prodID=84094',
           'https://www.selectscience.net/products/cell-dyn-3200/?prodID=82029',
           'https://www.selectscience.net/products/i-stat-1/?prodID=82028',
           'https://www.selectscience.net/products/pima-analyser/?prodID=196994']

# For Ortho

urlList = ["https://www.selectscience.net/products/ortho-vision-analyzer/?prodID=197538",
           "https://www.selectscience.net/products/vitros-250+350--chemistry-system/?prodID=209470",
           "https://www.selectscience.net/products/ortho-provue/?prodID=195222",
           "https://www.selectscience.net/products/vitros---hiv-combo-test/?prodID=210153",
           "https://www.selectscience.net/products/vitros-4600-chemistry-system/?prodID=204472",
           "https://www.selectscience.net/products/ortho-workstation/?prodID=210373"]  



# For Siemens

urlList = ['https://www.selectscience.net/products/iris/?prodID=210515',  
           'https://www.selectscience.net/products/maxum-edition-ii/?prodID=85661',
           'https://www.selectscience.net/products/atellica-solution/?prodID=209387',
           'https://www.selectscience.net/products/bn-prospec-system/?prodID=195920',
           'https://www.selectscience.net/products/symbia-e/?prodID=210508',
           'https://www.selectscience.net/products/advia---1800-chemistry-system/?prodID=113267',
           'https://www.selectscience.net/products/advia-centaur-xpt-immunoassay-system/?prodID=197003',
           'https://www.selectscience.net/products/bn-ii-system/?prodID=195919',
           'https://www.selectscience.net/products/tissue-preparation-system/?prodID=180109',
           'https://www.selectscience.net/products/dca-vantage---analyzer/?prodID=172868',
           'https://www.selectscience.net/products/clinitek-advantus---urine-chemistry-analyzer/?prodID=194912',
           'https://www.selectscience.net/products/dimension---exl---with-lm-integrated-chemistry-system/?prodID=106742',
           'https://www.selectscience.net/products/sysmex-cs-5100-system/?prodID=172000',
           'https://www.selectscience.net/products/innovance---pfa-200-system/?prodID=113270',
           'https://www.selectscience.net/products/advia-2120-hematology-system/?prodID=79572',
           'https://www.selectscience.net/products/advia---120-hematology-system/?prodID=113272',
           'https://www.selectscience.net/products/advia-centaur---cp-immunoassay-system/?prodID=113279',
           'https://www.selectscience.net/products/magnetom-skyra/?prodID=195193',
           'https://www.selectscience.net/products/versant-kpcr-molecular-system/?prodID=180107',
           'https://www.selectscience.net/products/immulite---2000-immunoassay-system/?prodID=113276',
           'https://www.selectscience.net/products/stratus---cs-200-acute-care-analyzer/?prodID=205950',
           'https://www.selectscience.net/products/rapidpoint---500-blood-gas-systems/?prodID=116360',
           'https://www.selectscience.net/products/advia---2120i-hematology-system-with-autoslide/?prodID=113271']

# For Beckman

urlList = ['https://www.selectscience.net/products/au5822/?prodID=208773',  
           'https://www.selectscience.net/products/access-2-immunoassay-system/?prodID=113649',
           'https://www.selectscience.net/products/dxh-800-hematology-analyzer/?prodID=210169',
           'https://www.selectscience.net/products/au480-chemistry-system/?prodID=113654',
           'https://www.selectscience.net/products/itag-mhc-tetramers/?prodID=84791',
           'https://www.selectscience.net/products/dxc-700-au-chemistry-analyzer/?prodID=208771',
           'https://www.selectscience.net/products/navios-flow-cytometer/?prodID=210000',
           'https://www.selectscience.net/products/biomek-i5-automated-workstation/?prodID=207022',
           'https://www.selectscience.net/products/formapure-dna/?prodID=207556',
           'https://www.selectscience.net/products/multisizer-4e-coulter-counter/?prodID=194858',
           'https://www.selectscience.net/products/allegra-x-30-benchtop-centrifuge/?prodID=196983',
           'https://www.selectscience.net/products/allegra-25r-benchtop-centrifuge/?prodID=204809',
           'https://www.selectscience.net/products/allegra-x-15r-benchtop-centrifuge/?prodID=204810',
           'https://www.selectscience.net/products/ls-13-320-laser-diffraction-analyser/?prodID=79673',
           'https://www.selectscience.net/products/avanti-j-hc-high-capacity-centrifuge/?prodID=10182',
           'https://www.selectscience.net/products/isoflow-sheath-fluid/?prodID=197523',
           'https://www.selectscience.net/products/cytoflex-flow-cytometer/?prodID=204015',
           'https://www.selectscience.net/products/avanti-jxn-30-high-performance-centrifuge/?prodID=197548',
           'https://www.selectscience.net/products/formapure-total/?prodID=209982',
           'https://www.selectscience.net/products/z-series-coulter-counter/?prodID=10042',
           'https://www.selectscience.net/products/ampure-xp---pcr-purification/?prodID=173145',
           'https://www.selectscience.net/products/unicel-dxc-600-synchron-clinical-systems/?prodID=210496',
           'https://www.selectscience.net/products/airfuge-air-driven-ultracentrifuge/?prodID=80159',
           'https://www.selectscience.net/products/microfuge-20-series-benchtop-centrifuge/?prodID=173157',
           'https://www.selectscience.net/products/allegra-6-benchtop-centrifuge/?prodID=92775',
           'https://www.selectscience.net/products/optima-max-tl/?prodID=10185',
           'https://www.selectscience.net/products/biomek-i7-automated-workstation/?prodID=207023',
           'https://www.selectscience.net/products/kaluza-analysis-software/?prodID=197494',
           'https://www.selectscience.net/products/optima-xe-ultracentrifuge/?prodID=194948',
           'https://www.selectscience.net/products/vi-cell-xr-cell-viability-analyzer/?prodID=10044',
           'https://www.selectscience.net/products/allegra-x-14r-refrigerated-benchtop-centrifuge/?prodID=14039',
           'https://www.selectscience.net/products/biomek-nxp-laboratory-automation-workstation/?prodID=13581',
           'https://www.selectscience.net/products/biomek-fx-p--laboratory-workstation/?prodID=10220',
           'https://www.selectscience.net/products/multisizer-3-coulter-counter/?prodID=10046',
           'https://www.selectscience.net/products/avanti-j-e-high-capacity-centrifuge/?prodID=10184',
           'https://www.selectscience.net/products/proteomelab-xl-a+xl-i-analytical-ultracentrifuge-(auc)/?prodID=116304',
           'https://www.selectscience.net/products/microscan-panels/?prodID=180106',
           'https://www.selectscience.net/products/gallios-flow-cytometer/?prodID=194857',
           'https://www.selectscience.net/products/biomek-4000-laboratory-automation-workstation/?prodID=171567',
           'https://www.selectscience.net/products/avanti-j-26s-series-high-performance-centrifuge-system/?prodID=116724',
           'https://www.selectscience.net/products/microscan-walkaway-plus-system-(40-and96)/?prodID=206451',
           'https://www.selectscience.net/products/copan-wasp---walk-away-specimen-processor/?prodID=206455',
           'https://www.selectscience.net/products/bruker-maldi-tof-biotyper----system/?prodID=206454',
           'https://www.selectscience.net/products/coulter-epics-xl-and-xl-mcl-flow-cytometer/?prodID=1678']
           #'https://www.selectscience.net/products/cyan-adp-analyzer/?prodID=83871',
           #'https://www.selectscience.net/products/MoFlo®+Astrios™/?prodID=116848',
           #'https://www.selectscience.net/products/avanti-jxn-26-high-performance-centrifuge/?prodID=195921']
           
'''

# Looping through url list


for urlLine in urlList:
    r = urllib.request.Request(urlLine, headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    html = urllib.request.urlopen(r)
    soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
    
    #print("\n URL:",urlLine,"\n")  
    
    # Loading the JSON content from html
    
    js = json.loads(soup.select_one("script[type=application/ld+json]").text.encode('utf8'), strict=False)    
       
    #js = json.loads(soup.select_one("script[type=application/ld+json]").text.replace('\r\n', '\\r\\n'))
        
    # Initializing and writing to output csv files
    
    fieldnames = ['name','description','image','reviewBody','reviewRating']
    writer = csv.DictWriter(oFile, fieldnames=fieldnames)
        
    # Extracting relevant tags from the JSON data 
    
    for key in js['review']: 
            
        for item in key:    
            if (item == 'reviewBody'):
                if ('name' in item):
                    body = key['name']+"."+key[item]
                else:
                    body = key[item]
                
            if (item == 'reviewRating'):
                rating = key[item]['ratingValue']
        
        writer.writerow({'name': js['name'], 'description': js['description'], 'image': js['image'], 'reviewBody': body, 'reviewRating': rating})
    
    counter += 1
    
print("Number of links decoded:",counter)

oFile.close()
