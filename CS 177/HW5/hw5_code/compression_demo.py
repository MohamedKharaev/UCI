'''
UCI CS177: Huffman Coding
    This is DEMONSTRATION code:
    - It gives an example of how to construct Huffman codes for two datasets, 
      plus some visualizations of the data.
    - You may (but do not have to) reuse parts of this code in your solutions.
    - It is NOT a template for the individual questions you must answer,
      for that see the main homework pdf.
'''

from huffman import getHuffmanTree, getFreqDict, getCode, encode, decode, getEntropy
import numpy as np
import matplotlib.pyplot as plt

print("-------The tortoise and the hare.----------")

# construct the frequency dictionary
file = open("theTortoiseAndTheHare.txt","r")  
textData = file.read()
textFreqs = getFreqDict(textData)

# construct the Huffman tree and extract binary codes
textTree = getHuffmanTree(textFreqs)
textCodes = getCode(textTree)
print("\nHuffman code for text data:")
for (key, value) in textCodes.items():
    print(key,'\t',value)

# let's encode the tale
textBinary = encode(textData,textCodes)
print("\nEncoded text data:")
print("%s -------> %s"%(textData,textBinary))
print("Average length (bits per character): ", len(textBinary)/len(textData))
# TODO: to compare average length to entropy, must implement getEntropy()
print("PART A - Entropy:", getEntropy(textFreqs))
print("PART B - The ceiling of entropy and average code length are equal")
# TODO: to decode messages, must implement decode()
messageEncoded = '0110000101010010111100011001111110100101100101001011110'
messageDecoded = decode(messageEncoded,textTree)
print('\nPART C, D - Decoded message:',"".join(messageDecoded))


print("\n\n-----Web session lengths.------")

# construct the frequency dictionary
sessionLengths = np.load("sessionLengths.npy")
webFreqs = {}
for i in range(len(sessionLengths)):
	webFreqs[i+1] = sessionLengths[i]
print('PART E - Entropy:', getEntropy(webFreqs))
# compute and plot session length probabilities
webProbs = sessionLengths/np.sum(sessionLengths)

plt.semilogy(range(1,101), webProbs)
plt.xlabel('Web Session Length')
plt.ylabel('Log of Empirical Probability')
    
# construct the Huffman tree and extract binary codes
webTree = getHuffmanTree(webFreqs)
webCodes = getCode(webTree)
print("\nHuffman code for web data:")
for key in range(1,101):
    print(key,'\t',webCodes[key])

# TODO: to decode session lengths, must implement decode()
webEncoded = '1010001011000011000100000100010100000000001100001'
webDecoded = decode(webEncoded,webTree)
print('PART F - Decoded message:', "".join([str(i) for i in webDecoded]))
print('\nDecoded session lengths: ',webDecoded)
