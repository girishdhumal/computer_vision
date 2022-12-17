from wordcloud import WordCloud
import matplotlib.pyplot as plt
text="Hello this is Vikas Gupta today I will talk about NSE. National Stock Exchange of India Limited is the leading stock exchange under the ownership of various group of domestic and global financial institutions, public and privately owned entities and individuals. It is located in Mumbai, Maharashtra."
wordcloud=WordCloud().generate(text)
plt.figure(figsize=(12,12))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
