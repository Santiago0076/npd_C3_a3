from json import loads, dumps

class MySerializer(object):

    @classmethod
    def deserialize(cls, jsonstr):
        json_dict = loads(json_str)
        cls = loads(jason_str)
        return cls(**d)



        # load from json to dict
        # initialize object, return

        return cls(**d)

    def serialize(self):
        # iterate over self.my_attrs
        # get attrs, set into dictionary
        # return dumps(dictionary)
        pass

