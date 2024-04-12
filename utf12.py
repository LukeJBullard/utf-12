def encode(unicode_characters):
    return bytes((len(unicode_characters) if unicode_characters else 1))

def decode(slabs):
    return ""
