def insertionSort(nxlist):
   for index in range(1,len(nxlist)):

     currentvalue = nxlist[index]
     position = index

     while position>0 and nxlist[position-1]>currentvalue:
         nxlist[position]=nxlist[position-1]
         position = position-1

     nxlist[position]=currentvalue

nxlist = [215,326,13,227,57,2421,425,121,7022]

insertionSort(nxlist)

print(nxlist)