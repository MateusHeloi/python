import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = ''
analyzer = SentimentIntensityAnalyzer()
def suggest_movies():
    phrase = input("Como voce esta se sentindo ?")
    emotion = analyzer.polarity_scores(phrase)['compound']

    if emotion <= -0.5:
        genre = "18" #Filme de Drama
    elif emotion < 0:
        genre = "35"#Filmes de comedia
    elif emotion < 0.5:
        genre = "10749"#Filmes de romance
    else:
        genre = "27"#Filmes de Terror

    url=f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genre}&vote_count.gte=4"
    response = requests.get(url).json()
    if response['results']:
        titles = [result ['title'] for result in response['results'][:3]]
        print("Recomendo os seguintes filmes para voce")
        for title in titles:
            print(f"-{title}")
    else:
        print("Não encontrei nenhuma sugestão de filme para voce")
def chatbot():
    print("Ola! sou um chat de sugestões de filmes. Como posso te ajudar hoje ?")
    while True:
        try:
            response = input().lower()
            if 'filme' in response:
                suggest_movies()
            elif 'tchau' in response or 'adeus' in response:
                print("Adeus vejo voce na proxima vez")
                break
            else:
                print("Desculpe não entendi o que quis dizer. ")
        except KeyboardInterrupt:
            break
chatbot()
