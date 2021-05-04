import requests  
from bs4 import BeautifulSoup  
from wordcloud import WordCloud, STOPWORDS  
import matplotlib.pyplot as plt  
from textblob import TextBlob  
headline_list = []  
url = 'https://inshorts.com/en/read/world'  
response = requests.get(url)  

def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')  
    headlines = soup.find_all(attrs={"itemprop": "headline"})  
    for headline in headlines:  
        headline_list.append(headline.text)  
        print(headline.text)  
    return headline_list  
words = print_headlines(response.text)  
comment_words = ''  
stopwords = set(STOPWORDS)  

for val in words:
    val = str(val)
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(comment_words)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("wordcloud.jpg")  
print() 

for sentense in words:
    var = TextBlob(
        sentense).sentiment.polarity  
    
    if var > 0:  
        print("The headline '" + sentense + "' is Positive sentiment.")
    elif var == 0:  
        print("The headline '" + sentense + "' is neutral sentiment.")
    else:  
        print("The headline '" + sentense + "' is negative sentiment.")