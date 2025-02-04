from ninja import NinjaAPI
from ninja.parser import Parser
from muscleinfo.api import router as muscleinfo
from volume.api import router as volume
from users.api import router as users
from calories.api import router as calories
from usda.api import router as usda
import orjson

class ORJSONParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)

api = NinjaAPI(parser=ORJSONParser(), csrf=True)

api.add_router("/", muscleinfo)
api.add_router("/", volume)
api.add_router("/", users)
api.add_router("/", calories)
api.add_router("/", usda)