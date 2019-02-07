# RR-Verkefni3  

**1. hanoi...**  
Mynd fylgir hér að ofan.

**2. Hver er flækjutími fallsins hanoi(n, A, B, C)? Rökstyddu.**  
Flækjutími fallsins er O(2^n) þar sem þú þarft nákvæmlega 2^n - 1 aðgerðir til að klára þrautina óháð diskafjölda.  

**3. Útskýrðu stuttlega tímaflækjurnar hér fyrir neðan og nefndu dæmi um reiknirit sem hafa flækjurnar.**  
  **a) O(n)**  
  Framkvæmir einfalda leit, ef n = 10 tekur forritið 10 tímaeiningar að klára.  
  Dæmi: MergeSort  
  **b) O(n²)**  
  Ef n = 10 tekur forritið 100 tímaeiningar að klára þar sem 10 * 10 = 100.  
  Dæmi: Selection Sort  
  **c) O(log(n))**  
  Þýðir að reikniritið tekur í versta falli log(n) tíma að klára. Þ.e.a.s. Ef n er 100 tekur það 2 tímaeiningar þar sem log(100) er 2.  
  Dæmi: QuickSort  
  
**4.**  
```python
def allarMogulegarEinn(stafir, n):

    k = len(stafir)
    allarMogulegarTveir(stafir, "", k, n)

def allarMogulegarTveir(stafir, tmp, k, n):

    if n == 0:
        print(tmp)
        return

    for x in range(k):
        if len(tmp) > 0:
            if stafir[x] in tmp:
                #print("sama: " + tmp + " nýtt verður: " + tmp+stafir[x])
                continue
            #else:
                #print("ekki sama: " + tmp + " nýtt verður: " + tmp+stafir[x])
        newTmp = tmp + stafir[x]
        allarMogulegarTveir(stafir, newTmp, k, n-1)


stafir = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
n = int(input("Hvað á strengurinn að vera langur? "))
allarMogulegarEinn(stafir, n)
```  
**a) Hversu margir möguleikar fyrir strengi af lengd n?**  
**b) Flækjutími fallsins**  

**5.**  
```python

```  

