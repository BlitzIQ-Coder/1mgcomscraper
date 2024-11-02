#from subprocess import call
import onemg_cetaphil1_scraping, onemg_lasheild_scraping, onemg_thedermaco_scraping
import onemg_cetaphil2_scraping, onemg_cerave_scraping
print("By: BlitzIQ")     
print("1🇲🇬.🇨🇴🇲 🇸🇨🇷🇦🇵🇪🇷")
print(" 1🇲🇬.🇨🇴🇲 🇸🇨🇷🇦🇵🇪🇷")
print("  1🇲🇬.🇨🇴🇲 🇸🇨🇷🇦🇵🇪🇷")
print("Program to scrape required available details from 1mg.com")
                                                                                                                                                                                                                       
def main():
    while True:
        print("\nMENU:")
        print("1. Cetaphil Products")
        print("2. La Shield Products")
        print("3. Cerave Products")
        print("4. The Derma Co Products")
        print("5. EXIT")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            print("Getting you Cetaphil Products...")
            onemg_cetaphil1_scraping.cetaphil1()
            onemg_cetaphil2_scraping.cetaphil2()
            #call(["python", "onemg_cetaphil1_scraping.py"])
            #call(["python", "onemg_cetaphil2_scraping.py"])
            #os.system('python onemg_cetaphil1_scraping.py')
            #subprocess.run(["python", "onemg_cetaphil2_scraping.py"])
        elif choice == '2':
            print("Getting you La-Shield Products...")
            onemg_lasheild_scraping.lasheild()
            #call(["python", "onemg_lasheild_scraping.py"])
            #subprocess.run(["python", "scraper2.py"])
        elif choice == '3':
            print("Getting you Cerave Products...")
            onemg_cerave_scraping.cerave()
            #call(["python", "onemg_cerave_scraping.py"])

        elif choice == '4':
            print("Getting you The-Derma-Co Products...")
            onemg_thedermaco_scraping.thedermaco()
            #call(["python", "onemg_thedermaco_scraping.py"])  
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

#if __name__ == "__main__":
main()
 
