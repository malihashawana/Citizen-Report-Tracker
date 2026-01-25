from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from .models import Report
from .serializers import ReportSerializer
from api.views import model, vectorizer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by('-created_at')
    serializer_class = ReportSerializer
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]  # ✅ IMPORTANT
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'status']

    def perform_create(self, serializer):
        description = serializer.validated_data.get('description', '')

        text_vec = vectorizer.transform([description])
        prediction = int(model.predict(text_vec)[0])

        serializer.save(
            risk_score=prediction,
            status='pending'
        )
