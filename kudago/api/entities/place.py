from ..entities.base_entity import KudagoBase


class Place(KudagoBase):
    """Places for which the company publishes information. It can be museums, clubs, etc."""

    def __init__(self, **kwargs):
        """Init object.

        Kwargs:
            id: Identifier.
            title: Name of place.
        """
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')

        self._id_attrs = (self.id, )
