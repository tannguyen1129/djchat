from django import template

register = template.Library()

@register.filter 
def if_id_in_queryset(id, queryset):
    print("id",id)
    return any(id == query.receiver.id for query in queryset)



# @register.filter