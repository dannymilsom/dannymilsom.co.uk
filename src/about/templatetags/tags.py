from django import template
import re

register = template.Library()

@register.simple_tag
def active(request, pattern):
	"""
	Used in templates to identify the current page by parsing the URL, 
	returning active if the pattern matches the request path. 
	"""
	if re.search(pattern, request.path):
		return 'active'