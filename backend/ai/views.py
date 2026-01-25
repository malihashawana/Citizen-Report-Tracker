import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def analyze_text(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        text = body.get('text', '')

        # mock score for now (replace with ML model)
        risk_score = 3

        return JsonResponse({'risk_score': risk_score})
