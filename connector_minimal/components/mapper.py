from odoo.addons.component.core import AbstractComponent
from odoo.addons.component.core import Component
from odoo.addons.connector.components.mapper import mapping


class GenericMapper(AbstractComponent):
    """Base Generic Mapper inherited by all Mappers
    """
    # same inheritance than Odoo models
    _name = 'minimal.mapper'
    _inherit = [
        'base.import.mapper',   # provided by Connector module
        'base.data.connector'  #
    ]
    # usage is used for lookups of components
    _usage = 'import.mapper'


class PartnerMapper(Component):
    _name = 'minimal.partner.import.mapper'
    _inherit = 'minimal.mapper'
    _apply_on = [
        'minimal.res.partner'
    ]
    _usage = 'import.mapper'

    direct = [
        ('name', 'name')
    ]

    @mapping
    def default_values(self, record):
        return {
            'external_id': record['id'],
            'backend_id': self.backend_record.id,
        }
