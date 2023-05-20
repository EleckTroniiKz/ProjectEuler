#WIP
def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n+1

chain = 1
maxChain = 0
current = 13
startNum = 13
largest = 0

while current < 1000000:
    while current != 1:
        current = collatz(current)
        chain += 1
    maxChain = max(maxChain, chain)
    if maxChain == 131434183:
        print(startNum)
    startNum += 1
    current = startNum
    

print(maxChain)