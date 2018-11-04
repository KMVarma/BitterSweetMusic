# BitterSweet Sounds

## Introduction

BitterSweet Music is an Amazon Alexa skill that plays songs that enhance either the bitter or sweet tastes in the food that a user is eating.  The user tells Alexa what they are eating and Alexa will identify the ingredients in the food, allow the user to choose one, and play a song that either compliments the bitter taste of a bitter ingredient or compliments the sweet taste of a sweet ingredient.

### Music's Affect on Taste



## Usage

In order to invoke the skill, the user should say "open BitterSweet Sounds"

To specify the food that the user wants to match music to, they can use the following utterances:

"{food}"
"{food}  please"
"I am going to eat {food}"
"I made {food}"
"I cooked {food}"
"I am eating {food}"
"I ate {food}"
"I cooked {food}"
"I like {food}"

In response to the above utterances, Alexa will list the ingredients in the food and ask the user to choose one to enhance the taste of. The user needs to respond with one of the ingredients and then the ingredient will be matched to a song that will start playing.  If the food is itself an ingredient (e.g. chicken), then no ingredients will be listed after the user specifies the food and the song will play immediately.

### Sample Usage

User: "Alexa, open BitterSweet Sounds"

Alexa: 
"Hi, welcome to the My Food to Music Alexa Skill. I will play music depending on food ingredients."
"What food do you like or are you eating? You could say for example: I like salad or I'm eating salad"

User: "I am eating a hamburger"

Alexa: "Which of the following ingredients would you like to enhance with music? Cheese, beef, lettuce, ketchup, onion"

User: "cheese"

Alexa: *plays a song that complements the bitter tastes in cheese*

## BitterSweet Custom Alexa Skill

bittersweet.json defines the interaction model for the skill.

## AWS Lambda Function

lambda_function.py is a serverless AWS labmda function that has all of the backend code.  It takes a JSON file from the frontend of the Alexa skill based on the user's utterance, interprets the JSON file to formulate a generate a new JSON file representing the response that the skill should provide.

## Future Work

* allow the skill to recognize more food and corresponding ingredients, as well as the possible songs that the ingredients can be mapped to.  This could potentially involve using a search API to find the ingredients in a given food or through consulting a knowledge base such as Wikidata.  One method we considered for recognizing/classifying unknown/unclassified food is through using image recognition to identify the food.
* incorporate the other taste receptors (sour, salty, umami) and other factors that influence taste, for example, matching the texture of a food to a texture of sound will enhance textural components.
* lighting and color can also influence taste receptors, so using the light ring on the echo or connecting it to lights in the home, the lighting can be altered to enhance certain tastes

## Potential Applications

There is potential for BitterSweet Sounds to be applied to health purposes such as increasing sweetness in food in order to satisfy someone's craving for sugar without them needing to eat a lot of sugar. It can also alter the taste of a food that a person doesn't like to make it taste better to them, which is useful in situations where a person needs to eat something they don't like the taste of. When someone is stressed their tastes are distorted, which in most cases means a craving for unhealthy food high in sugar and fat, so BitterSweet Sounds can provide a way to distort the taste of foods in order to match the distortion that stress is causing.
