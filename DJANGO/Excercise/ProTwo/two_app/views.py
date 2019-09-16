from django.shortcuts import render
from two_app.models import Topic,Webpage,AccessRecord
# Create your views here.
def index(request):
    # my_dict={'insert_content':"Welcome Django!"}
    # return render(request,'two_app/index.html',context=my_dict)
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    return render(request, 'two_app/index.html', context=date_dict)
