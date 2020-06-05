from odoo.addons.component.core import AbstractComponent
from odoo.addons.component.core import Component


class GenericAdapter(AbstractComponent):
    # same inheritance than Odoo models
    _name = 'minimal.adapter'
    _inherit = [
        'base.backend.adapter',  # adapter provided by Connector module
        'base.data.connector'  # Base Connector shared between all Components
    ]
    # usage is used for lookups of components
    _usage = 'backend.adapter'

    _external_model = None

    def _call(self, *args, **kwargs):
        location = self.backend_record.location
        # use client API

    def read(self, record_id: int, fields: list = None) -> dict:
        """ Search records according to some criterias
        and returns a list of ids
        """
        connection = self.backend_record.get_connection()
        model_model = connection.env(self._external_model)
        fields = fields or ()
        return model_model.read(record_id, fields)

    def search(self, filters: list = None) -> list:
        """ Search records according to some criterias
        and returns a list of ids
        """
        connection = self.backend_record.get_connection()
        model_model = connection.env(self._external_model)
        filters = filters or []
        # Attention! We limit records to just first 10
        return model_model.search(filters, limit=30)


# these are the components we need for our synchronization
class PartnerAdapter(Component):
    _name = 'minimal.partner.adapter'
    _inherit = 'minimal.adapter'
    _apply_on = [
        'minimal.res.partner'  # binding model it applies to
    ]
    _external_model = 'res.partner'  # the name of the model in external system
    _usage = 'backend.adapter'
