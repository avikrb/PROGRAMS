#!/usr/local/bin/python3

######BY: AVIK RANJAN BHATTARAI
import gc
key_10bits = str(input("Enter 10-bit key: "))
plain_text = str(input("Enter 8-bit plain text: "))

key10 = []
split_digits = []
left_half = []
right_half = []
left_half_shift1 = []
right_half_shift1 = []
l = []
combine = []
key1 = []
key2 = []
P8_result = []

def split_into_digits(k):
    split_digits = []
    for each_digit in k:
        split_digits.append(each_digit)
    return split_digits

def IP_key(L):
    IP_result=[]
    IP_result = [L[2],L[4],L[1],L[6],L[3],L[9],L[0],L[8],L[7],L[5]]
    return IP_result

def IP_inverse(L):
    IP_inverse_result =[]
    IP_inverse_result = [L[3],L[0],L[2],L[4],L[6],L[1],L[7],L[5]]
    return IP_inverse_result

def split_half_left(L,a,b):
    left_half = []
    for value1 in range (int(a),int(b)):
        left_half.append(L[value1])
    return left_half

def split_half_right(R,a,b):
    right_half=[]
    for value2 in range (a,b):
        right_half.append(R[value2])
    return right_half

def shift(l, n):
    return l[n:] + l[:n]

def merge_halves(L,R):
    combine=[]
    for value3 in L:
        combine.append(value3)

    for value4 in R:
        combine.append(value4)
    return combine

def P8(P):
    P8_result=[]
    P8_result = [P[5],P[2],P[6],P[3],P[7],P[4],P[9],P[8]]
    return P8_result

def get_key(A,B):
    key10 = []
    IPforKey=[]
    left_half_key=[]
    right_half_key=[]
    left_half_shift1=[]
    right_half_shift1=[]
    key_combined=[]
    key=[]
    key10 = split_into_digits(A)
    IPforKey = IP_key(key10)
    left_half_key = split_half_left(IPforKey,0,5)
    right_half_key = split_half_right(IPforKey,5,10)
    left_half_shift1 = shift(left_half_key,B)
    right_half_shift1 = shift(right_half_key,B)
    key_combined = merge_halves(left_half_shift1, right_half_shift1)
    key = P8(key_combined)
    gc.collect()
    return key

key1 = get_key(key_10bits,1)
key2 = get_key(key_10bits,3)

def IP_text(P):
    IP = []
    IP= [P[1],P[5],P[2],P[0],P[3],P[7],P[4],P[6]]
    return IP

def expansion_permutation(text):
    EP_result = []
    EP_result = [text[3],text[0],text[1],text[2],text[1],text[2],text[3],text[0]]
    return EP_result

def XOR(T,K,num):
    XORresult = []
    for i in range (0,num):
        XORresult.append(str((int(T[i]) ^ int(K[i]))))
    return XORresult

def sbox_function(a,sbox):
    b = str(a[0])+str(a[3])
    c = str(a[1])+str(a[2])
    
    
    if (b == "00"):
        list1 = sbox[0].split(",")
        if c == "00":
            value = list1[0]
        elif c == "01":
            value = list1[1]
        elif c == "10":
            value = list1[2]
        elif c == "11":
            value = list1[3]
        
    elif b == "01":
        list1 = sbox[1].split(",")
        if c == "00":
            value = list1[0]
        elif c == "01":
            value = list1[1]
        elif c == "10":
            value = list1[2]
        elif c == "11":
            value = list1[3]
        
    elif b == "10":
        list1 = sbox[2].split(",")
        if c == "00":
            value = list1[0]
        elif c == "01":
            value = list1[1]
        elif c == "10":
            value = list1[2]
        elif c == "11":
            value = list1[3]
        
    elif b == "11":
        list1 = sbox[3].split(",")
        if c == "00":
            value = list1[0]
        elif c == "01":
            value = list1[1]
        elif c == "10":
            value = list1[2]
        elif c == "11":
            value = list1[3]
        
    ret = bin (int(value))[2:]
    if ret == "0":
        return "00"
    elif ret == "1":
        return "01"
    else:
        return ret

def permutation4(list2):
    list3 = [list2[1],list2[3],list2[2],list2[0]]
    return list3

def swap(m,n,o,p):
    split_left =  split_half_left(m,n,o)
    split_right = split_half_right(m,o,p)
    return (split_right+split_left)

def round (text, slist0, slist1, count):
    plain_text_split = split_into_digits(text)
    if count == 1:
        IPfortext = IP_text(plain_text_split)
        key = key1
    elif count == 2:
        IPfortext = plain_text_split
        key = key2
    elif count == 3:
        key = key2
        IPfortext = IP_text(plain_text_split)
    elif count ==4:
        key = key1
        IPfortext = plain_text_split
    text_lefthalf = split_half_left(IPfortext,0,4)
    text_righthalf = split_half_right(IPfortext,4,8)
    EP = expansion_permutation(text_righthalf)
    EP_XOR_key = XOR(EP, key, 8)
    EP_XOR_key_left_half = split_half_left(EP_XOR_key,0,4)
    EP_XOR_key_right_half = split_half_right(EP_XOR_key,4,8)
    S_0 = EP_XOR_key_left_half
    S_1 = EP_XOR_key_right_half
    sbox0_result = sbox_function(S_0,slist0)
    sbox1_result = sbox_function(S_1,slist1)
    merge_sboxes = split_into_digits(str(sbox0_result) + str(sbox1_result))
    P4 = permutation4 (merge_sboxes)
    P4_XOR = XOR(P4,text_lefthalf,4)
    if count == 2 or count == 4:
        return (P4_XOR+text_righthalf)
    elif count ==1 or count == 3:
        result = swap(P4_XOR+text_righthalf,0,4,8)
        return (result)

sbox0_list =['1,0,3,2','3,2,1,0','0,2,1,3','3,1,3,2']
sbox1_list = ['0,1,2,3','2,0,1,3','3,0,1,0','2,1,0,3']
sbox0_modified = ['3,1,3,2','3,2,1,0','0,2,1,3','1,0,3,2']
round1_result_after_swapping = round(plain_text, sbox0_list, sbox1_list,1)                
print ("a) Intermediate result after SW operation while encrypting",' '.join (round1_result_after_swapping))   
round2_result = round (round1_result_after_swapping,sbox0_list, sbox1_list,2)
CIPHERTEXT = IP_inverse(round2_result)
print ("b) Final CipherText = ",' '.join(CIPHERTEXT))
decrypt_round1_result_after_swapping = round (CIPHERTEXT,sbox0_list,sbox1_list,3)
#for question (c) we use the modified sbox instead of sbox0
plain_text_recover = round (decrypt_round1_result_after_swapping,sbox0_list,sbox1_list,4)
print ("c) Intermediate result after SW operation while decrypting ", ' '.join(plain_text_recover))
final_plain_text = IP_inverse (plain_text_recover)
print ("d) plain_text=",' '.join(final_plain_text))
