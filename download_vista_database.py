#version 1 
#10/20/2015
#Module -> downloading from the Vista Enhancer Browser
#Url: http://enhancer.lbl.gov/frnt_page_n.shtml
#Scope of this module is to downlaod info for Human Enhancers from VISTA Database
#For corrections ikagiampis@gmail.com

#URL FORMAT: http://enhancer.lbl.gov/cgi-bin/imagedb3.pl?show=1;page=1;search.form=no;form=search;chrom=chr1;search.org=Human;end=5000000;page_size=20000;search.result=yes;action=search;start=3000000;search.sequence=1

#Hg19 gene coordinates: http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/knownGene.txt.gz

#Size of the Humnan Chromosomes (GRCh38.p5): 
#http://www.ncbi.nlm.nih.gov/projects/genome/assembly/grc/human/data/

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas import read_html

from numpy.random import randn
from scipy import stats
from pandas.tools.plotting import scatter_matrix
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import re
import os
import scipy.cluster.hierarchy as hier
import pylab as pl
import matplotlib.ticker as mticker
import html5lib

from Bio.pairwise2 import format_alignment
from urllib.request import urlopen

%matplotlib inline

chromInfo = pd.read_csv('Hg38_chromosomes_lengths.txt', sep = '\t')

def make_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def making_url(value):
    
    def download_save(URL, chrom):
        
        print(URL)
        
        make_directory('Enhancer_Database_VISTA')
        
        path = 'Enhancer_Database_VISTA' + '/' + chrom + '.txt'
        
        data = urlopen(URL)
        
        with open(path, "wb") as code:
            code.write(data.read())
        

    chrom, chrom_end = value
    
    chrom_end = chrom_end.replace(",", "")
    
    part1 = 'http://enhancer.lbl.gov/cgi-bin/imagedb3.pl?show=1;page=1;search.form=no;form=search;chrom=chr'
    
    part3 = ';search.org=Human;end='
    
    part5 = ';page_size=20000;search.result=yes;action=search;start=3000000;search.sequence=1'
    
    fullURL = part1 + str(chrom) + part3 + str(chrom_end) + part5
    
    download_save(fullURL, chrom)
    
    return fullURL

chromInfo['URLs'] = chromInfo[['chr', 'total length']].apply(making_url, axis =1)

print(chromInfo)
