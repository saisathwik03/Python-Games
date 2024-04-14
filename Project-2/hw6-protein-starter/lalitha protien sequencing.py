"""
15-110 Hw6 - Protein Sequencing Project
Name: H V Lalitha Parameswari
AndrewID:
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
    lines=""
    file=open(filename,'r')
    reader=file.read()
    for line in reader:
        lines+=line.replace("\n",'')
    file.close()
    return lines


'''
dnaToRna(dna, startIndex)
#2 [Check6-1]
Parameters: str ; int
Returns: list of strs
'''
def dnaToRna(dna, startIndex):
    codons = []
    i = startIndex
    
    while i < len(dna):
        codon = dna[i:i+3]
        rna_codon = codon.replace("T", "U")
        codons.append(rna_codon)
        if rna_codon in ["UAA", "UAG", "UGA"]:
            break
        i+=3
    return codons


'''
makeCodonDictionary(filename)
#3 [Check6-1]
Parameters: str
Returns: dict mapping strs to strs
'''
def makeCodonDictionary(filename):
    import json
    dic={}
    with open(filename,"r") as file:
        amino_to_codon= json.load(file)
        for aminoacids,condon in amino_to_codon.items():
            for i in condon:
                x=i.replace("T","U")
                dic[x]=aminoacids

    return dic


'''
generateProtein(codons, codonD)
#4 [Check6-1]
Parameters: list of strs ; dict mapping strs to strs
Returns: list of strs
'''
def generateProtein(codons, codonD):
    protein = []
    for i in range(len(codons)):
        if i==0 and codons[i] == "AUG":
           protein.append('Start')
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
    print("Total Bases: ",len(dna))
    print("Unused Bases: ",bases)
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
    common_proteins=[]
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
    amino_acids = []
    for protein in proteinList:
        for aminoacid in protein:
            amino_acids.append(aminoacid)

    return amino_acids


'''
aminoAcidDictionary(aaList)
#3 [Check6-2]
Parameters: list of strs
Returns: dict mapping strs to ints
'''
def aminoAcidDictionary(aaList):
    aa={}
    for amino in aaList:
        if amino not in aa:
            aa[amino]=1
        else:
            aa[amino]+=1
    return aa


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
    # print("The following proteins occurred in both DNA Sequences:")
    # for common in commonalities:
    #     print(" ".join(common))

    # print("\nAmino acids with differences exceeding the cutoff:")
    # for diff in differences:
    #     print(f"Amino Acid: {diff[0]}")
    #     print(f"Percentage in Protein Set 1: {diff[1]:.3f}")
    #     print(f"Percentage in Protein Set 2: {diff[2]:.3f}")
    #     print()
    print("The following proteins occurred in both DNA Sequences:")
    for common in commonalities:
       print(' '.join(common))

    print("\nAmino acids with differences exceeding the cutoff:")
    for amino_acid, freq1, freq2 in differences:
        print(f"{amino_acid} : {freq1 * 100:.3f} in Protein Set 1,\n{freq2 * 100:.3f} in Protein Set 2")

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
    combinedproteins=combineProteins(proteinList1+proteinList2)
    aminoaciddict=aminoAcidDictionary(combinedproteins)
    aminoacidlabels=list(aminoaciddict.keys())
    aminoacidlabels.sort()
    return aminoacidlabels


'''
setupChartData(labels, proteinList)
#3 [Hw6]
Parameters: list of strs ; 2D list of strs
Returns: list of floats
'''
def setupChartData(labels, proteinList):
    combined_proteins = combineProteins(proteinList)
    amino_acid_dict = aminoAcidDictionary(combined_proteins)
    frequency_list=[]
    for amino_acid in labels:
        if amino_acid in amino_acid_dict:
            frequency= amino_acid_dict.get(amino_acid, 0) / len(combined_proteins)
        else:
            frequency=0.0
        frequency_list.append(frequency)

    return frequency_list





'''
createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None)
#4 [Hw6] & #5 [Hw6]
Parameters: list of strs ; list of floats ; str ; list of floats ; str ; [optional] list of strs
Returns: None
'''
def createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None):
    import matplotlib.pyplot as plt
    import numpy as np
    bar_width = 0.40
    x1 = np.arange(len(xLabels))
    x2 = [x + bar_width for x in x1]
    plt.bar(x1, freqList1, width=bar_width, label=label1)
    plt.bar(x2, freqList2, width=bar_width, label=label2)
    # plt.bar(x1, freqList1, width=bar_width,align='edge',label=label1,edgecolor=edgeList)
    # plt.bar(x2, freqList2, width=bar_width,align='edge',label=label1,edgecolor=edgeList)
    plt.xlabel('Amino Acids')
    plt.ylabel('Frequency')
    plt.title('Amino Acid Frequency Comparison')
    plt.xticks(x1 + bar_width / 2, xLabels)
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

    color = []

    for label in labels:
        if label in [i[0] for i in biggestDiffs]:
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
    # print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    # runWeek1()
    #test.testReadFile()
    # test.testDnaToRna()
    #test.testMakeCodonDictionary()
    #test.testGenerateProtein()
    #test.testSynthesizeProteins()
    # test.testFindAminoAcidDifferences()


    ## Uncomment these for Week 2 ##
    """
    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    runWeek2()
    """
    #test.testCommonProteins()
    # test.testCombineProteins()
    # test.testFindAminoAcidDifferences()
    # runWeek2()

    ## Uncomment these for Week 3 ##
    """
    print("\n" + "#"*15 + " WEEK 3 TESTS " +  "#" * 16 + "\n")
    test.week3Tests()
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    runFullProgram()
    """
    # test.testMakeAminoAcidLabels()
    # test.testSetupChartData()
    # test.testCreateChart()
    # test.testMakeEdgeList()
    runFullProgram()
