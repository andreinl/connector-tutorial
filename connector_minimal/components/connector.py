# © 2020 Andrei Levin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.addons.component.core import AbstractComponent


class BaseDataConnectorComponent(AbstractComponent):
    """Base Connector shared between all Components
    """
    # same inheritance as in Odoo models
    _name = 'base.data.connector'
    _inherit = 'base.connector'  # provided by Connector module
    # subscribe to:
    _collection = 'minimal.backend'
    # the collection will be inherited to the components below,
    # because they inherit from this component
