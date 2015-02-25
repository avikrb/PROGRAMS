#!/usr/local/bin/python3

##AVIK RANJAN BHATTARAI
import math
import time

#e = 7
#n = 15
#C = 3
e = int(input("Enter value for 'e' = "))
n = int(input("Enter value for 'n' = "))
C = int(input("Enter value for 'C' = "))
current_time1 = time.time() #getting current time

M = 0
i = 0
result_dict = {}
def factors(n):
    for i in range(0,n):
        for j in range(0,n):
            multiply = i * j
            #print (multiply)
            if multiply == n:
                result_dict.setdefault(i,[]).append(j)
    for key1,value1 in result_dict.items():
        for key2,value2 in result_dict.items():
            #print (key2,value2[0])
            if (int(key1) + int(value1[0])) < (int(key2) + int(value2[0])):
                p = key2
                q = value2[0]
            elif (int(key1) + int(value1[0])) == (int(key2) + int(value2[0])):
                p = key2
                q = value2[0]
    #print (p,q)
    pq_list = [p,q]
    return pq_list



def phi_function(list_pq):
    p = list_pq[0]
    q = list_pq[1]
    phi_result = (p-1)*(q-1)
    return phi_result

def modulo_function(e,phi):
    d = 0
    while True:
        result = (e*d)%phi
        if result == 1:
            return d
        d = d+1

def find_message(C,d,n):
    message = (C**d)%n
    return message
    

while True:
    
    factor_list = factors(n)
    print ("p = ", factor_list[0], "\nq = ",factor_list[1])
    phi = phi_function (factor_list)
    #print (phi)
    secret_key = modulo_function(e, phi)
    print ("The secret key (d) = ", secret_key)
    M = find_message(C,secret_key,n)
    print ("The plain text (M) = ", M)
    break

current_time2 = time.time()
time_for_attack = current_time2 - current_time1
print ("The attack took: ", time_for_attack, "Seconds")
