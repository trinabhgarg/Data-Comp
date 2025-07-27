
import basic
import pdb

def mini(l):
    """This function returns two lists which are formed by splitting the input list such that the difference between the sum of elements
    of the two lists is least."""
    a=0 # pointer from start 
    b=len(l)-1 # pointer from end
    sum_start=0 # to calculate the sum from start
    sum_last=0 # to calculate the sum from back
    # while the pointer from end is greater than the pointer from start 
    # and the loop ends when they become equal
    while(b>a-1):
        if sum_start>sum_last:
            sum_last+=l[b][0]
            b=b-1
        else:
            sum_start+=l[a][0]
            a=a+1
    return l[:a],l[b+1:]

#print(mini([[45,'f'],[16,'e'],[13,'d'],[12,'c'],[5,'b'],[4,'a']]))
#print(mini([[50,'a'],[50,'b']]))

def shannon_fano(freq_alpha):
    """This function returns the shannon_fano dictionary mapping on each character based on the value key list based
    on the frequency distribution of each character"""
    #pdb.set_trace()
    #freq_alpha=basic.key_value_list(d)
    freq_alpha=basic.quick_sort(freq_alpha) # sorts the value_key list
    freq_alpha=freq_alpha[::-1] # arranges it in decending order
    if len(freq_alpha)==2:
        # if there are only 2 elements in the freq_alpha
        ans={}  # pre-defining the ans dictionary
        ans[freq_alpha[0][1]]='0'  # assigning 0 to the left list
        ans[freq_alpha[1][1]]='1'  # assigning 1 to the right list
        return ans
    else:
        ans={}
        left,right=mini(freq_alpha)  # applying mini function on freq_alpha
        # now we apply shannon_fanno algorithm to left and right part if length of left or rigth is greater then 1
        if len(left)==1:
            ans[left[0][1]]='0'
        else:
            # shannon fano algorithm applied recursively
            left_dict=shannon_fano(left)
            #print(left_dict)
            # adding the recursion ans to the current ans
            for i in left_dict:
                if i in ans:
                    ans[i]+='0'
                    ans[i]+=left_dict[i]
                else:
                    ans[i]='0'  # first add '0' to the dictionary value at i
                    ans[i]+=left_dict[i]  # concatenate with the left_dict value at i

        if len(right)==1:
            ans[right[0][1]]='1'
        else:
            # shannon fano algorithm applied recursively
            right_dict=shannon_fano(right)
            # adding the recusrion ans to the current ans
            for i in right_dict:
                if i in ans:
                    ans[i]+='1'  # first add '1' to the dictionary value at i
                    ans[i]+=right_dict[i]  # concatenate with the right_dict value at i
                else:
                    ans[i]='1'
                    ans[i]+=right_dict[i]
        
        return ans

