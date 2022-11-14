def alphabet_position(text):
    alphabet= 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    return ' '.join([str(alphabet.find(i) + 1) for i in text if i in alphabet])
