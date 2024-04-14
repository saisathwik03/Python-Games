"""
15-110 Hw6 - Protein Sequencing Project
Name:B.MAHAVIR KARTHIK
ROLL NO:2023501041
"""

import hw6_protein_tests as test

project = "Protein" # don't edit this

### WEEK 1 ###

'''
readFile(filename)
#1 [Check6-1]
Parameters: str
Returns: str
''' 
#Reading file 
def readFile(filename):
    text = ''  # Initialize the text variable
    file = open(filename, 'r')
    
    for line in file:
        text += line.strip()  # Remove newline characters and append to text
    
    file.close()  # Close the file
    
    return text



'''
dnaToRna(dna, startIndex)
#2 [Check6-1]
Parameters: str ; int
Returns: list of strs
'''
def dnaToRna(dna, startIndex):
    codons = []
    # codon = ""

    # Loop through the DNA sequence starting from the given index
    for i in range(startIndex, len(dna), 3):
        codon = dna[i:i+3]

        # Check if the codon is a stop codon
        if codon in ["TAA", "TAG", "TGA"]:
            codons.append(codon.replace("T","U"))
            break

        # Replace T with U and add the codon to the list
        codons.append(codon.replace("T", "U"))
    return codons



'''
makeCodonDictionary(filename)
#3 [Check6-1]
Parameters: str
Returns: dict mapping strs to strs
'''
def makeCodonDictionary(filename):
    import json
    codon_dict={}
#assigning empty dictionary as codon dict
    with open(filename,'r') as acid:
        amino_codon_map=json.load(acid)
#opening json file
        for amino_acid ,codons in amino_codon_map.items():
            for codon in codons:
                U=codon.replace("T","U")
#replacing T with U to map codons to amino acids
                codon_dict[U]=amino_acid
    return codon_dict


'''
generateProtein(codons, codonD)
#4 [Check6-1]
Parameters: list of strs ; dict mapping strs to strs
Returns: list of strs
'''
#function to convert RNA to Proteins which appends codons to protein list with start and stop
def generateProtein(codons, codonD):
    protein=[]
    for i in range(len(codons)):
        if i==0 and codons[i]=="AUG":
            protein.append("Start")
        elif codonD[codons[i]]=="Stop":
            protein.append(codonD[codons[i]])
            break
        else:
            protein.append(codonD[codons[i]])
    return protein



'''
synthesizeProteins(dnaFilename, codonFilename)
#5 [Check6-1]
Parameters: str ; str
Returns: 2D list of strs
'''
#this function iterates through dna file name and points all rna strands and returns proteins and unused bases
def synthesizeProteins(dnaFilename, codonFilename):
    dna=readFile(dnaFilename)
    codonD=makeCodonDictionary(codonFilename)
    proteins=[]
    bases=0
    i=0
    while i<len(dna):
        if dna[i:i+3]=="ATG":
            rna=dnaToRna(dna,i)
            protein=generateProtein(rna,codonD)
            proteins.append(protein)
            i+=3*len(rna)
        else:
            i+=1
            bases+=1
    print(f"Total Bases: {len(dna)}")
    print(f"Unused Bases: {bases}")
    print(f"Total Synthesized:{len(proteins)}")
    return proteins


def runWeek1():
    print("Human DNA")
    humanProteins = synthesizeProteins("data/filename.txt", "data/codon_table.json")
    print("Elephant DNA")
    elephantProteins = synthesizeProteins("data/elephant_p53.txt", "data/codon_table.json")


### WEEK 2 ###

'''
commonProteins(proteinList1, proteinList2)
#1 [Check6-2]
Parameters: 2D list of strs ; 2D list of strs
Returns: 2D list of strs
'''
#function to find common proteins and append them in a common proteins list
def commonProteins(proteinList1, proteinList2):
    common_proteins = []

    for protein1 in proteinList1:
        for protein2 in proteinList2:
            if protein1 == protein2:
                common_proteins.append(protein1)
    return common_proteins


'''
combineProteins(proteinList)
#2 [Check6-2]
Parameters: 2D list of strs
Returns: list of strs
'''
#searching for repettitive amino acids and append them into a list
def combineProteins(proteinList):
    amino_acids = []
    for protein in proteinList:
        amino_acids.extend(protein)
    return amino_acids




'''
aminoAcidDictionary(aaList)
#3 [Check6-2]
Parameters: list of strs
Returns: dict mapping strs to ints
'''
#making the repeated amino acid into a dictionary such that it consists of acid as key and repettive number as value
def aminoAcidDictionary(aaList):
    aa={}
    for amino_acid in aaList:
        if amino_acid in aa:
            aa[amino_acid]+=1
        else:
            aa[amino_acid]=1
    
    return aa


'''
findAminoAcidDifferences(proteinList1, proteinList2, cutoff)
#4 [Check6-2]
Parameters: 2D list of strs ; 2D list of strs ; float
Returns: 2D list of values
'''
#This takes two protein lists and a float cutoff and returns a list of three element lists, where the first element in the list is an amino acid, the second element is the frequency of that amino acid in proteinList1, and the third element is the frequency of that amino acid in proteinList2
def findAminoAcidDifferences(proteinList1, proteinList2, cutoff):
    combinedlist1 = combineProteins(proteinList1)
    combinedlist2 = combineProteins(proteinList2)
    dict1 = aminoAcidDictionary(combinedlist1)
    dict2 = aminoAcidDictionary(combinedlist2)
    differences = []
    for aminoacid in dict2:
        if aminoacid not in dict1:
            dict1[aminoacid] = 0
    for aminoacid in dict1:
        if aminoacid not in dict2:
            dict2[aminoacid] = 0
    for aminoacid in dict1:
        if (aminoacid != "Start") and (aminoacid != "Stop") and (abs((dict1[aminoacid]/len(combinedlist1))-(dict2[aminoacid]/len(combinedlist2)))>cutoff) : # To exclude start and stop
            differences.append([aminoacid,dict1[aminoacid]/len(combinedlist1),dict2[aminoacid]/len(combinedlist2)])  
    return differences


'''
displayTextResults(commonalities, differences)
#5 [Check6-2]
Parameters: 2D list of strs ; 2D list of values
Returns: None
'''
#it prints common proteins and different acids
def displayTextResults(commonalities, differences):
    print("The following proteins occurred in both DNA Sequences:")
    for common in commonalities:
        print(" ".join(common))

    print("\nAmino acids with differences exceeding the cutoff:")
    for diff in differences:
        print(f"Amino Acid: {diff[0]}")
        print(f"Percentage in Protein Set 1: {diff[1]:.3f}")
        print(f"Percentage in Protein Set 2: {diff[2]:.3f}")
        print()


def runWeek2():

    humanProteins = synthesizeProteins("data/human_p53.txt", "data/codon_table.json")
    elephantProteins = synthesizeProteins("data/elephant_p53.txt", "data/codon_table.json")

    commonalities = commonProteins(humanProteins, elephantProteins)
    differences = findAminoAcidDifferences(humanProteins, elephantProteins, 0.005)
    displayTextResults(commonalities, differences)


### WEEK 3 ###

'''
makeAminoAcidLabels(proteinList1, proteinList2)
#2 [Hw6]
Parameters: 2D list of strs ; 2D list of strs
Returns: list of strs
'''
#finds amino acids occur in both genes returns sorted list of acids
def makeAminoAcidLabels(proteinList1, proteinList2):
    combined_proteins=combineProteins(proteinList1+proteinList2)
    amino_acid_dict=aminoAcidDictionary(combined_proteins)
    amino_acid_labels=sorted(amino_acid_dict.keys())
    return amino_acid_labels


'''
setupChartData(labels, proteinList)
#3 [Hw6]
Parameters: list of strs ; 2D list of strs
Returns: list of floats
'''
def setupChartData(labels, proteinList):    # this function is used to create a frequency list which consists of frequencies of each gene. 
    combined_proteins=combineProteins(proteinList)
    dict=aminoAcidDictionary(combined_proteins)
    frequency_list=[]
    for amino_acid in labels:
        if amino_acid in combined_proteins:        
            frequency_list.append(dict[amino_acid]/len(combined_proteins))    # appending frequency 
        else:
            frequency_list.append(0.0)
    
    return frequency_list


'''
createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None)
#4 [Hw6] & #5 [Hw6]
Parameters: list of strs ; list of floats ; str ; list of floats ; str ; [optional] list of strs
Returns: None
'''
#function to plot bar graph
def createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None):
    import matplotlib.pyplot as plt
    w=0.35
    plt.bar(xLabels,freqList1,width=-w,align='edge',label=label1,edgecolor=edgeList)
    plt.bar(xLabels,freqList2,width=w,align='edge',label=label2,edgecolor=edgeList)
    plt.legend()
    plt.show()
    return
'''
makeEdgeList(labels, biggestDiffs)
#5 [Hw6]
Parameters: list of strs ; 2D list of values
Returns: list of strs
'''
def makeEdgeList(labels, biggestDiffs):         # this function returns a 1D list where each element of the list is "black" if the corresponding amino acid is in the biggestDiffs list and "white" otherwise.
    edge_colors=[]                              # list with Black and white colors for index.
    amino_acid=[item[0] for item in biggestDiffs]
    for i in labels:
        if i in amino_acid:                     # if amino_acid is present in biggestDiffs, black color edgelist is added.
            edge_colors.append("black")
        else:
            edge_colors.append("white")         # else , white color edgelist is added.

    return edge_colors


'''
runFullProgram()
#6 [Hw6]
Parameters: no parameters
Returns: None
'''
def runFullProgram():   # Main function to generate graphs,  flow of process to get the analysis
    human_protein=synthesizeProteins("data/human_p53.txt", "data/codon_table.json")
    elephant_protein=synthesizeProteins("data/elephant_p53.txt", "data/codon_table.json")
    similarities=commonProteins(human_protein,elephant_protein)
    differences=findAminoAcidDifferences(human_protein,elephant_protein,0.005) # cutoff given as 0.5% which is 0.005 
    displayTextResults(similarities,differences)
    labels_on_x=makeAminoAcidLabels(human_protein,elephant_protein)
    frequency1=setupChartData(labels_on_x,human_protein)
    frequency2=setupChartData(labels_on_x,elephant_protein)
    edgelist=makeEdgeList(labels_on_x,differences)
    createChart(labels_on_x,frequency1,"Human Genes",frequency2,"Elephant Genes",edgelist)

### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    # print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    # test.week1Tests()
    # test.testReadFile()
    # test.testDnaToRna()
    # test.testMakeCodonDictionary()
    # test.testGenerateProtein()
    # test.testSynthesizeProteins()
    # print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    # runWeek1()

    ## Uncomment these for Week 2 ##
    
    # print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    # test.week2Tests()
    # test.testCommonProteins()
    # test.testCombineProteins()
    # test.testAminoAcidDictionary()
    # test.testFindAminoAcidDifferences()
    
    # print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    # runWeek2()
    

    ## Uncomment these for Week 3 ##
    
    # print("\n" + "#"*15 + " WEEK 3 TESTS " +  "#" * 16 + "\n")
    # test.week3Tests()
    # test.testMakeAminoAcidLabels()
    # test.testSetupChartData()
    # test.testCreateChart()
    # test.testMakeEdgeList()
    # print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    runFullProgram()
    # """
