import datetime
import wikipedia

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%B %d, %Y")

def search_wikipedia(query):
    try:
        # Get a short 2-sentence summary
        result = wikipedia.summary(query, sentences=2)
        return result
    except:
        return "I could not find any specific information on that topic."
