# BitterSweet Sound

## Introduction

BitterSweet Music is an Amazon Alexa skill that plays songs that enhance either the bitter or sweet tastes in the food that a user is eating.  The user tells Alexa what they are eating and Alexa will identify the ingredients in the food, allow the user to choose one, and play a song that either compliments the bitter taste of a bitter ingredient or compliments the sweet taste of a sweet ingredient.

### Music's Affect on Taste



## Usage

### Sample Usage

## BitterSweet Custom Alexa Skill



## AWS Lambda Function

lambda_function.py is an AWS labmda function that has all of the backend code.  It is serverless

### Functionality
* `lambda_handler`:
* `on_start`:
* `on_launch`:
* `on_end`:
* `intent_scheme`:
* `ingredientCheck`:
* `taste_to_url`:
* `json_play_music`:
* `stop_the_skill`:
* `assistance`:
* `fallback_call`:
* `plain_text_builder`:
* `reprompt_builder`:
* `card_builder`:
* `response_field_builder_with_reprompt_and_card`:
* `output_json_builder_with_reprompt_and_card`:

## Notes

## Future Work

* allow the skill to recognize more food and corresponding ingredients, as well as the possible songs that the ingredients can be mapped to.  This could potentially involve using a search API to find the ingredients in a given food.  One way to recognize unknown food is through using image recognition to identify the food.
* Incorporating some knowledge base, like Wikidata, could also allow for more food to be recognized.  It would allow an easy discovery of the associated ingredients, and could help classify songs to match them to the qualities of a song (e.g. genre, tempo) that influence taste.
* incorporate other factors that influence taste, for example, matching the texture of a food to a texture of sound will enhance textural components
* Lighting and color can also influence taste receptors, so using the light ring on the echo or connecting it to lights in the home, the lighting can be altered to enhance certain tastes
* Not all sources that were consulted for mapping certain foods to the 5 taste receptors (bitter and sweet being two of them) agreed on a way to create this mapping, so the mapping that this skill uses should be verified in some way.  It could also be further researched though an empirical study.
* Other taste receptors (sour, salty, umami) can be considered in order to better match the taste of an ingredient because many are not necessarily bitter or sweet
