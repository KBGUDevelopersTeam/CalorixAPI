from db.Database import db_init
from db.Database import session
from db.models.Products import Products

import csv


db_init()

with open("clean_foods.csv", 'r') as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')


    with session() as db:
        for i, iter in enumerate(data):
            product_name = iter['product_name']
            kcal = iter['energy-kcal_100g']
            protein = iter['proteins_100g']
            fat = iter['fat_100g']
            carb = iter['carbohydrates_100g']


            db.add( Products(name=product_name,
                             calories=kcal,
                             proteins = protein,
                             fats=fat,
                             carbohydrates=carb) )

            db.commit()
