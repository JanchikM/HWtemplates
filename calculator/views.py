from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipe(request):
    dish = request.path[1:-1]
    recipes = {dish: {}}
    servings = int(request.GET.get('servings', 1))
    for ingredient, amount in DATA[dish].items():
        if isinstance(amount, int):
            recipes[dish].update({ingredient: int(amount * servings)})
        else:
            recipes[dish].update({ingredient: round(amount * servings, 3)})
    context = {
        'recipe': recipes[dish]
    }
    return render(request, 'calculator/index.html', context)
