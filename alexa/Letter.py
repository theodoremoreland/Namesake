class Letter():
    """ An object for assigning positions to letters on a 5x5 grid.
    """
    def __init__(self, positions, val):
        self.positions = positions
        self.val = val

    def onLetter(self, pos):

        if pos in self.positions:
            return True
        else:
            return False

# Each letter and its respective coordinates
a = Letter([3,4,7,10,12,13,14,15,17,20,22,25], "a")
b = Letter([2,3,4,7,10,12,13,14,17,20,22,23,24], "b")
c = Letter([3,4,5,7,12,17,23,24,25], "c")
d = Letter([2,3,4,7,10,12,15,17,20,22,23,24], "d")
e = Letter([2,3,4,5,7,12,13,14,17,22,23,24,25], "e")
f = Letter([2,3,4,5,7,12,13,14,17,22], "f")
g = Letter([3,4,5,7,12,14,15,17,20,23,24,25], "g")
h = Letter([2,5,7,10,12,13,14,15,17,20,22,25], "h")
i = Letter([3,8,13,18,23], "i")
j = Letter([5,10,15,17,20,23,24], "j")
k = Letter([2,5,7,9,10,12,13,17,19,22,25], "k")
l = Letter([2,7,12,17,22,23,24], "l")
m = Letter([1,5,6,7,9,10,11,13,15,16,20,21,25], "m")
n = Letter([2,5,7,8,10,12,14,15,17,20,22,25], "n")
o = Letter([3,4,7,10,12,15,17,20,23,24], "o")
p = Letter([2,3,4,7,10,12,13,14,17,22], "p")
q = Letter([3,4,7,10,12,15,17,19,20,23,24,25], "q")
r = Letter([2,3,4,7,10,12,13,14,17,19,22,25], "r")
s = Letter([3,4,5,7,13,14,20,22,23,24], "s")
t = Letter([2,3,4,8,13,18,23], "t")
u = Letter([2,5,7,10,12,15,17,20,22,23,24,25], "u")
v = Letter([2,4,7,9,12,14,17,19,23], "v")
w = Letter([1,5,6,10,11,15,16,18,20,22,24], "w")
x = Letter([2,4,7,9,13,17,19,22,24], "x")
y = Letter([3,5,8,10,13,14,15,19,24], "y") # TODO Correct coordinates for "y"
z = Letter([2,3,4,5,10,14,18,22,23,24,25], "z")

# This List can be used to confirm coordinates for each letter
letters = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]