
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(wrd):
    for char in punctuation_chars:
        if char in wrd:
            wrd=wrd.replace(char, "");
    return wrd

def get_pos(str):
    count=0
    y=str.lower().split()
    for wrd in y:
        y=strip_punctuation(wrd);
        if y in positive_words:
            count+=1;
    return count

def get_neg(str):
    count=0
    wlist=str.lower().split()
    for wrd in wlist:
        wrd=strip_punctuation(wrd);
        if wrd in negative_words:
            count+=1;
    return count

infile=open('project_twitter_data.csv', 'r')
outfile=open('resulting_data.csv', 'w')
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
for aline in infile.readlines()[1:]:
    if aline[0]!='\n':
        row=aline.rstrip('\n');
        data=row.split(',')
        tweet=data[0]
        retweets=data[1]
        replies=data[2]
        pos=get_pos(tweet)
        neg=get_neg(tweet)
        net=pos-neg
        new_row='{}, {}, {}, {}, {}'.format(retweets, replies, pos, neg, net)
        outfile.write(new_row)
        outfile.write('\n')
