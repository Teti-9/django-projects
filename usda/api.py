from ninja import Router
from ninja.responses import JsonResponse
from googletrans import Translator
from .utils import buscar_alimento

router = Router()

@router.get("/alimento/{query}")
async def lista_alimentos(request, query: str):
    async with Translator() as translator:
        query = await translator.translate(query, src='pt', dest='en')
        if query.text == 'minced meat':
            query.text = 'ground beef'

        foods = buscar_alimento(query.text)
        foods_list = [
            {
                'Nome': item['description'],
                'Carboidrato': next(
                    (nutrient['value'] for nutrient in item['foodNutrients']
                     if nutrient['nutrientName'] == 'Carbohydrate, by difference'), 0),
                'Proteína': next(
                    (nutrient['value'] for nutrient in item['foodNutrients']
                     if nutrient['nutrientName'] == 'Protein'), 0),
                'Gordura': next(
                    (nutrient['value'] for nutrient in item['foodNutrients']
                     if nutrient['nutrientName'] == 'Total lipid (fat)'), 0),
                'Fibras': next(
                    (nutrient['value'] for nutrient in item['foodNutrients']
                     if nutrient['nutrientName'] == 'Fiber, total dietary'), 0)
            }
            for item in foods.get('foods', [])
        ]

        return JsonResponse({"Alimentos (100g)": foods_list}, status=200)