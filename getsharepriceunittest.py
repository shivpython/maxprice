from get_share_prices import GetsharePrize
import unittest
import os
import random
class TestShareprize(unittest.TestCase):
    # class to test GetsharePrize class
    
    def setUp(self):
            self.companies_list = GetsharePrize("share_prices.csv").readCSVfile()   
    
    
    def test_for_csv_notexist(self):
        #Raise Exception if csv file not exist.        
        sharePricedata = GetsharePrize("no_csv_file.csv")
        self.assertRaises(IOError, lambda:sharePricedata.readCSVfile())        
        
        
    def test_randomcheck_allcompanies(self):  
        #This is a random check, it should check all the values in this array. 
        #Which means all companies, their max prices, year and month.       
        for companylist in self.companies_list:           
            for max_data in random.sample(companylist, 4):
                self.assertTrue(max_data in companylist)
           
    
    def test_max_price(self):
        #CompanyB max price is 100.        
        maxprice_of_companyB = self.companies_list[1][1]        
        self.assertEquals(100, maxprice_of_companyB)
        
        
    def test_maxprice_mnth(self):
        #CompanyD max price month Nov       
        maxprice_mnth_of_companyD = self.companies_list[3][3]               
        self.assertEquals('Nov', maxprice_mnth_of_companyD)
        
        
    def test_maxprice_year(self):
        #CompanyC max price year is 1990          
        maxprice_yr_of_companyC = self.companies_list[2][2]                  
        self.assertEquals('1990', maxprice_yr_of_companyC)
        
        print '\nList for each Company year and month in which the share price was highest \n',\
        self.companies_list
if __name__ == '__main__':
    unittest.main()
