from rest_framework import generics 
from .models import Person 
from .serializers import PersonSerializer
from django.http import HttpResponse
from django.db.models import Q

class PersonCreateAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

def index(request):
    return HttpResponse("test")

class PersonSearch(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        city_query = self.request.query_params.get('city','')
        state_query = self.request.query_params.get('state','')
        name_query = self.request.query_params.get('name','')

        return Person.objects.filter(Q(city__icontains = city_query) & Q(state__icontains = state_query) & Q(name__icontains = name_query))


from django.http import JsonResponse
from rest_framework.decorators import api_view
import openai
from django.conf import settings

@api_view(['POST'])
def chat(request):
    user_message = request.data.get('message')
    if not user_message:
        return JsonResponse({'error': 'No message provided'}, status=400)


    openai.api_key = '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'

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": ""}
            ]
        )
        return JsonResponse({'response': response.choices[0].message['content']})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
