import os
import joblib
from django.http import JsonResponse

# Path to ml_model folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ml_path = os.path.join(BASE_DIR, '..', 'ml_model', 'text_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, '..', 'ml_model', 'vectorizer.pkl')

# Load the models
model = joblib.load(ml_path)
vectorizer = joblib.load(vectorizer_path)

def analyze_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if not text:
            return JsonResponse({'error': 'No text provided'}, status=400)
        
        text_vec = vectorizer.transform([text])
        prediction = model.predict(text_vec)
        return JsonResponse({'prediction': prediction.tolist()})
    
    return JsonResponse({'error': 'Only POST allowed'}, status=400)
