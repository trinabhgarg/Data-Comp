import basic
import huffman
import naive_method
import random
import shannon_fano

def main_huffman(filename):
    """Takes the relative path of a text file"""

    #imported the textstrip function and applied to a text file 
    s=basic.textstrip(filename)

    #string will contain the binary from of the text file
    bin_s_standard=basic.binary_make(s)

    print("Direct file size in binary :",len(bin_s_standard),'bits')
    
    # writing binary in a text file
    f=open('binary_files\direct_genral','wb')
    for i in bin_s_standard:
        f.write(bytes(int(i)))
    f.close()

    #created a frequency dictionary of s
    freq_dict=basic.letter_distribution(s)

    #found the huffman dictionary for the frequency distribution
    huffman_dict=huffman.huffman(freq_dict)
    #print(hoffman_dict)

    #encrypted s using the huffman dictionary and storing it to a file
    bin_s_direct_huffman=basic.substitution_encrypt(s,huffman_dict)
    f=open('binary_files\huffman_genral.bin','wb')
    for i in bin_s_direct_huffman:
        f.write(bytes(int(i)))
    f.close()

    
    print("Binary file size using huffman compression :",len(bin_s_direct_huffman),' bits')
    print("Percentage Compresion using huffman encoding :",((len(bin_s_standard)-len(bin_s_direct_huffman))/len(bin_s_standard))*100)
    #print(hoffman_approch1.huffman_decode(hoffman_dict,bin_s_direct_hoffman))
    s_decode=huffman.huffman_decode(huffman_dict,bin_s_direct_huffman)
    f=open('huffman_decode.txt','w')
    f.write(s)
    f.close()

    print("Is the decoding working fine: ",s==s_decode)
    

def main_shannon_fano(filename):
    """This function takes a file as name as input and tels the percentage compresion"""
    s=basic.textstrip(filename)
    freq_dict=basic.letter_distribution(s)
    freq_list=basic.key_value_list(freq_dict)
    # gets the shannon fano encoding dict
    shannon_fano_dict=shannon_fano.shannon_fano(freq_list)

    s=basic.textstrip(filename)

    #string will contain the binary from of the text file
    bin_s_standard=basic.binary_make(s)
    # showing the original file size
    print("Direct file size in binary :",len(bin_s_standard),'bits')

    # creating a binary file based on shanon encoding dict
    bin_s_shannon=basic.substitution_encrypt(s,shannon_fano_dict)
    print("Binary file size using shannon fano compression :",len(bin_s_shannon),' bits')
    print("Percentage Compresion using shanon fanno :",((len(bin_s_standard)-len(bin_s_shannon))/len(bin_s_standard))*100)
    s_decode=huffman.huffman_decode(shannon_fano_dict,bin_s_shannon)

    # writing the encoding as a binary file
    f=open('binary_files\shannon_fano_genral.bin','wb')
    for i in bin_s_shannon:
        f.write(bytes(int(i)))
    f.close()

    print("Is the decoding working fine: ",s==s_decode)


def main_naive_approach(filename):
    """Creates the naive compression file of the text takes the filename as input"""
    s=basic.textstrip(filename)
    naive_s=naive_method.naive_approach(s)
    bin_s_standard=basic.binary_make(s)
    
    # make the binary file of naive approach
    bin_naive_s=basic.binary_make(naive_s)

    # adding the content to a file

    print("Direct file size in binary :",len(bin_s_standard),'bits')
    print('No.of bits after applying navie approch:',len(bin_naive_s),'bits')
    print('percentage compresion is :', ((len(bin_s_standard)-len(bin_naive_s))/len(bin_s_standard))*100)
    
    # writting the binary file
    f=open('binary_files\_naive_genral.bin','wb')
    for i in bin_naive_s:
        f.write(bytes(int(i)))
    f.close()

print()
print('Result for random text file')
main_huffman('_random.txt')
print()
main_shannon_fano('_random.txt')
print()
main_naive_approach('_random.txt')
print()
print()
print('Result for order text file')
main_huffman('ordered.txt')
print()
main_shannon_fano('ordered.txt')
print()
main_naive_approach('ordered.txt')
print()
print()
print('Result for sherlock holmes')
main_huffman('The Adventures of Sherlock Holmes.txt')
print()
main_shannon_fano('The Adventures of Sherlock Holmes.txt')
print()
main_naive_approach('The Adventures of Sherlock Holmes.txt')