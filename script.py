from PIL import Image
from IPython.display import display 
import random 
import json 
import os 

class Face:
    face = ['White', 'Black']
    face_weights = [50, 50]
    face_files = {
    "White": "face1",
    "Black": "face2"
    }

class Ears:
    ears = ['No Earring', 'Left Earring', 'Right Earring', 'Two Earrings']
    ears_weights = [25, 30, 44, 1]
    ears_files = {
    "No Earring": "ears1",
    "Left Earring": "ears2",
    "Right Earring": "ears3",
    "Two Earrings": "ears4"
    }

class Eyes:
    eyes = ['Regular', 'Small', 'Rayban', 'Hipster', 'Focused']
    eyes_weight = [70, 10, 5, 1, 14]
    eyes_files = {
        "Regular": "eyes1",
        "Small": "eyes2",
        "Rayban": "eyes3",
        "Hipster": "eyes4",
        "Focused": "eyes5"     
    }

class Hair:
    hair = ['Up Hair', 'Down Hair', 'Mohawk', 'Red Mohawk', 'Orange Hair', 'Bubble Hair', 'Thin Hair', 'Bald', 'Blonde Hair', 'Caret Hair', 'Pony Tails']
    hair_weights = [10 , 10 , 10 , 10 ,10, 10, 10 ,10 ,10, 7 , 1 , 2]
    hair_files = {
    "Up Hair": "hair1",
    "Down Hair": "hair2",
    "Mohawk": "hair3",
    "Red Mohawk": "hair4",
    "Orange Hair": "hair5",
    "Bubble Hair": "hair6",
    "Emo Hair": "hair7",
    "Thin Hair": "hair8",
    "Bald": "hair9",
    "Blonde Hair": "hair10",
    "Caret Hair": "hair11",
    "Pony Tails": "hair12"
    }

class Mouth:
    mouth = ['Black Lipstick', 'Red Lipstick', 'Big Smile', 'Smile', 'Teeth Smile', 'Purple Lipstick']
    mouth_weights = [10, 10,50, 10,15, 5]
    mouth_files = {
        "Black Lipstick": "m1",
        "Red Lipstick": "m2",
        "Big Smile": "m3",
        "Smile": "m4",
        "Teeth Smile": "m5",
        "Purple Lipstick": "m6"
    }

class Nose:
    nose = ['Nose', 'Nose Ring']
    nose_weights = [90, 10]
    nose_files = {
        "Nose": "n1",
        "Nose Ring": "n2"   
    }


class Create_NFT:
    user_num = int(input("How many NFTs would you like to create?: "))
    all_images = []


    def create_image(self):
        new_image = {}
        face = Face()
        ears = Ears()
        eyes = Eyes()
        hair = Hair()
        mouth = Mouth()
        nose = Nose()
        new_image['Face'] = random.choices(face.face, face.face_weights)[0]
        new_image['Ears'] = random.choices(ears.ears, ears.ears_weights)[0]
        new_image['Eyes'] = random.choices(eyes.eyes, eyes.eyes_weight)[0]
        new_image['Hair'] = random.choices(hair.hair, hair.hair_weights)[0]
        new_image['Mouth'] = random.choices(mouth.mouth, mouth.mouth_weights)[0]
        new_image['Nose'] = random.choices(nose.nose, nose.nose_weights)[0]

        if new_image in self.all_images:
            self.create_image()
        else:
            return new_image 

    def unique_combinations(self):
        for i in range(user_num):
            new_trait_image = self.create_image()
            self.all_images.append(new_trait_image)
             
               




