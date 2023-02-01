from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("Home Page")
    return HttpResponse("This is home page")
    '''
    friends=['Nikhil', 'Harshal', 'Praful']
    return JsonResponse(friends, safe=False)
    '''