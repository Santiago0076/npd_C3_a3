class camera(MySerializer):
    my_attrs = {'an_attr': int, 'another_attr': str}
    an_attr = ('I am an attr')
    another_attr = (6)
    a_third_attr = ('I should not exist')
    def __init__(self, **kwargs):
        for i,k in self.my_attrs.items:
            print('Adding my attrs: {}'.format(i))
            print('Adding my types: {}'.format(k))
            value_type = k(kwargs.get(i))
            setattr(self, i, val_type)



