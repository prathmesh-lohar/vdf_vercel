from django.contrib import admin
from .models import feedback, gallery,feedback
from .models import page,mediaimg
from .models import mediafile
from .models import registration,contact
from .models import news,mou,viewer,naac,recruter
# Register your models here.


admin.site.register(page)

admin.site.register(gallery)

admin.site.register(mediaimg)

admin.site.register(mediafile)

admin.site.register(registration)

admin.site.register(news)

admin.site.register(mou)

admin.site.register(naac)

admin.site.register(viewer)

admin.site.register(recruter)

admin.site.register(contact)

admin.site.register(feedback)