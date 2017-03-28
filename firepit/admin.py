from django.contrib import admin
from .models import Banner, SlideShowImage, ReviewControl, RequestQuote, RequestQuoteImage, DecorateSpace, DecorateSpaceImage, PowerSolutions
# Register your models here.

admin.site.register(Banner)
admin.site.register(SlideShowImage)
admin.site.register(ReviewControl)
admin.site.register(RequestQuote)
admin.site.register(RequestQuoteImage)
admin.site.register(DecorateSpace)
admin.site.register(DecorateSpaceImage)
admin.site.register(PowerSolutions)