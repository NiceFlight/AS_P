'''使用在 admin.py 的設定'''
class myAppRouter:
    """
    A router to control all database operations on models in the
    Hub_app application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read Hub_app models go to second.
        """
        if model._meta.app_label == 'Hub_app':
            return 'second'
        elif model._meta.app_label == 'Shipwreck_app':
            return 'third'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write Hub_app models go to second.
        """
        if model._meta.app_label == 'Hub_app':
            return 'second'
        elif model._meta.app_label == 'Shipwreck_app':
            return 'third'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the Hub_app app is involved.
        """
        db_list = ('default', 'second', 'third')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the ZXC app only appears in the 'second'
        database.
        """
        if app_label == 'Hub_app':
            return db == 'second'
        elif app_label == 'Shipwreck_app':
            return db == 'third'
        return db == 'default'
    