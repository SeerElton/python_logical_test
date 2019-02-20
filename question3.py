# imports
import string

# string of characters
characters = """kAewtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYm
vnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhR
RiUvGmYmvnJIHEmbTaWEReGHYvkAewtloYgcFQaJNhHVGxmvnJIHEmbTkAewtloYgcFQaJ
NhHVGxXDiQmzjfcpiGqhRRiUvGmYmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpYbzx
lWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYmvnJIHEmbTbCDFuWSXj
AewtloYgcFQaJNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiAewtloYgcFQaJ
NhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpimvnJIHEmbTkAewtloYgcFQaJN
hHVGxXDiQmzjfcptIUYrTGBuAewtloYgcFQaJNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGx
XDiQmzjfcpiAewtloYgcFQaJNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxtloYgcFQaJNhH
VGxXDiQmzjfcpiGqhRRiUvGmYmvnJIHEmbTkAewtlXDiQmzjfcpiiERToMKOotloYgcFQaJNh
HVGxXDiQmzjfcpiGqhRRiUvGmYmvnJIHEmbTkAewtltloYgcFQaJNhHVGxXDiQmzjfcpiGqhR
RiUvGmYmvnJIHEmbTkAewtltloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvGmYmvnJIHEmbTk
AewtloWAScWQAsNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvN
hHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvdTGXoERBfNhHVGxmv
nJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvNhHVGxmvnJIHEmbTkAewtloYgc
FQaJNhHVGxXDiQmzjfcpiGqhRRiUvNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQm
zjfcpiGqhRRiUvgTYUmVBNhNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiGq
hRRiUvhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiAewhHVGxmvnJIHEmbTk
AewtloYgcFQaJNhHVGxXDiQmzjfcpiAe"""

###
# Description - get characters surrounded by EXACTLY three big letters on each of its sides.
#
# @param characters(string) - a string of characters
#
# return(string) - the word that the surrounded letters make up.
##


def get_Characters(characters):

    new_Word = ''
    characters_list = list(characters)

    for index, chars in enumerate(characters_list):

        first_Three = characters[index:index+3]
        three_Chars = first_Three.isupper() and first_Three.isalpha()

        if(three_Chars):
            last_Four = characters[index+3:index+7]

            if(last_Four[1:].isupper() and last_Four[1:].isalpha()):
                letter = last_Four[0:-3]
                new_Word += letter

    return new_Word


# get the word surounded by capital letters
word = get_Characters(characters)

print(word)
