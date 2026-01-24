import os
import json
import joblib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Path to ml_model folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ml_path = os.path.join(BASE_DIR, '..', 'ml_model', 'text_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, '..', 'ml_model', 'vectorizer.pkl')

# Load the models
model = joblib.load(ml_path)
vectorizer = joblib.load(vectorizer_path)

@csrf_exempt
def analyze_text(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode('utf-8'))
            text = body.get('text', '')

            if not text:
                return JsonResponse({'error': 'Text is required'}, status=400)

            text_vec = vectorizer.transform([text])
            prediction = model.predict(text_vec)

            return JsonResponse({
                'risk_score': int(prediction[0])
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST allowed'}, status=405)

