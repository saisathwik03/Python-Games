"""
15-110 Hw6 - Protein Sequencing Project
Name: J Sai Sathwik
Roll No: 2023501066 
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
def readFile(filename):
    txt=''
    f=open(filename, "r")
    text=f.read()
    for each in text:
        txt+= each.strip()
    f.close()
    return txt


'''
dnaToRna(dna, startIndex)
#2 [Check6-1]
Parameters: str ; int
Returns: list of strs
'''
def dnaToRna(dna, startIndex):
    codons=[]
    rna=''
    for i in range(startIndex, len(dna),3):
        codon=dna[i:i+3]
        rna=codon.replace('T','U')
        codons.append(rna)
        if rna in ('UAA', 'UAG', 'UGA'):
            break
        
    return codons

'''
makeCodonDictionary(filename)
#3 [Check6-1]
Parameters: str
Returns: dict mapping strs to strs
'''
def makeCodonDictionary(filename):
    import json
    d={}
    with open(filename,"r") as file:
        amino_to_codon=json.load(file)
        for aminoacids, codon in amino_to_codon.items():
            for i in codon:
                x=i.replace("T","U")
                d[x]=aminoacids
    return d


'''
generateProtein(codons, codonD)
#4 [Check6-1]
Parameters: list of strs ; dict mapping strs to strs
Returns: list of strs
'''
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
def synthesizeProteins(dnaFilename, codonFilename):
    dna=readFile(dnaFilename)
    codonD=makeCodonDictionary(codonFilename)
    proteins=[]
    base_count=0
    i=0
    while i<len(dna):
        if dna[i:i+3]=="ATG":
            rna=dnaToRna(dna,i)
            protein=generateProtein(rna,codonD)
            proteins.append(protein)
            i+=3*len(rna)
        else:
            i+=1
            base_count+=1
    print("Total Bases:", len(dna))
    print("Unused Bases:", base_count)
    print("Total Synthesized:",len(proteins))
    return proteins


def runWeek1():
    print("Human DNA")
    humanProteins = synthesizeProteins("data/human_p53.txt", "data/codon_table.json")
    print("Elephant DNA")
    elephantProteins = synthesizeProteins("data/elephant_p53.txt", "data/codon_table.json")


### WEEK 2 ###

'''
commonProteins(proteinList1, proteinList2)
#1 [Check6-2]
Parameters: 2D list of strs ; 2D list of strs
Returns: 2D list of strs
'''
def commonProteins(proteinList1, proteinList2):
    common_proteins = []
    for protein in proteinList1:
        if protein in proteinList2:
            common_proteins.append(protein)
    return common_proteins

'''
combineProteins(proteinList)
#2 [Check6-2]
Parameters: 2D list of strs
Returns: list of strs
'''
def combineProteins(proteinList):
    aminoacids = []
    for protein in proteinList:
        for aminoacid in protein:
            aminoacids.append(aminoacid)
    return aminoacids

'''
aminoAcidDictionary(aaList)
#3 [Check6-2]
Parameters: list of strs
Returns: dict mapping strs to ints
'''
def aminoAcidDictionary(aaList):
    d={}
    for i in aaList:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d


'''
findAminoAcidDifferences(proteinList1, proteinList2, cutoff)
#4 [Check6-2]
Parameters: 2D list of strs ; 2D list of strs ; float
Returns: 2D list of values
'''
def findAminoAcidDifferences(proteinList1, proteinList2, cutoff):
    combinedList1 = combineProteins(proteinList1)
    combinedList2 = combineProteins(proteinList2)
    dict1 = aminoAcidDictionary(combinedList1)
    dict2 = aminoAcidDictionary(combinedList2)
    differences = []
    for aminoAcid in dict1.keys() | dict2.keys():
        if aminoAcid not in ('Start', 'Stop'):
            frequency1 = dict1.get(aminoAcid, 0) / len(combinedList1)
            frequency2 = dict2.get(aminoAcid, 0) / len(combinedList2)

            if abs(frequency1 - frequency2) > cutoff:
                differences.append([aminoAcid, frequency1, frequency2])

    return differences
    


'''
displayTextResults(commonalities, differences)
#5 [Check6-2]
Parameters: 2D list of strs ; 2D list of values
Returns: None
'''
def displayTextResults(commonalities, differences):
    print("The following proteins occurred in both DNA Sequences:")
    for common in commonalities:
        print(" ".join(common))

    print("\nAmino acids with differences exceeding the cutoff:")
    for diff in differences:
        print("Amino Acid:", diff[0])
        print("Percentage in Protein Set 1:" ,diff[1])
        print("Percentage in Protein Set 2:", diff[2])
        print()
    return


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
def makeAminoAcidLabels(proteinList1, proteinList2):
    proteins_in_combined=combineProteins(proteinList1+proteinList2)
    amino_acid_dict=aminoAcidDictionary(proteins_in_combined)
    aminoacidlabels=list(amino_acid_dict.keys())
    aminoacidlabels.sort()
    return aminoacidlabels


'''
setupChartData(labels, proteinList)
#3 [Hw6]
Parameters: list of strs ; 2D list of strs
Returns: list of floats
'''
def setupChartData(labels, proteinList):
    frequency_lst=[]
    proteins_in_combined=combineProteins(proteinList)
    amino_acid_dict=aminoAcidDictionary(proteins_in_combined)
    for amino_acid in labels:
        if amino_acid in proteins_in_combined:        
            frequency_lst.append(amino_acid_dict[amino_acid]/len(proteins_in_combined)) 
        else:
            frequency_lst.append(0.0)
    
    return frequency_lst



'''
createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None)
#4 [Hw6] & #5 [Hw6]
Parameters: list of strs ; list of floats ; str ; list of floats ; str ; [optional] list of strs
Returns: None
'''

def createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None):
    import matplotlib.pyplot as plt
    import numpy as np
    bar_width=0.40
    plt.bar(xLabels,freqList1,width=-bar_width,align='edge',label=label1,edgecolor=edgeList)
    plt.bar(xLabels,freqList2,width=bar_width,align='edge',label=label2,edgecolor=edgeList)
    plt.xlabel('AMINO ACIDS')
    plt.ylabel('FREQUENCY')
    plt.title('AMINO ACID FREQUENCY COMPARISON')
    plt.legend()
    plt.show()
    return
'''
makeEdgeList(labels, biggestDiffs)
#5 [Hw6]
Parameters: list of strs ; 2D list of values
Returns: list of strs
'''
def makeEdgeList(labels, biggestDiffs):
    color=[]                              
    amino_acid=[element[0] for element in biggestDiffs]
    for i in labels:
        if i in amino_acid:                     
            color.append("black")
        else:
            color.append("white")        

    return color

'''
runFullProgram()
#6 [Hw6]
Parameters: no parameters
Returns: None
'''
def runFullProgram():
    human_protein=synthesizeProteins("data/human_p53.txt", "data/codon_table.json")
    elephant_protein=synthesizeProteins("data/elephant_p53.txt", "data/codon_table.json")
    similarities=commonProteins(human_protein,elephant_protein)
    differences=findAminoAcidDifferences(human_protein,elephant_protein,0.005)  
    displayTextResults(similarities,differences)
    labels_on_x=makeAminoAcidLabels(human_protein,elephant_protein)
    freqList1=setupChartData(labels_on_x,human_protein)
    freqList2=setupChartData(labels_on_x,elephant_protein)
    edgelist=makeEdgeList(labels_on_x,differences)
    createChart(labels_on_x,freqList1,"Human Genes",freqList2,"Elephant Genes",edgelist)
    
    return


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
    runWeek2()
    

    ## Uncomment these for Week 3 ##
    
    # print("\n" + "#"*15 + " WEEK 3 TESTS " +  "#" * 16 + "\n")
    # test.week3Tests()
    # test.testMakeAminoAcidLabels()
    # test.testSetupChartData()
    # test.testCreateChart()
    # test.testMakeEdgeList()
    # print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    # runFullProgram()