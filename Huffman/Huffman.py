def main():
    letter_frequency = {}

    with open("input.txt", "r") as f:
        for letter in f.read():
            if letter not in letter_frequency:
                letter_frequency[letter] = 0
            letter_frequency[letter] += 1

    print("Frequencies:", letter_frequency)
    huffman_tree = build_huffman_tree([(letter, letter_frequency[letter]) for letter in letter_frequency.keys()])
    print("Tree root:", huffman_tree.__str__())

    huffman_table = dict()
    build_huffman_table(huffman_tree, huffman_table, '')
    print("Huffman table:", huffman_table)

    encode(huffman_table)
    decode()


class Node:
    def __init__(self, char=None, frequency=0, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __cmp__(self, other):
        return self.frequency - other.frequency

    def __str__(self):
        return "%s, %s" % (self.char, self.frequency)


def build_huffman_tree(frequencies):
    nodes = [Node(char, frequency) for char, frequency in frequencies]

    while len(nodes) > 1:
        nodes.sort(reverse=True)

        left = nodes.pop()
        right = nodes.pop()

        new_node = Node(left.char + right.char, left.frequency + right.frequency)
        new_node.left = left
        new_node.right = right

        nodes.append(new_node)

    return nodes.pop()


def build_huffman_table(node, codes, code):
    if node.left is not None:
        build_huffman_table(node.left, codes, code + '0')
    if node.right is not None:
        build_huffman_table(node.right, codes, code + '1')
    if node.left is None and node.right is None:
        codes[node.char] = code


def encode(table):
    with open("input.txt", "r") as f_input:
        with open("encoded.txt", "w") as f_output:
            for keys in table.keys():
                f_output.write(str(keys) + str(table[keys]))
            f_output.write("|")

            for letter in f_input.read():
                f_output.write(table[letter])


def parse_dictionary_string(dictionary_string):
    dictionary = dict()
    value = ""
    key = ""

    for i in dictionary_string:
        if i != "1" and i != "0":
            if len(value) > 0:
                dictionary[value] = key
                value = ""
            key = i
        else:
            value += i
    dictionary[value] = key

    return dictionary


def decode():
    with open("encoded.txt", "r") as f_input:
        dictionary_string = ""

        current_char = f_input.read(1)
        while current_char != "|":
            dictionary_string += current_char
            current_char = f_input.read(1)
        dictionary = parse_dictionary_string(dictionary_string)
        print("Decoded dictionary:", dictionary)

        with open("decoded.txt", "w") as f_output:
            code = ""

            for char in f_input.read():
                if code in dictionary:
                    f_output.write(dictionary[code])
                    code = char
                else:
                    code += char
            f_output.write(dictionary[code])


main()
