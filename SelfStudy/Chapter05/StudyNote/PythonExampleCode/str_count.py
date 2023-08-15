msg = 'にわにはにわにわとりがいる'

print(msg.count('にわ'))
print(msg.count('にわ', 3))
print(msg.count('にわ', 3, 6))

msg = 'いちいちいちばにいち'
print(msg.count('いちいち'))  # count メソッドは寿福のない出現数をカウントするので、出現数は 1 回