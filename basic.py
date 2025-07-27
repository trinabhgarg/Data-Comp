import pdb
import random
import string



def random_string(n):
    """This function generates a random string of length n"""
    s=''  # defining empty string that will contain the randomly generated string
    for i in range(n):
        s+=random.choice(string.printable)  # placing random symbol at the ith index of the string
    return s

def order_data(n):
    """This function returns a string of length n having only 2 elements A and B"""
    s=''  # pre-defining the empty string that will contain the ans
    for i in range(n//2):  # in the first half of string length
        if i%7==0:
            s+=' '
        else:
            s+='A'  # assign 'A' to all the indices
    for i in range(n//2):  # in the remaining second half of string length
        if i%7==0:
            s+=' '
        else:
            s+='B'  # assign 'B' to all the indices
    return s 

def direct_binary_dict(s):
    """This function returns the binary conversion dictionary of all the characters in s"""
    ans={} # defining the ans dict
    for i in s:
        # the built-in ord function returns the Unicode code of the character
        ans[binary(ord(i))]=i  # the binary value of Unicode of the element 'i' is mapped to the element itself
    return ans


def binary(n):
    '''This function returns a string which will store the binary form of the number'''
    a=''
    #while the number n stays greater than zero after continuously dividing by ten
    while(n>0):
        #if the number is even then 0 is added to the string
        if(n%2==0):
            n=n/2
            a=a+'0'
        #if the number is odd then 1 is added to the string
        else:
            n=n//2
            a=a+'1'
    while len(a)<8:  # when string a has less than 8 characters (8 because, ascii code has 8 characters)
        a+='0'  # place '0' at the end
    return a[::-1]  # reversing the string


def binary_make(s):
    """This function returns the binary string of the string s"""
    bin=''  # pre-defining the binary ans string
    for i in s:
        bin+=binary(ord(i))  # keep on placing the binary form the unicode of ith element
    return bin

#print(len(binary_make("Hi ")))

def direct_binary_decode(s):
    """This function takes a binary string and converts it into the text."""
    d=direct_binary_dict(s)  # calling the binary conversion dictionary, whose function has been defined above.
    #print(d)
    ans=""  # pre-defining the ans string
    for i in range(len(s)//8):
        ans+=d[s[i*8:(i+1)*8]]  # converting binary to text
    return ans

#pdb.set_trace()
#print(direct_binary_decode(binary_make('Hi ')))

def textstrip(filename):
    '''This funcion takes the file and converts it to a string with all the spaces and other special characters removed.
    What remains is only the lower case letters.'''

    #open is used to open the text file 
    f=open(filename, encoding='utf-8')

    s=f.read()  # read the file
    f.close()  # closethe file
    return s

   
def letter_distribution(s):
    '''This function creates a dictionary containing the frequency distribution of letters in a string s.'''
    #created a dictionary which will contain the lower case letters as key and its number of occurence as its value
    d={}

    #traversing through every letter in string s
    for i in s:
        if i in d:  #if the letter i is already there in the dictionary
            d[i]+=1  #then the value of it is increased by one meaning the number of occurence is increased by one
        else:  #if i is not there in dictionary
            d[i]=1  # then it is added to the dictionary and its value is set to 1 which would increase if its number of occurence is more than one
    return d


def left_right_k(L):
	"""This code takes the first element of the list and creates a left and a right list and returns left, right and the element"""
    #created empty left and right lists
	left=[]
	right=[]

    #created a variable k with value as the first element of the list 
	k=L[0]  

    #traversing through the list L
	for i in range(1,len(L)):
		if L[i]<=k:  # if ith element is less than or equal to the variable
			left.append(L[i])  # place it in the left list
		else:  # if the ith element is greatr than the variable
			right.append(L[i])  # place it in the right list
	return left,right,k


def quick_sort(L):
	"""This function sorts the given list using the quick sort method 1 for accending -1 for desending
	this element takes an element(say x) and creates 2 lists left(which contains elements less then x)
	and right (which contains elements greater then x). It puts the element (x) at its correct position and
	then sorts the left and the right halves individually and then adds all together."""

	if len(L)<=1: #if the length of the list is less than 1
		return L  # return the list as it is

	else:  #if the length of the list is greater than one
		left,right,k=left_right_k(L)  # call the left_right_k function
		L[len(left)]=k
		left,right=quick_sort(left),quick_sort(right)
		for i in range(len(left)):
			L[i]=left[i]
		for i in range(len(right)):
			L[i+len(left)+1]=right[i]
		return L
		
			
def key_value_list(d):
    """This function converts the key value pair of the dictionary to value key pair nested list"""
    ans =[] # the final list

    #traversing through the dictionary and appending elements in the list ans. The key value pair is stored as a nested list in the list 
    for i in d:
        ans.append([d[i],i])
    return ans

#print(binary(4))

def ascii(s):
    '''This function returns a dictionary that would store the elements of the string s as key and ascii value as the value to the key'''
    d={}

    #first found the ascii code of the character using ord function and then using binary functon converted the ascii code to binary form 
    for i in s:
        d[i]=binary(ord(i))
    
    return d


def substitution_encrypt(s,d):
    '''This function encrypts the contents of s using the input dictionary d which comprises of the substitutions.'''
    #print(d)
    t=""  # pre-defining the ans string
    #traversing the elements of string s
    for i in s:
        t=t+d[i]  # place the substitution in the pre-defined ans string
    return t
