# imports
import string
import sys

# keys
keys = [['K', 'O', 'E'], ['M', 'Q', 'G']]

# lowercase letters
letters = string.ascii_lowercase

# sentance
sentence = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq
glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb."""

###
# Description - this function receives the keys and return the diffirence between them.
#
# @params keys(array) - a multidimensional array of keys.
#
# return(int) - the diffirence between the characters.
##


def get_Key_Diffirence(keys):

    difference = -1
    last_difirence = -1
    left_Keys_Indexes = list()

    for leftKeys in keys[0]:

        index = letters.index(string.lower(leftKeys))
        left_Keys_Indexes.append(index)

    for i, rightKeys in enumerate(keys[1]):

        index = letters.index(string.lower(rightKeys))
        difference = index - left_Keys_Indexes[i]

        if(difference == last_difirence or last_difirence == -1):
            last_difirence = difference

        else:
            print('characters indexes are not parralel')
            sys.exit()
    return difference


###
# Description - this function translate the string using the diffirence between characters.
#
# @params letters(string) -  letters from a - z.
# @params sentance(string) -  the string to translate.
# @params keys(int) - the diffirence between the characters.
#
# return(string) - a translated character.
##


def translate(letters, sentence, diffirence):

    letters_list = list(letters)
    transalate_string = ''

    for char in letters_list:

        if((letters.index(char) + diffirence) < len(letters)):
            transalate_string += letters[letters.index(char) + diffirence]

        else:
            transalate_string += letters[letters.index(
                char) + diffirence - len(letters)]

    translate_to = string.maketrans(letters, transalate_string)
    return sentence.translate(translate_to)


# get the diffirence.
diffirence = getKeyDiffirence(keys)

# translate the string
answer = translate(letters, sentence, diffirence)

print(answer)
