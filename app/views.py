from django.shortcuts import render
from .serializers import IrisInputSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from joblib import load
model = load('./app/notebooks/savedModels/model.joblib')

def home(request):
     if request.method == 'POST':
          sepal_length = request.POST['sepal_length']
          sepal_width = request.POST['sepal_width']
          petal_length = request.POST['petal_length']
          petal_width = request.POST['petal_width']
          # y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
          y_pred = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
          if y_pred[0] == 0:
               y_pred = 'Setosa'
          elif y_pred[0] == 1:
               y_pred = 'Verscicolor'
          else:
               y_pred = 'Virginica'
          print(y_pred)
          return render(request, 'home.html', {'result' : y_pred})
     return render(request,'home.html')

class IrisPredictionView(APIView):
    def post(self, request):
        input_serializer = IrisInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        sepal_length = input_serializer.validated_data['sepal_length']
        sepal_width = input_serializer.validated_data['sepal_width']
        petal_length = input_serializer.validated_data['petal_length']
        petal_width = input_serializer.validated_data['petal_width']

        # Make predictions using your model
        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        # Adjust this part based on how your model is loaded and used.

        # Placeholder response for illustration
        if y_pred == 0:
            result = 'Setosa'
        elif y_pred == 1:
            result = 'Versicolor'
        else:
            result = 'Virginica'
        return Response({'result': result})
