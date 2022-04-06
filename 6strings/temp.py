while True:
    line=input('>')
    if  len(line)==0 or line[0]=='#':
        continue
    if line=='done':
        break
    print(line)

print('Done!')
