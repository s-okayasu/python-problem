'''
模範解答
'''

# アルファベットを大文字と小文字のリストに格納して別リストに格納
alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpabet_list_upper = []
alpabet_list_lower = []
alpabet_list_list = []

for character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    alpabet_list_upper.append(character)
    alpabet_list_lower.append(str.lower(character))

alpabet_list_list.append(alpabet_list_upper)
alpabet_list_list.append(alpabet_list_lower)

# この方法でもできる #リストリのテラルの中でfor文を回す「リスト内包表記」という省略記法
# alpabet_list_list = [[chr(i).lower() for i in range(65, 91)], [chr(i) for i in range(65, 91)]]

# アルファベットの大文字と小文字を結合してリストへ格納
joined_character_list = []

for index in range(len(alpabet)):
    character_upper = alpabet_list_list[0][index]
    character_lower = alpabet_list_list[1][index]
    joined_character = character_upper + character_lower
    joined_character_list.append(joined_character)

# 結合した文字のリストをコンソール出力
count = 0
while count < len(joined_character_list):
    print(joined_character_list[count])
    count = count + 1
