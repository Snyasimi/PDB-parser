import re,sys
PDB_FILE = sys.argv[1]
CHAIN_A=[]
CHAIN_B=[]
 
def Check_file(PDB_FILE):
    if re.search("^\S\w+\.pdb$",PDB_FILE):
        print(f"{PDB_FILE} is valid")
        return PDB_FILE
    else:
        print("Not valid")

def parse_file():
    file_pdb = Check_file(PDB_FILE)
    try:

        with open(f"{PDB_FILE}","r") as f:
            contents = f.read()
            #SCRAPING THE AMMINOS TODO
            HEADER = re.findall("HEADER .+" ,contents)
            TITLES = re.findall("TITLE .+",contents)
            DBREF = re.findall("DBREF .+",contents)
            HELIX = re.findall("HELIX .+",contents)
            SHEET = re.findall("SHEET .+",contents)
            SEQRES = re.findall("SEQRES .+",contents)
            AMMINO = re.search("((A-Z){3}) +",contents)
            
            print(type(SEQRES))
            AMMINO_ACIDS=[]
            for i in SEQRES:
                p = re.split("\s",i,1)
                print(p[1])
                

                #take only the amminos

                Ammino_acids = re.findall("([A-Z]{3})+",p[1])
                for t in Ammino_acids:
                    AMMINO_ACIDS.append(t)
                

                print(Ammino_acids)
                
                

                #CHAINS
                if re.search("[A-Z]{1}",p[1]):
                    
                    chain = re.search("[A-Z]{1}",p[1])
                    if chain.group(0)=="A":
                        print(chain.group(0))
                        print(chain.group(0))
                        CHAIN_A.append(chain.group(0))
                        print(CHAIN_A)
                    print("yes")


            print(len(AMMINO_ACIDS))
            print(AMMINO_ACIDS)

        
        
        def identify_chain(STRUCTURE):
            #HAVE TO DECLARE CHAIN LIST OUT OF FUNCTION
            for item in STRUCTURE:
                line = re.split("\s",item,1)
                

                



            
            #for line in SEQRES:
                #acids = re.search("(A-Z{3})",line)
                #print(acids.group(1))
            #for i in AMMINO:

            #print(AMMINO.group(0))
        

            #print(HEADER[0])
            #print(TITLES[0])
            #print(TITLES[1])
            #print("---------------------------------------------------------\n-----------------------------------------------")
            #print all seqres
            
            #for i in SEQRES:
              #print(i)

            #print all HELIX
            #for h in HELIX:
                #print(h)

            print("THE LENGTH OF HELIX IS : " + str(len(HELIX)))
        


            #print all SHEETS

            #for s in SHEET:
                #print(s)



            #if re.search("SEQRES .+",contents):
                #print("SEQ PRESENT")
            #if re.search("TITLE .+",contents):
                #print("TITLE CHECk")

            #print(HEADER[0])
            print("-----------------")
        
            print("-------------------------------------------------------------")
            #print(SEQRES)
            
            #print(get_info(HELIX))
            identify_chain(HELIX)


    except FileNotFoundError:
        print("The file does not exist")
        



parse_file()


    
