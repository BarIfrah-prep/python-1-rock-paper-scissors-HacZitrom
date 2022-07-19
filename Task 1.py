numlist = [[4, 1, 222, 7, 5],[4, 1, 222, 7, 5],[7, 3, 5, 1, 3],[222, 5, 4, 3, 2]]




def meterazia(numlist):
    s = 0
    rowlist = []
    maxsumrow=0
    ri = 0

    while s<4:
        rowlist.append(sum(numlist[s]))
        s+=1
    maxsumrow=max(rowlist)
    if sorted(rowlist) not in range(len(numlist)):
        i=0
        while maxsumrow!=sum(numlist[i]):
            i+=1
        else:
            print(f'the duplicate is {numlist[i]}')
    else:

        if maxsumrow != rowlist[ri]:
            ri += 1
        else:
            print(f'The index of the max row is {ri}')


    col_list=[[],[],[],[],[]]
    c=0
    while ri<4:
        if c<5:
            col_list[c].append(numlist[ri][c])
            c+=1
        elif c>=5:
            c=0
            ri+=1
    else:
        pass
    sumofcols = []
    maxsumcol=0
    ci=0

    while ci in range(len(col_list[ci])):
        if sum(col_list[ci]) not in sumofcols:
            sumofcols.append(sum(col_list[ci]))
            ci+=1
        else:
            pass
    maxcol=max(col_list)
    maxsumcol = max(sumofcols)
    i = 0
    if  len(sorted(sumofcols))<len(sumofcols):

        while maxcol not in col_list[i]:
             i += 1
        else:
            print(f'the duplicate col index is {col_list[i]}')
    else:
        print(f'The max col = {maxsumcol}')
    while i < len(col_list):
        if maxcol != col_list[i]:
            i += 1
        else:
            print(f'The max col is in index {i}')
            break
































































































pass

meterazia(numlist)


