from get_share_prices import GetsharePrize
import unittest
import os
class TestShareprize(unittest.TestCase):
    
    # class to test GetsharePrize class
    
    def test_for_csv_notexist(self):
        #Raise Exception if csv file not exist.        
        sharePricedata = GetsharePrize("no_csv_file.csv")
        self.assertRaises(IOError, lambda:sharePricedata.readCSVfile())
        
    def test_max_price(self):
        #CompanyB max price is 100.
        sharePricedata = GetsharePrize("share_prices.csv")
        self.price = sharePricedata.readCSVfile()       
        self.assertEquals(100, self.price[1][1])
        
    def test_maxprice_mnth(self):
        #CompanyD max price month Nov
        sharePricedata = GetsharePrize("share_prices.csv")
        self.month=sharePricedata.readCSVfile()        
        self.assertEquals('Nov', self.month[3][3])
        
    def test_maxprice_year(self):
        #CompanyC max price year is 1990
        sharePricedata = GetsharePrize("share_prices.csv")
        self.year=sharePricedata.readCSVfile()        
        self.assertEquals('1990', self.year[2][2])
        
        print '\nList for each Company year and month in which the share price was highest \n',\
        sharePricedata.readCSVfile()
if __name__ == '__main__':
    unittest.main()
