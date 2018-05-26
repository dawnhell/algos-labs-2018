text = 'abdfbcbedbabcfefbdddedbbfababc'

def build_huffman_tree(text):
    f = {}

    for char in text:
        if char in f:
            f[char] = f[char] + 1
        else:
            f[char] = 1

    ht = []
    for item in f.items():
        ht.append((item[0], item[1]))

    while len(ht) > 1:
        ht.sort(key=lambda item: item[1])
        new_node = (ht[0][0] + ht[1][0], ht[0][1] + ht[1][1], ht[0], ht[1])

        ht.pop(0)
        ht[0] = new_node
    return ht[0]

def encode_symbol(char, tree, code = []):
    if len(tree[0]) > 1:
        if char in tree[2][0]:
            code.append('0')
            return encode_symbol(char, tree[2], code)
        else:
            code.append('1')
            return encode_symbol(char, tree[3], code)
    elif tree[0] == char:
        return code
    else:
        raise Exception("Symbol '%c' is not in the tree" % char)

def encode_alphabet(alphabet, tree):
    encoding = {}
    for char in alphabet:
        encoding[char] = encode_symbol(char, tree, [])
    return encoding

def encode_message(text, table):
    code = []
    for char in text:
        code.extend(table[char])
    return ''.join(code)

def decode_message(code, tree):
    tree_iter = tree
    message = ''
    for bit in code:
        tree_iter = tree_iter[2 if bit == '0' else 3]
        if len(tree_iter[0]) == 1:
            message = message + tree_iter[0]
            tree_iter = tree
    return message

tree = build_huffman_tree(text)
print('Huffman tree')
print(tree)

table = encode_alphabet(tree[0], tree)
print("Code table: %s" % table)

code = encode_message(text, table)

print("Encoded sequence: %s" % code)
print("Decoded sequence: %s" % decode_message(code, tree))