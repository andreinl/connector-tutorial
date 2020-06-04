# © 2020 Andrei Levin - Didotech srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields
from .odoo_odoo import OdooAccess


class MinimalBackend(models.Model):
    _name = 'minimal.backend'
    _description = 'Minimal Backend'
    _inherit = 'connector.backend'  # provided by connector module

    _rec_name = 'database'

    hostname = fields.Char(string="Host", required=True)
    username = fields.Char(string="Username", required=True)
    password = fields.Char(string="Password", required=True)
    database = fields.Char(string="Database", required=True)

    # def import_partner(self, external_id: int) -> None:
    #     model = 'minimal.res.partner'  # name of the binding model
    #     with self.work_on(model_name=model) as work:
    #         importer = work.component(usage='record.importer')
    #         # returns an instance of PartnerImporter, which has been
    #         # found with:the collection name (minimal.backend, the model,
    #         # and the usage).
    #         importer.run(external_id)

    def get_connection(self):
        if not hasattr(self, 'connection'):
            self.connection = OdooAccess(self)
            user_model = self.connection.env("res.users")
            try:
                user_model.search([("login", "=", "admin")])
            except RuntimeError:
                print('External database is not accessible or is not used yet')
            except:
                print('External database is not accessible or is not used yet')
        return self.connection
