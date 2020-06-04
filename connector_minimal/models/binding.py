# © 2020 Andrei Levin - Didotech srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class ImportBinding(models.AbstractModel):
    """ Abstract Model for the Bindings.

    All the models used as bindings between Clients Systems and Odoo
    should ``_inherit`` it.
    """
    _name = 'minimal.binding'
    _inherit = 'external.binding'  # provided by connector module
    _description = 'Import Binding (abstract)'

    # odoo_id = odoo-side id must be declared in concrete model
    backend_id = fields.Many2one(
        comodel_name='minimal.backend',
        string='Import Backend',
        required=True,
        ondelete='restrict'
    )


class MinimalPartnerBinding(models.Model):
    _name = 'minimal.res.partner'
    _inherit = 'minimal.binding'
    _inherits = {
        'res.partner': 'odoo_id'
    }
    _description = 'External Partners'

    # Default name:
    # _rec_name = 'external_id'

    odoo_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partners',
        required=False,
        ondelete='cascade'
    )
    # Default external ID:
    external_id = fields.Char(string="External ID", required=False)
