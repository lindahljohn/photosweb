from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from iptcinfo3 import IPTCInfo

# def single(request):
#   template = loader.get_template('single.html')
#   return HttpResponse(template.render())

def single(request):
    # Call the image_view function to extract IPTC data
    iptc_data = image_view(request)

    # Pass the IPTC data to the HTML template
    return render(request, 'single.html', {'iptc_data': iptc_data})

# def image_view(request):
#     # Open the image file
#     with open('photos/static/testphoto.jpg', 'rb') as image_file:
#         # Create an IPTCInfo object
#         iptc_info = IPTCInfo(image_file)

#         # Extract the IPTC data
#         iptc_data = iptc_info._data   

#         # Pass the IPTC data to the HTML template
#         return render(request, 'single.html', {'iptc_data': iptc_data})

def image_view(request):
    # Open the image file
    with open('photos/static/testphoto.jpg', 'rb') as image_file:
        # Create an IPTCInfo object
        iptc_info = IPTCInfo(image_file)

        # Extract the IPTC data
        iptc_data = iptc_info._data

        # Return the IPTC data
        return iptc_data