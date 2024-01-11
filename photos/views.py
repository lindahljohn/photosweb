from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from iptcinfo3 import IPTCInfo

def index(request):
    return render(request, 'index.html')

def single(request):
    # Call the image_view function to extract IPTC data
    iptc_data = image_view(request)
    
    try:
        keywords = iptc_data['keywords']
        if len(keywords) > 0:
            keywords = keywords[0]
            keywords = keywords.decode()
    except:
        keywords = "none"    
    caption = iptc_data['caption/abstract']
    caption = caption.decode()
    
    # Pass the IPTC data to the HTML template
    return render(request, 'single.html', {
        'iptc_data': iptc_data, 
        'keywords': keywords,
        'caption': caption
        }
                  )

def image_view(request):
    # Open the image file
    with open('photos/static/testpicedited.jpg', 'rb') as image_file:
        # Create an IPTCInfo object
        iptc_info = IPTCInfo(image_file)

        # Extract the IPTC data
        iptc_data = iptc_info._data
        #iptc_data = str(iptc_data)

        # Return the IPTC data
        return iptc_data