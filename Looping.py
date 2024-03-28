#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Mencetk angka 1 -10
for i in range(1,11):
    print(i, end=" ")


# In[6]:


#Mencetak angka 10 20 30 --- 100
for i in range(1,11):
    print(i * 10, end=" ")


# In[7]:


#Mencetak angka 10 20 30 --- 100
for i in range(10,101,10):
    print(i, end=" ")


# In[8]:


#Mencetak angka 10 9 8 7 ...
for i in range(1,11):
    print(11 - i, end = " ")


# In[11]:


#Mencetak angka 10 9 8 7 ...
for i in range(10,0,-1):
    print(i, end=" ")


# In[20]:


#Mencetak angka 1 -2 3 -4 5 -6....10
sign = 1
for i in range (1,11):
    sign = sign * -1
    print(i*sign, end = " ")
    


# In[35]:


#Mencari bilangan faktorial
#Input = 3, output = 3 * 2 * 1 = 6
#Input = 4, Outpurt = 4 * 3 * 2 * 1 = 24

bil = int(input('Isikan Bilangan :'))

hasil = 1
label = ""

for i in range(1, bil+1):
    hasil = hasil * i
    if i < bil:
        label = label + str((bil+1) - i) + "*"
    else:
        label = label + str((bil+1) - i)
    
print(f"{bil}! adalah {hasil}")
print(f"{label} = {hasil}")


# In[44]:


#Menghitung Bilangan pangkat

bil = int(input('Isikan BIlangan :'))
pangkat = int(input('Isikan Pangkat :'))
hasil = 1

for i in range(1, pangkat+1):
    hasil *= bil
    
print(f"{bil}! pangkat {pangkat} adalah {hasil}")


# In[56]:


#Mengecek Bilangan prima atau bukan
#Bilanga prima dlah bilangan yang  hanya habis di bagi dengan 1 dan bilangan itu sendiri => 2 faktor

bil = int(input("Isiaka Bilangan :"))
jumlah = 0
for i in range(1, bil + 1):
    sisa = bil % i
    if sisa == 0:
        jumlah = jumlah + 1
if jumlah == 2:
        print(f"{bil} adalah bilanan prima")
else:
        print(f"{bil} adalah bukan bilangn prima")
        


# In[ ]:





# In[104]:


#Break

for i in range(1, 100):
    print(i, end = " ")
    if i==5:
        break
print()

for j in range(1,10):
    print(j, end = " ")
    if j == 5 :
        continue


# In[101]:


#Looping untuk string menghitung huruf vokal 

kalimat = input("Isikan Kalimat :")

vokal_a = 0
vokal_i = 0
vokal_u = 0
vokal_e = 0
vokal_o = 0

for i in kalimat:
    if i=='a':
        vokal_a += 1
    elif i=='i':
        vokal_i +=1
    elif i=='u':
        vokal_u +=1
    elif i=='e':
        vokal_e +=1
    elif i=='o':
        vokal_o +=1
        
print(f"jumlah huruf a : {vokal_a}\njumlah huruf i : {vokal_i}\njumlah huruf u : {vokal_e}\njumlah huruf e : {vokal_e}\njumlah huruf o : {vokal_e}")

        


# In[100]:


#Kalimat palindrom

kalimat = input("Isikan Kalima :")
panjang = len(kalimat)
keterangan = "Dia adalah palindrom"

for i in range(0, panjang):
    kika = kalimat [i]
    kaki = kalimat [panjang - i-1]

    if kika != kaki:
        keterangan = "Bukan Palindrom"
        break
        
print(f"{keterangan}")
    

