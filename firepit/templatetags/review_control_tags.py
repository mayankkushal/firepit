from django import template
from firepit.models import ReviewControl

register = template.Library()

@register.assignment_tag(takes_context=True)
def is_review_allowed(context):
	request = context['request']
	if request.user.is_anonymous():
		return True
	else:
		control = ReviewControl.objects.get(user=request.user)
		return control.allowed
