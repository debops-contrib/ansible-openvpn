
def dict_update(*items):
    d = {}
    for i in items:
        d.update(i)
    return d

def defaults_from(*items):
    return dict_update(*reversed(items))

class FilterModule(object):

    def filters(self):
        return {
            'dict_update': dict_update,
            'defaults_from': defaults_from,
        }
