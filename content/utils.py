import string
import random
def generate_id(Model,field,length):
    list = [random.choice(string.ascii_letters + string.digits) for n in xrange(length)]
    str = "".join(lst)
    if not Model.objects.filter(**{field:str}):
        return str
    else:
        generate_id(Model,field,length)
