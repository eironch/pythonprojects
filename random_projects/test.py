a = "{"
b = "}"

for x in range(11):
    for y in range(11):
        print(f'if enemyHealthX{x + 7}Y{y + 2} != 0 then')
        print(f'label "{a}1, : enemyHealthX{x + 7}Y{y + 2}{b}" at {x + 7},{y + 2}')
        print(f'end')