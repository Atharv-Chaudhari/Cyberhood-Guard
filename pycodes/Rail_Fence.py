def Rail_Fence_encrypt(text="Hello",rails=3):
    l=len(text)
    mat=[["-" for i in range(l)] for j in range(rails)]
    i,j=0,0
    c=False
    for k in text:
        if(i==0 or i==rails-1):
            c=not c
        mat[i][j]=k
        j=j+1
        if(c):
            i=i+1
        else:
            i=i-1
    ans=""
    for i in mat:
        ans=ans+"".join(i)
    ans=ans.replace("-","")
    return ans

def Rail_Fence_decrypt(cipher, key=3):
    rail = [['\n' for i in range(len(cipher))]
                  for j in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '-'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '-') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        if (rail[row][col] != '-'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    ans="".join(result)
    return ans