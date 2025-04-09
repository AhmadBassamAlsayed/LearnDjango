from django.http import HttpResponse

# Create your views here.
def main_view(request):
    num=request.session.get('cnt',0)+1
    request.session['cnt']=num
    if request.session['cnt'] > 4:
        del request.session['cnt']
    print (num)

    return HttpResponse("you visited us "+str(num)+" times")
