from iptcinfo3 import IPTCInfo

# Open the image file
with open('photos/static/testphoto.jpg', 'rb') as image_file:
    # Create an IPTCInfo object
    iptc_info = IPTCInfo(image_file)

# Extract the IPTC data
iptc_data = iptc_info._data

# Print the IPTC fields
print('Object Name:', iptc_data['object name'])
print('Caption:', iptc_data['caption/abstract'])
print('Keywords:', iptc_data['keywords'])
print('Credit:', iptc_data['credit'])

print(iptc_data)