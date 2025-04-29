#from colorama import init
#from termcolor import colored

pets = {
    'dogs': [
        {
            'name': 'Spot',
            'age': 2,
            'breed': 'Dalmatian',
            'description': 'Spot is an energetic puppy who seeks fun and adventure!',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-spot.jpeg'
        },
        {
            'name': 'Shadow',
            'age': 4,
            'breed': 'Border Collie',
            'description': 'Eager and curious, Shadow enjoys company and can always be found tagging along at your heels!',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-shadow.jpeg'
        }
    ],
    'cats': [
        {
            'name': 'Snowflake',
            'age': 1,
            'breed': 'Tabby',
            'description': 'Snowflake is a playful kitten who loves roaming the house and exploring.',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/cat-snowflake.jpeg'
        }
    ],
    'rabbits': [
        {
            'name': 'Easter',
            'age': 4,
            'breed': 'Mini Rex',
            'description': 'Easter is a sweet, gentle rabbit who likes spending most of the day sleeping.',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/rabbit-easter.jpeg'
        }
    ]
}
pet_type = "dogs"
"""
def animals(pet_type):
    print(pets[pet_type])
    for i in pets[pet_type]:
        print(i.keys())
        print(i.values())
        for a in i:
            print(a)
            #print(avalues())
animals(pet_type)
"""

"""
for x, y in pets.items():
    #This is print(x, y)
    print("\n")
    print("This is print(x, y)")
    print(x, y)
    print("\n")

    #This is x
    print("This is x:")
    print(x)
    print("\n")
    #Now this is y
    print("This is y:")
    print(y)
    print("\n")
"""

#This code dont work. #This code has been fixed!

for x, y in pets.items():
    if x == pet_type:
        #print(y)
        
        for z in y:
            print(z)
            #print(z.keys())
            #print(z.values())
            #for i1 in z.keys():
            #    print("i1")
            #    print(i1)
            for i2 in z.items():
                print("i2")
                print(i2)
                print("i2[1](i2.values)")
                if i2[0] == "name":
                    print("This is highlighted!!!+" + i2[0])
                else:
                    print(i2[0])