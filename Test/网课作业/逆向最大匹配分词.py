#-*- coding:utf-8 -*-
def Reverse_matching(sent,max_len,word_dict):
    words = []
    sent = unicode(sent,'utf-8')
    end = len(sent)
    while end > 0:
        for begin in range(max(end - max_len, 0),end,1):
            if sent[begin:end] in word_dict or end == begin + 1:
                words.append(sent[begin:end])
                break
        end = begin
    return words
words = unicode(raw_input(), 'utf-8')
max_len = 1
word_dict = set()
List = []
word = words.split()
for w in word:
    word_dict.add(w)
    if len(w) > max_len:
        max_len = len(w)
for i in range(2):
    sent = raw_input()
    Words = Reverse_matching(sent,max_len,word_dict)
    Words.reverse()
    List.append(Words)
for words in List:
    for word in words:
        print word.encode('utf-8'),
    print

