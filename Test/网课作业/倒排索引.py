def create_index():
    Dict = {}
    for i in range(100):
        sent = raw_input()
        sent = sent.lower()
        words = sent.strip().split()
        for word in words:
            if word in Dict:
                Dict[word].add(i+1)
            else:
                Dict[word] = {i+1}
    return Dict
def print_index(Dict):
    answer_list = sorted(Dict.iteritems(), key=lambda d: d[0])
    for word in answer_list:
        l = list(word[1])
        l.sort()
        print word[0] + ': ' + ', '.join(map(str, l))
def print_answer(answer_set):
    empty_set = set()
    if empty_set == answer_set:
        print 'None'
    else:
        answer_list=list(answer_set)
        answer_list.sort()
        print ', '.join(map(str,answer_list))
Dict = create_index()
List = []
while True:
    Query = raw_input()
    if Query == '':
        break
    List.append(Query)
print_index(Dict)
for Query in List:
    answer_set = set()
    if 'OR: ' in Query:
        print 'OR:',
        Query = Query[3:]
        Query_list = Query.split()
        for word in Query_list:
            if word != '' and word in Dict:
                answer_set = Dict[word] | answer_set
            print_answer(answer_set)
    else:
        if 'AND: ' in Query:
            Query = Query[4:]
            print 'AND:',
        Q_word_list = Query.split()
        if Q_word_list != []:
            for i in range(1, 101):
                answer_set.add(i)
            for word in Q_word_list:
                if word != '':
                    if word in Dict:
                        answer_set = Dict[word] & answer_set
                    else:
                        answer_set = set()
            print_answer(answer_set)
        else:
            print 'None'
