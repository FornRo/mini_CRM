from django import template

register = template.Library()


@register.simple_tag
def parameters_url_filter(value, field_name, urlencode=None):
    url = f'?{field_name}={value}'

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = f'{url}&{encoded_querystring}' if encoded_querystring else url
    return url

