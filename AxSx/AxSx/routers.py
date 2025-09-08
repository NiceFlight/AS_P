"""使用在 admin.py 的設定"""


class myAppRouter:

    SYSTEM_APPS = {"auth", "admin", "contenttypes", "sessions"}

    def db_for_read(self, model, **hints):
        label = model._meta.app_label
        if label == "Routes_app":
            return "second"
        elif label == "Shipwreck_app":
            return "third"
        elif label == "Axsx_app":
            return "default"
        elif label in self.SYSTEM_APPS:
            return "fourth"
        return "fourth"

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "Routes_app":
            return "second"
        elif model._meta.app_label == "Shipwreck_app":
            return "third"
        elif model._meta.app_label == "Axsx_app":
            return "default"
        elif (
            model._meta.app_label == "sessions"
            or model._meta.app_label == "auth"
            or model._meta.app_label == "admin"
            or model._meta.app_label == "contenttypes"
        ):
            return "fourth"
        return "fourth"

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ("default", "second", "third", "fourth")
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the ZXC app only appears in the 'second'
        database.
        """
        if app_label == "Routes_app":
            return db == "second"
        elif app_label == "Shipwreck_app":
            return db == "third"
        elif app_label == "Axsx_app":
            return db == "default"
        elif app_label in {"auth", "admin", "contenttypes", "sessions", "migrations"}:
            return db == "fourth"
        return False
