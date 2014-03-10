import csv
import random
from operator import itemgetter


class GetsharePrize:    

    def __init__(self, path):
        self.path = path
         
    def writeCSVfile(self):
        try:
            with open(self.path, 'w') as csfile:
                
                print 'file created'
                writer = csv.writer(csfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow(["Year","Month","CompanyA","CompanyB","CompanyC",\
                                 "CompanyD","CompanyE","CompanyF","CompanyG",\
                                 "CompanyH","CompanyI","CompanyJ"])
                
                cnt = 0
                lyr = 1990 
                #for each in range(276):
                for each in range(48):
                           
                    mont = ('Jan','Feb','Mar','Aprl','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
                    my_randoms = random.sample(xrange(100), 13)
                    writer.writerow([lyr,mont[cnt],my_randoms[cnt],my_randoms[cnt]+2,\
                                     my_randoms[cnt]+4,my_randoms[cnt]+5,\
                                     my_randoms[cnt]+7,my_randoms[cnt]+10,\
                                     my_randoms[cnt]+15,my_randoms[cnt]+9,\
                                     my_randoms[cnt]+14,my_randoms[cnt]+8])
                    cnt += 1
                    if cnt is 12:
                        lyr += 1
                        cnt = 0
        except IOError, error:
            print "I/OError:%r"%(error)
            raise IOError("FileDoesnotExist")
        
    
    def readCSVfile(self):
        #function to read the csv file n genrate the list for max price.
        try:            
            with open(self.path,'r') as csvfile:            
                columns = zip(*csv.reader(csvfile))
                year, month = columns[:2]
                data = columns[2:]    
            resultlist = list()
            for pricelist in data:
                name = pricelist[0]
                prices = map(int, pricelist[1:])
                i, price = max(enumerate(prices), key=itemgetter(1))
                resultlist.append((name, price, year[i+1], month[i+1]))               
            return resultlist 
        
        except IOError, err:
            print "IOError : %r" %(err)
            raise IOError("File dosen't Exist")

       
        
        
        
    
    
