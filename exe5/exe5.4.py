#Задание 5.4

def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''
    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding

def rle_decode(text):
    decoding = ''
    if not text: return ''
    for i in range(0,len(text),2):
        decoding += text[i+1]*int(text[i])
    return decoding

with open('text_for_RLE.txt', 'r') as file:
    text = file.readline()

print(text)

text_compression = rle_encode(text)
with open('text_compression_RLE.txt', 'w') as file:
    file.write(f'{text_compression}')

print(text_compression)

with open('text_compression_RLE.txt', 'r') as file:
    print(rle_decode(file.readline()))

