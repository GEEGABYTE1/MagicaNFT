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
    hair = ['Up Hair', 'Down Hair', 'Mohawk', 'Red Mohawk', 'Orange Hair', 'Bubble Hair', 'Emo Hair',
    'Thin Hair',
    'Bald',
    'Blonde Hair',
    'Caret Hair',
    'Pony Tails']
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

face = Face()
ears = Ears()
eyes = Eyes()
hair = Hair()
mouth = Mouth()
nose = Nose()
class Create_NFT:
    user_num = int(input("How many NFTs would you like to create?: "))
    all_images = []
        
    def __init__(self):
        self.create_image()
        self.unique_combinations()
        self.unique_correspondance()
        self.get_trait_counts()
        self.generate_nfts()

    def create_image(self):
        new_image = {}
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
        for i in range(self.user_num):
            new_trait_image = self.create_image()
            self.all_images.append(new_trait_image)

    def unique_checker(self, all_images):
        seen = list()
        return not any(i in seen or seen.append(i) for i in self.all_images)

    def unique_correspondance(self):
        print("Are all images unique?: {}".format(self.unique_checker(self.all_images)))
        i = 0 
        for item in self.all_images:
            item['tokenId'] = i
            i += 1
        print(self.all_images)
    
    def get_trait_counts(self):
        face_count = {}
        for item in face.face:
            face_count[item] = 0
            
        ears_count = {}
        for item in ears.ears:
            ears_count[item] = 0

        eyes_count = {}
        for item in eyes.eyes:
            eyes_count[item] = 0
            
        hair_count = {}
        for item in hair.hair:
            hair_count[item] = 0
            
        mouth_count = {}
        for item in mouth.mouth:
            mouth_count[item] = 0
            
        nose_count = {}
        for item in nose.nose:
            nose_count[item] = 0

        for image in self.all_images:
            face_count[image["Face"]] += 1
            ears_count[image["Ears"]] += 1
            eyes_count[image["Eyes"]] += 1
            hair_count[image["Hair"]] += 1
            mouth_count[image["Mouth"]] += 1
            nose_count[image["Nose"]] += 1
            
        print(face_count)
        print(ears_count)
        print(eyes_count)
        print(hair_count)
        print(mouth_count)
        print(nose_count)

    def generate_nfts(self):
        os.mkdir(f'./images')

        for item in self.all_images:

            im1 = Image.open(f'./face_parts/face/{face.face_files[item["Face"]]}.png').convert('RGBA')
            im2 = Image.open(f'./face_parts/eyes/{eyes.eyes_files[item["Eyes"]]}.png').convert('RGBA')
            im3 = Image.open(f'./face_parts/ears/{ears.ears_files[item["Ears"]]}.png').convert('RGBA')
            im4 = Image.open(f'./face_parts/hair/{hair.hair_files[item["Hair"]]}.png').convert('RGBA')
            im5 = Image.open(f'./face_parts/mouth/{mouth.mouth_files[item["Mouth"]]}.png').convert('RGBA')
            im6 = Image.open(f'./face_parts/nose/{nose.nose_files[item["Nose"]]}.png').convert('RGBA')

            #Create each composite
            com1 = Image.alpha_composite(im1, im2)
            com2 = Image.alpha_composite(com1, im3)
            com3 = Image.alpha_composite(com2, im4)
            com4 = Image.alpha_composite(com3, im5)
            com5 = Image.alpha_composite(com4, im6)

                            

            #Convert to RGB
            rgb_im = com5.convert('RGB')
            file_name = str(item["tokenId"]) + ".png"
            rgb_im.save("./images/" + file_name)
               


test = Create_NFT()