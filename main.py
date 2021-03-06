# chat bot main file
import pyttsx3 as voice
from wikipedia import summary as wiki_summary, PageError, DisambiguationError
from googlesearch import search


responses = {
    "hello": "Hello, what's up ?",
    "how is it going ?": "Good, How about you ?",
    "how are you": "I am feel fantastic",
    "what is your name": "I am Chat Bot builds with python you can call me anything.",
    "what do you do ?":  "I chat with you. You can tell me anything. I won't tell anyone about it, Trust Me!"
}

# initializing voice
voice_engine = voice.init()


def print_and_say(msg):
    print(msg)
    voice_engine.say(msg)
    voice_engine.runAndWait()


quit_chat = True

# start chat process
print_and_say("Type 'q' at anytime to quit.")
while quit_chat:
    message = input("\nType your message: ")

    if message == "q":
        # quit chat
        print_and_say("It was good talk, See you later!")
        quit_chat = False

    elif message == "search":
        quit_search = "yes"

        while quit_search.lower() == "yes":
            voice_engine.say("Search on google")
            voice_engine.runAndWait()
            query = input("\nSearch on google: ")
            for s in search(query, tld="com", num=10, stop=10, pause=2):
                print(s)

            quit_search = input("\nDo you want to search again?[yes,no] ")

    elif message == "wiki":
        quit_wiki = "yes"

        while quit_wiki == "yes":
            try:
                voice_engine.say("\nSearch on Wikipedia:")
                voice_engine.runAndWait()
                query = input("\nSearch on Wikipedia: ")

                # show them by line by line
                wiki = wiki_summary(query.title(), sentences=2)
                wikiSentence = wiki.split(". ")
                print_and_say("\n".join(wikiSentence))

            except (PageError, DisambiguationError) as e:
                # if document not found on wikipedia
                print_and_say("Your search did not match any documents on Wikipedia\n")

            finally:
                quit_wiki = input("\nDo you want to search again?[yes,no] ")

    else:
        try:
            print_and_say(responses[message.lower()])
        except KeyError:
            # if response not found
            print_and_say("I can't understand you.\n"
                          "Suggestions:\n"
                          "    Make sure all words are spelled correctly.\n"
                          "    Try different keywords.\n"
                          "    Try more general keywords.\n"
                          "    Try fewer keywords.")
