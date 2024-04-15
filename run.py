import module_1.verifier
import module_2.scrapper
import module_3.aioutput
import module_3.unitTesting

#Zayne Bonner
#800756759


def main():
    #this runs module_3, which is the new OpenAI API scrapper for project 3, 
    #module_3.aioutput.performAction()
    
    print(module_3.unitTesting.TestKey(module_3.aioutput.key))

    #module_1.verifier.Verify()                           #all of this is project 2 stuff; not necessary.
    #for idx,e in enumerate(module_1.verifier.verified):  #verifies each article for module_2 to utilize
    #    verified.append(module_1.verifier.verified[idx])
    #module_2.scrapper.MyScrapper.ScrapNeat(verified)     #scrapes the articles into a processed format.
    #module_2.scrapper.MyScrapper.ScrapRaw(verified)      #scrapes the articles into their raw format.


verified=[]
main()
print("Output scrapped and exported to Data folder.")