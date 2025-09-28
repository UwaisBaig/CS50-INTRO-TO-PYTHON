fruits = [
    {"fruits":"apple", "calories":"130"},
    {"fruits":"banana", "calories":"110"},
    {"fruits":"grapefruit", "calories":"60"},
    {"fruits":"honeydew", "calories":"50"},
    {"fruits":"lemon", "calories":"15"},
    {"fruits":"nectarine", "calories":"60"},
    {"fruits":"peach", "calories":"60"},
    {"fruits":"pineapple", "calories":"50"},
    {"fruits":"strawberries", "calories":"50"},
    {"fruits":"watermelon", "calories":"80"},
    {"fruits":"sweet cherries", "calories":"100"},
    {"fruits":"plums", "calories":"70"},
    {"fruits":"tangerine", "calories":"50"},
    {"fruits":"pear", "calories":"100"},
    {"fruits":"orange", "calories":"80"},
    {"fruits":"lime", "calories":"20"},
    {"fruits":"kiwifruit", "calories":"90"},
    {"fruits":"grapes", "calories":"90"},
    {"fruits":"cantaloupe", "calories":"50"},
    {"fruits":"avocado", "calories":"50"},
]

k = input("Item: ").lower()

for item in fruits:
    if item["fruits"] == k:
        print("Calories:",item["calories"])
        break
