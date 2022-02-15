
import csv
import pandas as pd

def Partitions(arr,temp):
    keep = []
    if (len(arr) != 1):

        for i in range(len(arr)):
            keep.append(arr[i])
        flag = 0
        for u in keep:
            if (u%2 == 1):
                flag = 1
            elif(u%2==0):
                flag = 0
                return

        for t in range(len(keep)):
            if(flag == 1):
                print(keep[t], end = " ")
                temp.append(keep[t])
    temp.append(-1)
    print()

def integerPartitions(arr, i, n, pc,temp,control_param = 1):

    if (n == 0):
        Partitions(arr,temp)

    for j in range(i, n + 1):

        arr.append(j)
        pc = pc + 1
        integerPartitions(arr, j, n - j,pc,temp,control_param)

        del arr[-1]
    return pc


def integerPartitions_dataset(lh_list,numb,control = 1):

    input_combinatorial = []
    output_combinatorial = []
    c = 0
    while(c < len(lh_list)):
        while(c < len(lh_list) and lh_list[c] != -1):
            input_combinatorial.append(lh_list[c])
            c = c + 1

        c = c + 1

        while(c < len(lh_list) and lh_list[c] != -1):
            output_combinatorial.append(lh_list[c])
            c = c+1
        c = c + 1

        if(len(input_combinatorial) != 0 and len(output_combinatorial) != 0):
            with open('new_dataset.csv', 'a', newline='') as fp:
                a = csv.writer(fp, delimiter=',')
                data = [[input_combinatorial,output_combinatorial]]
                if(control == 0):
                    a.writerows(data)
                a.writerows(data)
            df = pd.read_csv("new_dataset.csv")
            df.to_csv('ds.csv',header=['Set1','Set2'],index= False, quoting = csv.QUOTE_NONE,escapechar = ' ')
            # awk '{$1=$1; gsub(/\|/,",")}1' OFS= ds.csv > dataset.csv  via terminal after the operation.
            print("input_combinatorial", input_combinatorial)
            print("output_combinatorial", output_combinatorial)
        input_combinatorial.clear()
        output_combinatorial.clear()
        control  = control + 1

if __name__ == '__main__':
    param_count = 0
    temp_list = []
    arr = []

    integerPartitions_dataset(temp_list,integerPartitions(arr, 1, 3,param_count,temp_list,0),0)
    for t in range(4,50):
        temp_list.clear()
        integerPartitions_dataset(temp_list,integerPartitions(arr, 1,t,param_count,temp_list))
