#!/usr/bin/env python
# coding: utf-8

# In[38]:


import random

arq = open('Sorteio.txt', 'w')
arq.close()

arq = open('Sorteio.txt', 'a')
for d in range(1,4):
    d = random.randrange(1,50)
    arq.write('{}\n'.format(d))
arq.close()

sorte = []
dados = []
a = int(input('Digite um número:'))
dados.append(a)
b = int(input('Digite outro:'))
dados.append(b)
c = int(input('Outra vez:'))
dados.append(c)


arq = open('Sorteio.txt', 'r')
for l in arq:
    l = l.strip()
    sorte.append(l)
    print(l)
arq.read()
arq.close()

print('Números sortidos aleatoriamente: {}.'.format(sorte))
print('Os números escolhidos: {}'.format(dados))
 


# In[ ]:





# In[ ]:




