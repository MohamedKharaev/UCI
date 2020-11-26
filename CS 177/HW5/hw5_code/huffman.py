from heapq import heappop, heappush, heapify
import numpy as np
import math

class Node(object):
    """ 
    Node class which will be used to construct the Huffman Tree.
    Attributes:
        left:   left child of node, or None for leaf nodes
        right:  right child of node, or None for leaf nodes
        item:   symbol for leaf nodes, or None for internal nodes
        weight: symbol frequency (or normalized symbol probability)
    """

    def __init__(self, item, weight):
        self.item = item
        self.weight = weight
        self.left = None
        self.right = None

    def setChildren(self, leftNode, rightNode):
        self.left = leftNode
        self.right = rightNode

    def __repr__(self):
        return "%s - %s -- %s _ %s" % (self.item, self.weight, self.left, self.right)

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight


def getFreqDict(text) :
    """
    Takes a text string as input and returns a dictionary of the letters 
    encountered with a count of how often they appear.
    """
    freqs = {}
    for ch in text :
        freqs[ch] = freqs.get(ch,0) + 1
    return freqs


def getHuffmanTree(freqs_dict):
    """
    Construct a Huffman Tree from the given frequency dictionary
    """
    itemqueue = [Node(key,value) for (key, value) in freqs_dict.items()]
    heapify(itemqueue)
    while len(itemqueue) > 1:
        # select two nodes with lowest frequency
        leftNode = heappop(itemqueue)       
        rightNode = heappop(itemqueue)
        # merge two selected nodes
        newNode = Node(None, leftNode.weight+rightNode.weight)  
        newNode.setChildren(leftNode, rightNode)
        # push the merged node into the priority queue 
        heappush(itemqueue, newNode)
    return itemqueue[0]


def getCode(huffmanTree):
    """
    Generate the binary code from the constructed Huffman tree.
    Args:
        huffmanTree (Node): Huffman tree constructed from dictionary frequencies
    Returns:
        codes (Dictionary): Dictionary where keys are the original symbols,
            and values are the encoded binary sequence.
    """
    codes = {}
    def codeIt(s, node):
        if node.item:
            if not s:
                print('I\'m here')
                codes[node.item] = "0"
            else:
                codes[node.item] = s
        else:
            codeIt(s+"0", node.left)
            codeIt(s+"1", node.right)

    s = ''
    codeIt(s, huffmanTree)
    return codes

def encode(inputS, codes):
    """
    Encode the input string using the given codes.
    Args:
        inputS (iterable): the input sequence
        codes (dictionary): the code book
    Returns:
        encoded (str): the encoded binary sequence
    """
    s = ''
    for i in inputS:
        s += codes[i]
    return s


def decode(binaryS, huffmanTree):
    """
    Decode the binary sequence by traversing the Huffman tree.
    Args:
        binaryS (str): a string sequence like '01001010101' to be decoded
        huffmanTree (Node): the Huffman tree to be used for decoding
    Returns:
        (list): a list of decoded symbols
    """
    ls = []
    cur = huffmanTree
    for i in binaryS:
        if i == '0':
            cur = cur.left
        else:
            cur = cur.right
        if cur.item != None:
            ls.append(cur.item)
            cur = huffmanTree
        # move left if i equals 0, right if i equals 1
        # if reach a leaf (item is not None), append item to ls and return to root        
    print('TODO: Implement Huffman decoding algorithm')
    return ls


def getEntropy(freqs_dict):
    """
    Calculate the entropy of given (possibly not normalized) frequencies.
    Args:
        freqs_dict (dict): key: classes, value: frequencies or normalized pmf
    Returns:
        entropy (float)
    """
    pmf = np.array(list(freqs_dict.values()))
    pmf = pmf/np.sum(pmf)
    print('TODO: Implement computation of entropy from pmf (probability mass function)')
    
    entropy = sum( [(i * math.log(1/i, 2)) for i in pmf] )
    return entropy