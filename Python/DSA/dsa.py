#!/usr/local/bin/python3

import math

'''p = 47
q = 23
h = 5
x = 7
k = 16
H_M1 = 5
H_M2 = 6
'''

'''p = 7
q = 3
h = 3
x = 2
k = 1
H_M1 = 3
H_M2 = 4
'''

p = 23
q = 11
h = 3
x = 7
k = 7
H_M1 = 9
H_M2 = 4


def compute_g(h,p,q):
    value1 = (h**(int((p-1)/q)))%p
    return value1


def compute_y(g,x,p):
    value2 = (g**x)%p
    return value2

def compute_r(g, k, p,q):
    value3 = ((g**k)%p)%q
    return value3


def compute_mod_inverse(a,c):
    b = 0
    while True:
        X = a * b
        Y = X % c
        if Y == 1:
            return b
            break
        else:
            b = b+1
            
def compute_s(k, H_M,x,r,q):
    k_value = compute_mod_inverse(k,q)
    print ("Mod inverse of K=", k_value)
    k_inverse = k_value %q
    value4 = (k_value*(H_M+(x*r)))% q
    return value4

def compute_w (s,q):
    value5 = compute_mod_inverse(s,q)
    return (value5%q)

def compute_u1_u2 (H_M,r,w,q):
    value1 = (H_M * w) % q
    value2 = (r*w) % q
    value6 = [value1, value2]
    return value6

def compute_v(g, y, u, p,q):
    u1 = u[0]
    u2 = u[1]
    value7 = ((g**u1)*(y**u2) % p ) % q
    return value7

g = compute_g(h, p, q)
print ("G = ",g)

y = compute_y(g,x,p)
print ("Y = ",y)

r = compute_r (g, k, p, q)
print ("R = ",r)

s = compute_s(k, H_M1,x, r,q)
print ("S = ",s)

##VERIFICATION
w = compute_w(s,q)
print ("W = ",w)

u1_u2 = compute_u1_u2 (H_M2,r, w, q) #change H_M1 to H_M2 depending on what you want to verify
print ("U1 = ", u1_u2[0], "U2 = ", u1_u2[1])

v = compute_v (g, y, u1_u2, p, q)
print ("v = ", v)

if v == r:
    print ("Signature verified")
else:
    print ("****Signature not verified")


