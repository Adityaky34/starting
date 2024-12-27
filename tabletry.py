def gen_table(n):
    table = ''
    for i in range(1,11):
        table += f'{n} X {i} = {n*i}\n'
    with open(f'table of {n}' , 'w') as f:
        f.write(table)


for i in range(2,11):
    gen_table(i)

