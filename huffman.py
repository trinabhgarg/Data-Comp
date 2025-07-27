import pdb
import basic

def huffman(d):
    """This function takes a dictionary and returns the binary of its components
    via hoffman coding algorithm"""

    #converted the dictionary to a list using key_value_list function
    freq_alpha=basic.key_value_list(d)

    #the final dictionary 
    ans={}
    #pointer 
    i=0
  
    #while the len of the list freq_alpha is greater than one the loop works 

    #print(freq_alpha)
    if len(freq_alpha)==1:
        return {freq_alpha[0][1]:'0'}

    while len(freq_alpha)>1:
        #sorted the list using quick_sort
        freq_alpha=basic.quick_sort(freq_alpha)

        # to add the new list to freq aplha
        l=[freq_alpha[0][0]+freq_alpha[1][0]] 

        # now adding all the elements in the ans dictionary 
        #traversing through the 1st nested list of list freq_alpha
        for i in range(1,len(freq_alpha[0])):
            #if the element is in the dictionary then add 0 to the value string of it
            if freq_alpha[0][i] in ans:
                ans[freq_alpha[0][i]]+='0'
            
            #if the element not found then create a new key value pair and '0' as the value to it
            else:
                ans[freq_alpha[0][i]]='0'

            #append the letters of which the dictionary is made to the list l
            l.append(freq_alpha[0][i])

        #traversing through the 2nd nested list of the list freq_alpha
        for i in range(1,len(freq_alpha[1])):
            #if the element is in the dictionary then add 1 to the value string of it
            if freq_alpha[1][i] in ans:
                ans[freq_alpha[1][i]]+='1'

            #if the element not found then create a new key value pair and '1' as the value to it
            else:
                ans[freq_alpha[1][i]]='1'
            
            #append the letters of which the dictionary is made to the list l
            l.append(freq_alpha[1][i])
        
        # removing the previous cases
        freq_alpha.pop(0)
        freq_alpha.pop(0)

        #appending the list l to freq_alpha list 
        freq_alpha.append(l)
    
    # now reversing the strings to get the binary code for the respective characters
    for i in ans:
        ans[i]=ans[i][::-1]
    return ans

#pdb.set_trace()
#print(hoffman({'a':5,'b':9,'c':12,'d':13,'e':16,'f':45,' ':60}))

def huffman_decode(d,s):
    """This decode the file that is created by hoffman encoding"""
    #the string that will store the final decoded string
    ans=''
    
    #list of values and keys of the dictionary d
    binary_code=list(d.values())
    keys=list(d.keys())

    #pointer to the place from which the encoded string has to be decoded
    k=0
    for i in range(len(s)+1):
        #if the string s from k to i index is found in binary_code list
        if s[k:i] in binary_code:
            #appending it's key in ans
            ans+=keys[binary_code.index(s[k:i])]
            #setting the pointer for next loop
            k=i
    return ans