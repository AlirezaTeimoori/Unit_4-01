# Created by: Alireza Teimoori
# Created on: 30 Oct 2017
# Created for: ICS3UR-1
# Lesson: Unit 4_01
# This program converts fahrenheit temprature to celsius


import ui

def convert_to_fahrenheit(temprature_in_celsius):
    # converts temprature from celsius to fahrenheit
    
    # process
    temprature_in_fahrenheit = ((1.8)*temprature_in_celsius) + 32
    view['answer_label'].text = "That temprature in Fahrenheit is: " + str(temprature_in_fahrenheit)
    

def calculate_touch_up_inside(sender):
    # runs when user touches calculate button
    
    # input
    temprature_celsius = int(view['celsius_textfield'].text)
    
    # output
    convert_to_fahrenheit(temprature_celsius)
    



view = ui.load_view()
view.present('sheet')
