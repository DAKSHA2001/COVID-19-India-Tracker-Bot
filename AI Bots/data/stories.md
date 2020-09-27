## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
  
## Casual Talk with location
* greet
  - utter_greet
* Information
  - utter_info
* Question{"disease":"corona", "location":"Karnataka"}
  - action_search
* Thankful
  - utter_goodbye
  
## Casual Talk without location
* greet
  - utter_greet
* Information
  - utter_info
* Question{"disease":"corona"}
  - utter_ask_location
* state{"location":"Karnataka"}
  - action_search
* Thankful
  - utter_goodbye
  
## Casual Talk without greet
* Information
  - utter_info
* Question{"disease":"corona", "location":"Karnataka"}
  - action_search
* Thankful
  - utter_goodbye
  
## Casual Talk with location without greet
* Information
  - utter_info
* Question{"disease":"corona"}
  - utter_ask_location
* state{"location":"Karnataka"}
  - action_search
* Thankful
  - utter_goodbye


## Disease + State
* greet
  - utter_greet
* Question{"disease":"corona", "location":"Karnataka"}
  - action_search
* Thankful
  - utter_goodbye
  
## Disease + State withot greet
* Question{"disease":"corona", "location":"Karnataka"}
  - action_search
* Thankful
  - utter_goodbye


## Disease + Location
* greet
  - utter_greet
* Question{"disease":"COVID-19"}
  - utter_ask_location
* state{"location":"Karnataka"}
  - action_search
* Thankful
  - utter_goodbye 
  
## Disease + Location without greet
* Question{"disease":"corona"}
  - utter_ask_location
* state
  - action_search
* Thankful
  - utter_goodbye 


## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
