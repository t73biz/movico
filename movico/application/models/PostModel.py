__author__ = 'rchaplin'

from core.models.Model import Model

class PostModel(Model):

    fields = ['id','title','content','created','modified']

    table = 'posts'

    def __init__(self):
        # tableObj = getSchema(table)
        for field in self.fields:
            pass
#            setattr(self.__class__, field, tableObj.schema.field.default)