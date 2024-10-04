# CLRS Book
# Maximum Subarray problem 
# Posmatramo niz koji predstavlja cene akcija na berzi tokom odredjenog perioda dana 
# Potrebno je odrediti maksimalan moguci profit za period od len(array) dana
# 
# JEDNA MOGUCNOST: Brute Force 
# - Mozemo isprobati sve kombinacije datuma dok ne dodjemo do maksimalnog profita 
# - Ovo rezultuje sa (n nad 2) kombinacija sto je Sigma(n^2) slozenost -> dakle n^2 u najboljem slucaju
# 
# BOLJE RESENJE:  
# - Posmatracemo niz cena akcija kao niz dnevnih promena cena pocevsi od nultog dana
# - U odnosu na ovaj niz, probacemo da pronadjemo maksimalan podniz - podniz koji ima najvecu sumu
# - Na prvi pogled ovo ne deluje kao bolje resenje jer bi trebalo i dalje da prodjemo kroz teta(n^2) podnizova za n dana
# - Medjutim, nad ovakvim nizom moze da se primeni podeli-pa-vladaj pristup kojim se postize ubrzanje

def findMaxCrossingSubaray(arr, low, mid, high):
    leftSum = float('-inf')
    sum = 0
    for i in range(mid, low, -1):           # Pronalazak maksimalnog podniza u levom delu 
        sum += arr[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i

    rightSum = float('-inf')
    sum = 0
    for j in range(mid+1, high):            # Pronalazak maksimalnog podniza u desnom delu
        sum += arr[j]
        if sum > rightSum: 
            rightSum = sum 
            maxRight = j
    
    return (maxLeft, maxRight, leftSum + rightSum)

def findMaximumSubarray(arr, low, high):
    if high == low: 
        return (low, high, arr[low])
    
    mid = (low + high) // 2
    leftLow, leftHigh, leftSum = findMaximumSubarray(arr, low, mid)
    rightLow, rightHigh, rightSum = findMaximumSubarray(arr, mid+1, high)
    crossLow, crossHigh, crossSum = findMaxCrossingSubaray(arr, low, mid, high)
    if leftSum >= rightSum and leftSum >= crossSum:
        return (leftLow, leftHigh, leftSum) 
    elif rightSum >= leftSum and rightSum >= crossSum:
        return (rightLow, rightHigh, rightSum)
    else: 
        return (crossLow, crossHigh, crossSum)
    
arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
result = findMaximumSubarray(arr, 0, len(arr) - 1)