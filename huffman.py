codeDict = {}

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def huffman_tree(frequency):
    priority_queue = []
    for char, freq in frequency.items():
        priority_queue.append((freq, Node(char)))

    while len(priority_queue) > 1:
        priority_queue.sort(key=lambda x: x[0])
        freq1, firstElement = priority_queue.pop(0)
        freq2, secondElemet = priority_queue.pop(0)
        merged_freq = freq1 + freq2
        merged_node = Node(None)
        merged_node.left = firstElement
        merged_node.right = secondElemet
        priority_queue.append((merged_freq, merged_node))
    return priority_queue[0][1]

def dfs(node, code=""):
    if node is not None:
        if node.value is not None:
            codeDict[node.value]=code      
        dfs(node.left, code + "0")
        dfs(node.right, code + "1")
        
def encode(text):
    stringEncoded = ''
    for i in text: 
        stringEncoded+=codeDict[i]
    return stringEncoded

def decode(text):
    stringDecoded = ''
    current_code = ''
    for char in text:
        current_code += char
        for char, code in codeDict.items():
            if code == current_code:
                stringDecoded += char
                current_code = ''
                break
    print("Decode",stringDecoded)

def spaceSaving(text):
    print('Uncompressed size:',len(text)*8)
    print('Compressed size:',len(encode(text)))
    print('Compression ratio:', round((len(text)*8) / len(encode(text)), 2))
    print('Saving Space:', round((1 - (len(encode(text))/(len(text)*8))) * 100, 2), '%')

def huffman():
    frequency = {}
    string = input(str("Type a text:\n"))
    for i in string:
        if i in frequency: 
            frequency[i] += 1
        else:
            frequency[i] = 1
    frequencyTree = huffman_tree(frequency)
    dfs(frequencyTree)
    spaceSaving(string)
    print("Encode",encode(string))
    decode(encode(string))
huffman()
