def getCypher(key,indicator):
  swapairs = {} 
  if indicator == 'd':
    key = key[::-1]
    split = [key[i:i+2] for i in range(0, len(key), 2)]
    for charPair in split: 
      swapairs[charPair] = {charPair[0]:charPair[1], charPair[1]:charPair[0]}
  else:
    #print('e')
    
    split = [key[i:i+2] for i in range(0, len(key), 2)]
    for charPair in split: 
      swapairs[charPair] = {charPair[0]:charPair[1], charPair[1]:charPair[0]}
  
  #print(swapairs) 
  return swapairs 


def decode_encode(key, filename, indicator):
    swaPairs = getCypher(key, indicator)  
    x = open(filename).read()
    Split = list(x) 
    #print(x)
    
    for charPair in swaPairs:
      for n, char in enumerate(Split):
        if char.upper() in charPair:
          if char.isupper():
            Split[n] = swaPairs[charPair][char.upper()]
          else:
             Split[n] = swaPairs[charPair][char.upper()].lower()
    
        
    return "".join(Split)   

def task1(key, filename, indicator): 
    string = decode_encode(key, filename, indicator)
    return string
  
if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task1 function
    print(task1('AE', 'spain.txt', 'd'))
    print(task1('VFSC', 'ai.txt', 'd'))
    print(task1('ABBC', 'cabs_plain.txt', 'e'))
    print(task1('ABBC', 'myTest.txt', 'd'))  