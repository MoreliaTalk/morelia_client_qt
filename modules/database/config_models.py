import sqlobject as orm


class Config(orm.SQLObject):
    """Generates a table containing data for client configuration settings.

    Args:
        param (str, required):
        value (str, optional):

    Returns:
        None
    """
    param = orm.StringCol(notNone=True, unique=True)
    value = orm.StringCol(default=None)
