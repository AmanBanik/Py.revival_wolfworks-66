Trans_H_E={
    'Madad':'Help',
    'Billi':'Cat',
    'Purush':'Man',
    'Shanni':'Saturn',
    'Pashu':'Animal'
}
i = 0
while i < 5: # while loop keeps on asking just for sake i know already😎
    r = input("The hindi word?:")
    print(f'{r} translated in Hindi is {Trans_H_E[r]}')# indexing
