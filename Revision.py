def moyenne(notes):
    return sum(notes)/len(notes)
def maxi(notes):
    return max(notes)
def mini(notes):
    return min(notes)
notes=[2,7,19,130,44]
print("Moyenne:",moyenne(notes))
print("note max:",maxi(notes))
print("note min:",mini(notes))
def mediane(notes):
    tri=sorted(notes)
    n=len(tri)
    return tri[n//2]
print("mediane = ",mediane(notes))