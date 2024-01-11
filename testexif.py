import exif

with open('photos/static/testpicedited.jpg', 'rb') as f:
    tags = exif.Image(f)

if not tags.has_exif:
    print('Sorry, image has no exif data.')
else:
    for tag in tags.list_all():
        try:
            print(f'{tag}: {tags[tag]}')
        except (KeyError, NotImplementedError):
            pass