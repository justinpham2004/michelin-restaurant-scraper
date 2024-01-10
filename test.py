#import webbrowser, sys 
import scraper


def main():

      #GET LOCATION OF DESIRED FOOD
      ## step one, parse information from a restaurant page
      scraper.allRestaurantData("https://guide.michelin.com/us//osaka-region/restaurants")

      
      #data = scraper.getRestaurantData('https://guide.michelin.com/us/en/tokyo-region/tokyo/restaurant/tensuke')
      #path = excel_transfer.createSpreadsheet(city= "tokyo")
      #path = excel_transfer.inputDataIntoSpreadsheet(path, data, 3)
      ##Step two, add to spreadsheet

      ##Step three, do this, but given a list of restaurants

        #f len(sys.argv) > 1: 
              #webbrowser.open(''.join(sys.argv[1]))
        #else:  
              #webbrowser.open('https://guide.michelin.com/us/en/tokyo-region/tokyo/restaurants/affordable')

#consider using python script in book to open map locaions on google maps, save links to excel file.. ??
#consider actually giving links, and then automate adding of restaurant, location, and notes into existing spreadsheet
            





main()