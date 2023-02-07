from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Welcome to OmdenaKano OpenC \n"
            response += "1. Project \n"
            response += "2. Monitor Projects \n"
            response += "3. language \n"
            response += "4. about \n"

        elif text=="1":
            response = "CON Select State \n"
            response += "1. Plateau \n"
            response += "2. Ekiti \n"
            response += "3. Edo \n"
            response += "4. Kano \n"
            response +=" 5. Kaduna \n"
            
        elif text=="1*1":
            response = "CON Select LGE \n"
            response += "1. Barkin Ladi \n"
            response += "2. Bassa \n"
            response += "3. Bokkos \n"
            response += "4. Jos-East \n"
            response += "5. Jos-North \n"
            response += "6. Jos-South \n"
            response += "7. Kanam \n"
            response += "8. Kanke \n"
            response += "9. Langtang North \n"
        
          
               
        elif text=="1*1*1":
            response = "CON Select MDA \n"
            response += "1. Ministry of Works \n"
            response += "2. Ministry of Health \n"
            response += "3. Ministry of Water Resources and Energy \n"
            response += "4. Ministry of Tourism, Culture and Hospitality \n"
            
        elif text == "1*1*1*1":
            response = "CON Select Contractor \n"
            response += "1.  Fundation solid Nigeria \n"
            response += "2.  P.W Nig Limited \n"
            response += "3.  Rick Rock Construction Nig. Ltd. \n"
            response += "4.  EEC. International Co. Ltd \n"
            
        elif text == "1*1*1*1*2": 
            response = "END Project: \n Dualization of Polo Roundabout-Farin Gada Algadama-Rock Haven Alheri Road Network and Terminus-Bauchi Road at JOS/NORTH. \n Status:\n Completed \n Amount:\n N25,423,495,900 \n"  
       
    
    
        return HttpResponse(response)
