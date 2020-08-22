import json
from rest_framework.renderers import JSONRenderer

class MovieJSONRenderer(JSONRenderer):
    charset = 'utf-8'  

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return json.dumps({'movie_review_data': data},ensure_ascii=False)