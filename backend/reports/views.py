# reports/views.py
from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer
from api.views import model, vectorizer  # import your ML model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by('-created_at')
    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'urgency', 'status']
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        # Get description
        description = serializer.validated_data.get('description', '')

        # AI prediction
        text_vec = vectorizer.transform([description])
        prediction = model.predict(text_vec)[0]  # example: returns category 0/1
        serializer.save(
            category=prediction,          # map to your category
            urgency='medium',             # default for now
            credibility=0.8,              # dummy score
            summary=description[:100]     # simple summary
        )
