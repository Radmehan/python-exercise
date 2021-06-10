# from win32com.client import Dispatch
#
# speak=Dispatch("SAPI.SpVoice")
#
# speak.Speak("Harry vhai how r you")
import requests, json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today...let's begin")
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey=4502b5e1b10b488f99a4abc72f717a0b"
    re=requests.get(url)
    news=re.text
    # print(news)
    # print(news["status"])
    news_dict=json.loads(news)
    # print(news_dict)
    # print(news_dict["status"])
    # print(news_dict["articles"])
    arts=news_dict["articles"]
    for articles in arts:
        print(articles)
        print(speak(articles["title"]))
        print("Moving on the next news.Listen now carefully")
    speak("Thanks for listenning")
