import MeCab 
from matplotlib import pyplot as plt
from wordcloud import WordCloud


# テキストファイル読み込み
with open('./coordinate_info_M.txt', mode='rt', encoding='utf-8') as fi:
    source_text = fi.read()

# MeCabの準備
tagger = MeCab.Tagger()
tagger.parse('')
node = tagger.parseToNode(source_text)

# 名詞を取り出す
word_list = []
while node:
    word_type = node.feature.split(',')[0]
    if word_type == '形容詞':
        word_list.append(node.surface)
    node = node.next

# リストを文字列に変換
word_chain = ' '.join(word_list)


#stop words 設定
stop_words_N = ['今日','yukichi','の','ん','instagram','yukkey','follow me',
'お気に入り','私','好き','please follow','please','follow','もの','インスタ',
'follow me','follow','me','これ','最近','もの','yuki','笑','コーデ','更新',
'更新中','こと','大好き','今年','ZOZOTOWN','本日','本日ZOZOTOWN','takahashi','_iiio',
'今回','wear','hinechi','iii','昨日','フォロー','仕事','お願い','依頼','仕事依頼',
'プロフィール','プロフィール欄','欄','我的','S','DM','連絡','毎日','投稿','毎日投稿','僕','コメント',
'gmail','com','line','Store','M','オススメ','感じ','ポイント','方','我','的','気軽',
'声','よう','時','http','www','的','人','是非','チェック','そう','問い合わせ','あと','営業','時間',
'是非']

stop_words_Adj = ['可愛い','かわいい','カワイイ','可愛','可愛く','嬉しい','いい','欲しい','欲しく','良い','っぽく','ぽく','良かった','良かっ',
'ない','よかった','よかっ','良','すごく','凄く','凄い','すごい','っぽい','ぽい','よろしいけれ','詳しく','詳しい'
,'よろしく','よろしけれ','良けれ','良く','欲しい','早く','無く','ない','よく','寂しい','宜しく']

# ワードクラウド作成
W = WordCloud(width=640, height=480, background_color='white', colormap='bone', font_path='./yumin.ttf',stopwords=set(stop_words_Adj)).generate(word_chain)
# stopwords=set(stop_words_Adj)
plt.imshow(W)
plt.axis('off')
plt.show()

