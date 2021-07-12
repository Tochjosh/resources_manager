
from resource_deco import resource_deco


@resource_deco(email='ore@decadev.com', password='decagon123')
def resource():
    '''This function returns business logic of our company'''
    return "This is the company most valuable resource"


print(resource())
