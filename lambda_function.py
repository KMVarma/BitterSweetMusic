import random
import json

Food_dict = {"tacos": ["cheese", "beef", "chicken", "tomato"], "pasta": ["noodles", "cheese", "meatball", "marinara sauce", "alfredo sauce"], "hamburger": ["cheese", "beef", "lettuce", "ketchup", "onion"], "salad": ["ranch dressing", "cheese", "avocado", "chicken", "seeds", "brocolli"], "pizza": ["cheese", "tomato sauce", "pepperoni", "mushrooms"], "smoothie": ["fruit", "yogurt", "milk", "peanut butter", "tea"]}
Ingredient_List = ["green olives","goat cheese","brocolli","extra virgin olive oil","nuts","seeds","parmesan","french dressing","balsamic vinegar","ranch dressing","italian dressing","caesar dressing","raspberry vinaigrette","dried cranberries","cucumber","carrot","corn","strawberries","pomegranate","watermelon","thousand island dressing","avocado","bell pepper","honey mustard dressing","cauliflower","radishes","edamame","steak","diced ham","blue cheese dressing","feta cheese","tomatoes","bacon","mushroom","chicken","kidney beans","black olives","egg","red onion","cheddar cheese","mozzarella cheese"]
Sweet_List   = ["raspberry vinaigrette","dried cranberries","cucumber","carrot","corn","strawberries","pomegranate","watermelon","thousand island dressing","avocado","bell pepper","honey mustard dressing","cauliflower","radishes","edamame","steak","diced ham","blue cheese dressing","feta cheese","tomatoes","bacon","mushroom","chicken","kidney beans","black olives","egg","red onion","cheddar cheese","mozzarella cheese"]
Bitter_List = ["green olives","goat cheese","brocolli","extra virgin olive oil","nuts","seeds","parmesan","french dressing","balsamic vinegar","ranch dressing","italian dressing","caesar dressing"]
Sweet_Song = ["https://www.youtube.com/watch?v=_kYYzwo7l5c", "https://www.youtube.com/watch?v=LeOfe-fpHNc", "https://www.youtube.com/watch?v=3eBnlAfvbqE"]
Bitter_Song = ["https://www.youtube.com/watch?v=pyUZh_Cbw6Q", "https://www.youtube.com/watch?v=lMl0kxzf4YU", "https://www.youtube.com/watch?v=pJDyrEGgyfc"]

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
    onlunch_MSG = "Hi, welcome to the My Food to Music Alexa Skill. I will play music depending on Salad Ingredients."
    "You could say for example: I like "+ ing
    reprompt_MSG = "What do you like ?"
    card_TEXT = "Pick a Ingredient."
    card_TITLE = "Choose a ingredient."
    return output_json_builder_with_reprompt_and_card(onlunch_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
def on_end():
    print("Session Ended.")
def intent_scheme(event):
    intent_name = event['request']['intent']['name']
    if intent_name == "ingredientmusic":
        #return ingredientCheck(event)     
        return taste_to_url(event)
    elif intent_name in ["AMAZON.NoIntent", "AMAZON.StopIntent", "AMAZON.CancelIntent"]:
        return stop_the_skill(event)
    elif intent_name == "AMAZON.HelpIntent":
        return assistance(event)
    elif intent_name == "AMAZON.FallbackIntent":
        return fallback_call(event)
    
def ingredientCheck(event):
    ingredient_name=event['request']['intent']['slots']['ingredient']['value']
    ingredient_list_lower=[w.lower() for w in Ingredient_List]
    if ingredient_name.lower() in ingredient_list_lower:
        reprompt_MSG = "You want to hear music from salad ingredient"
        card_TEXT = "You've picked " + ingredient_name
        card_TITLE = "You've picked " + ingredient_name
        resultat = "i am a nice ingredient" + ingredient # ToDo: get info
        return output_json_builder_with_reprompt_and_card(resultat, card_TEXT, card_TITLE, reprompt_MSG, False)
    else:
        wrongname_MSG = "You haven't used the full name of a player. If you don't know which ingredients you can pick say Help."
        reprompt_MSG = "Do you want to hear music from salad ingredient ?"
        card_TEXT = "Use the ingredient name."
        card_TITLE = "Wrong ingredient name."
        return output_json_builder_with_reprompt_and_card(wrongname_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def taste_to_url(event):
    ingredient_name=event['request']['intent']['slots']['ingredient']['value']
    if ingredient_name in Sweet_List:
        url = random.choice(Sweet_Song)
    else:
        url = random.choice(Bitter_Song)
    return json_play_music(url)

def json_play_music(url):
    data = {}
    data['type']="AudioPlayer.Play"
    data['playBehavior']= "REPLACE_ALL"
    data['audioItem']= {"stream": {"url": url, "token":"sweet_bitter", "offsetInMilliseconds":0}}
    return data
        
def stop_the_skill(event):
    stop_MSG = "Thank you. Bye!"
    reprompt_MSG = ""
    card_TEXT = "Bye."
    card_TITLE = "Bye Bye."
    return output_json_builder_with_reprompt_and_card(stop_MSG, card_TEXT, card_TITLE, reprompt_MSG, True)
    
def assistance(event):
    assistance_MSG = "You can choose among these ingredients: " + ', '.join(map(str, Ingredient_List)) + ". Be sure to use the full name when asking about the ingredient."
    reprompt_MSG = "Do you want to hear music from salad ingredient ?r?"
    card_TEXT = "You've asked for help."
    card_TITLE = "Help"
    return output_json_builder_with_reprompt_and_card(assistance_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
def fallback_call(event):
    fallback_MSG = "I can't help you with that, try rephrasing the question or ask for help by saying HELP."
    reprompt_MSG = "Do you want to hear music from salad ingredient ?"
    card_TEXT = "You've asked a wrong question."
    card_TITLE = "Wrong question."
    return output_json_builder_with_reprompt_and_card(fallback_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
    
# The response of our Lambda function should be in a json format.
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
