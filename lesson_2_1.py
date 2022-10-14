import csv
import re

def get_data():
    os_name_list = []
    os_code_list = []
    os_prod_list = []
    os_type_list = []
    main_data = [["Изготовитель системы", 'Название ОС',
                 'Код продукта', 'Тип системы']]
    numb = 1
    while numb < 4:
        with open(f'./info/info_{numb}.txt', 'r') as i1:
            for i in i1.readlines():
                if main_data[0][0] in i:
                    a = i.strip().split(':')
                    a[1] = a[1].strip()
                    os_prod_list.append(a[1])
                elif main_data[0][1] in i:
                    a = i.strip().split(':')
                    a[1] = a[1].strip()
                    os_name_list.append(a[1])
                elif main_data[0][2] in i:
                    a = i.strip().split(':')
                    a[1] = a[1].strip()
                    os_code_list.append(a[1])
                elif main_data[0][3] in i:
                    a = i.strip().split(':')
                    a[1] = a[1].strip()
                    os_type_list.append(a[1])
            numb +=1

    main_data.append(os_prod_list)
    main_data.append(os_name_list)
    main_data.append(os_code_list)
    main_data.append(os_type_list)
    return main_data



def write_csv(source):
    with open(source, 'w') as f:
        data = get_data()
        f_writer = csv.writer(f)
        for row in data:
            f_writer.writerow(row)

write_csv('result.csv')

with open('result.csv', 'r') as f:
    f_reader = csv.reader(f)
    for i in f_reader:
        print(i)