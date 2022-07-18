
# variable s is the index of numlist.rowlist for catching the sum rows of the original list.
# Then i made a variable to catch the summery row.
# i wanted to check if there are mutiple rows with the max value so i made an if statement to check if the
# unique rowlist is the same length as the original rowlist
# if yes i made a variable i that will be an index and made a while loop that checks for the index of the max sum
# of the row so i can print it without knowing where it is
# else i made an if statement that checks the index of the max sum row and prints it when finds it

# moving to columns i made a list with nested lists for each column than made a while loop that works if ri(row index)
# is <4 and c as the index of the rows and the col_list index and goes through each one and appends it to the col_list
# if the column index is => than 5 the column index resets and the row index is bigger by 1
# than i made variables that will catch the sum of column ,the max sum of colum and ci as the column index
# made an if statement  that checks for column duplicates and an if statment that finds the index of the max column

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
    if set(rowlist) not in range(len(rowlist)):
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
            print(maxsumrow)


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
    if  len(set(sumofcols))<len(sumofcols):

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





























































































pass

meterazia(numlist)


