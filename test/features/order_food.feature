Feature: Order food meal

    Scenario: Ordering food in form of thali
        Given a user of the system and thali 
        When the user orders required number of thali 
        Then the user successfully ordered
