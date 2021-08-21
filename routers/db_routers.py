# import user.models
# import products.models
#
# product_allmodels = dict([(name.lower(), cls) for name, cls in user.models.__dict__.items() if isinstance(cls, type)])
# user_allmodels = dict([(name.lower(), cls) for name, cls in user.models.__dict__.items() if isinstance(cls, type)])


class UserRouter(object):

    def db_for_read(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'user':
            return 'userdb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'user':
            return 'userdb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in chinook app"
        if obj1._meta.app_label == 'user' and obj2._meta.app_label == 'user':
            return True
        # Allow if neither is chinook app
        elif 'user' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_syncdb(self, db, model):
        if db == 'userdb' or model._meta.app_label == "user":
            return False  # we're not using syncdb on our legacy database
        else:  # but all other models/databases are fine
            return True


class ProductsRouter:

    def db_for_read(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'products':
            return 'productsdb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'products':
            return 'productsdb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in chinook app"
        if obj1._meta.app_label == 'products' and obj2._meta.app_label == 'products':
            return True
        # Allow if neither is chinook app
        elif 'products' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_syncdb(self, db, model):
        if db == 'productdb' or model._meta.app_label == "product":
            return False  # we're not using syncdb on our legacy database
        else:  # but all other models/databases are fine
            return True


