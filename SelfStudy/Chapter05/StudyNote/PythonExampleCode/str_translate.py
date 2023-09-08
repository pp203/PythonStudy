msg = '今日の,あなたの運勢は,●良い感じ●です.'

# 変換前後の文字を辞書として定義
print(msg.translate(str.maketrans({
    ',': '、',
    '.': '。',
    '●': ''
})))

# 変換すべき文字群を文字列として定義
print(msg.translate(str.maketrans(',.', '、。', '●')))
