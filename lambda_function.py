from __future__ import print_function
import random
import json

Food_dict = {"tacos": ["cheese", "beef", "chicken", "tomatoes"], "pasta": ["noodles", "cheese", "meatballs", "marinara sauce", "alfredo sauce"], "hamburger": ["cheese", "beef", "lettuce", "ketchup", "onion"], "salad": ["ranch dressing", "cheese", "avocado", "chicken", "seeds", "broccoli"], "pizza": ["cheese", "tomato sauce", "pepperoni", "mushroom"], "smoothie": ["fruit", "yogurt", "milk", "peanut butter", "tea"]}
Ingredient_List = ["ketchup", "lettuce", "marinara sauce", "alfredo sauce", "meatballs", "noodles", "beef", "cheese", "green olives","goat cheese","broccoli","olive oil","nuts","seeds","parmesan","french dressing","balsamic vinegar","ranch dressing","italian dressing","raspberry vinaigrette","dried cranberries","cucumber","carrot","tomato sauce", "pepperoni","corn","strawberries","fruit","yogurt","milk","peanut butter","tea","pomegranate","watermelon","thousand island dressing","avocado","bell pepper","honey mustard dressing","cauliflower","radishes","edamame","steak","diced ham","blue cheese dressing","feta cheese","tomatoes","bacon","mushroom","chicken","kidney beans","black olives","egg","onion","cheddar cheese","mozzarella cheese"]
Sweet_List   = ["ketchup", "marinara sauce","alfredo sauce","raspberry vinaigrette","dried cranberries","cucumber","carrot","corn","strawberries","pomegranate","watermelon","french dressing","thousand island dressing","avocado","bell pepper","honey mustard dressing","cauliflower","radishes", "tomato sauce","fruit","yogurt","milk", "tea"]
Bitter_List = ["lettuce", "cheese", "green olives","noodles","meatballs","beef","goat cheese","broccoli","olive oil","nuts","seeds","parmesan","balsamic vinegar","ranch dressing","italian dressing", "pepperoni", "onion", "peanut butter", "edamame","steak", "diced ham","blue cheese dressing", "feta cheese", "tomatoes", "bacon", "mushroom", "chicken", "kidney beans", "black olives", "egg", "cheddar cheese", "mozzarella cheese"]
Sweet_Song = ["https://s3.amazonaws.com/bittersweet123565/Fauré+G.+-+Piece+for+flutepiano.mp3", "https://s3.amazonaws.com/bittersweet123565/Fireflies+by+Owl+City+(Harp+cover).mp3", "https://s3.amazonaws.com/bittersweet123565/Yiruma+River+Flows+In+You+(Higher+Pitch)+Piano.mp3"]
Bitter_Song = ["https://s3.amazonaws.com/bittersweet123565/Adam+Ben+Ezra+-+AWESOME+UPRIGHT+BASS+SOLO.mp3", "https://s3.amazonaws.com/bittersweet123565/Down+in+the+River+to+Pray.mp3", "https://s3.amazonaws.com/bittersweet123565/Ultra+Deep+Bass+Test+%233+-+Can+U+Hear+Me+(Slowed).mp3"]
default_song = "https://s3.amazonaws.com/bittersweet123565/The+Duck+Song.mp3"

def lambda_handler(event, context):
    if event['session']['new']:
        on_start()
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event)
    elif event['request']['type'] == "IntentRequest":
        return intent_scheme(event)
    elif event['request']['type'] == "SessionEndedRequest":
        return on_end()

def on_start():
    print("Session Started.")

def on_launch(event):
    ing = random.choice(Ingredient_List)
    onlunch_MSG = "Hi, welcome to BitterSweet Sounds. I will play music depending on food ingredients. What food do you like or are you eating? You could say for example: I like "+ ing + "or I'm eating" + ing
    reprompt_MSG = "What food do you like or are you eating? You could say for example: I like "+ ing + "or I'm eating" + ing
    card_TEXT = "Pick a food."
    card_TITLE = "Choose a food."
    return output_json_builder_with_reprompt_and_card(onlunch_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def on_end():
    print("Session Ended.")

def intent_scheme(event):
    intent_name = event['request']['intent']['name']
    if intent_name == "ingredientmusic":
        if 'value' in event['request']['intent']['slots']['food']:
            return extract_ingredient(event)
        else:
            return taste_to_url(event)
    elif intent_name in ["AMAZON.NoIntent", "AMAZON.StopIntent", "AMAZON.CancelIntent"]:
        return stop_the_skill(event)
    elif intent_name == "AMAZON.HelpIntent":
        return assistance(event)
    elif intent_name == "AMAZON.FallbackIntent":
        return fallback_call(event)

def extract_ingredient(event):
    food_name = event['request']['intent']['slots']['food']['value']
    ingredient_list = Food_dict[food_name]
    if food_name not in Food_dict:
        resultat = "You haven't used the full name of a food. If you don't know what to do you can say Help."
        reprompt_MSG = "You haven't used the full name of a food. Can you repeat?"
        card_TEXT = "Use the food name"
        card_TITLE = "Wrong food name"
    else:
        resultat = "You said you are eating " + str(food_name) + ". Which ingredient would you like to be enhanced?"
        reprompt_MSG = "Which of the following ingredients would you like to enhance with music?"
        reprompt_MSG += ' '
        resultat += ' '
        for x in ingredient_list:
            reprompt_MSG += x + ' '
            resultat += x + ' '
        card_TEXT = reprompt_MSG
        card_TITLE = "Choose ingredient"
    return output_json_builder_with_reprompt_and_card(resultat, card_TEXT, card_TITLE, reprompt_MSG, False)

def taste_to_url(event):
    ingredient_name = event['request']['intent']['slots']['ingredient']['value']
    if ingredient_name in Sweet_List:
        url = random.choice(Sweet_Song)
    elif ingredient_name in Bitter_List:
        url = random.choice(Bitter_Song)
    else:
        url = default_song
    return json_play_music(url)

def json_play_music(url):
    return {"response": {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
                    "audioItem": {
                        "stream": {
                            "token": "12345",
                            "url": url,
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }}

def stop_the_skill(event):
    stop_MSG = "Thank you. Bye!"
    reprompt_MSG = ""
    card_TEXT = "Bye."
    card_TITLE = "Bye Bye."
    return output_json_builder_with_reprompt_and_card(stop_MSG, card_TEXT, card_TITLE, reprompt_MSG, True)

def assistance(event):
    assistance_MSG = "You can choose among these ingredients: " + ', '.join(map(str, Ingredient_List)) + ". Be sure to use the full name when asking about the ingredient."
    reprompt_MSG = "Do you want to hear music from a food ingredient?"
    card_TEXT = "You've asked for help."
    card_TITLE = "Help"
    return output_json_builder_with_reprompt_and_card(assistance_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def fallback_call(event):
    fallback_MSG = "I can't help you with that, try rephrasing the question or ask for help by saying HELP."
    reprompt_MSG = "Do you want to hear music from a food ingredient?"
    card_TEXT = "You've asked a wrong question."
    card_TITLE = "Wrong question."
    return output_json_builder_with_reprompt_and_card(fallback_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def plain_text_builder(text_body):
    text_dict = {}
    text_dict['type'] = 'PlainText'
    text_dict['text'] = text_body
    return text_dict
def reprompt_builder(repr_text):
    reprompt_dict = {}
    reprompt_dict['outputSpeech'] = plain_text_builder(repr_text)
    return reprompt_dict

def card_builder(c_text, c_title):
    card_dict = {}
    card_dict['type'] = "Simple"
    card_dict['title'] = c_title
    card_dict['content'] = c_text
    return card_dict
def response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    speech_dict = {}
    speech_dict['outputSpeech'] = plain_text_builder(outputSpeach_text)
    speech_dict['card'] = card_builder(card_text, card_title)
    speech_dict['reprompt'] = reprompt_builder(reprompt_text)
    speech_dict['shouldEndSession'] = value
    return speech_dict
def output_json_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    response_dict = {}
    response_dict['version'] = '1.0'
    response_dict['response'] = response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value)
    return response_dict
