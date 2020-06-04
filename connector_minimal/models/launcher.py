# © 2020 Andrei Levin - Didotech srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class LaunchImport(models.Model):
    _name = 'launch.import'
    _inherit = [
        'mail.thread'
    ]
    _description = 'Import External Data'

    name = fields.Selection([
        ('minimal.res.partner', 'Partner')
    ], string="Name", required=True)
    message = fields.Text(compute="dummy_function", string="Message", required=False)
    imported = fields.Boolean(string="Order Imported", default=False, readonly=True)

    backend_id = fields.Many2one(
        comodel_name='minimal.backend',
        string='Import Backend',
        required=True,
        ondelete='restrict'
    )

    _sql_constraints = [('external_table_name_unique', 'unique(name)', 'Table name should be unique!')]

    @api.one
    def dummy_function(self):
        backend = '{model},{backend_id}'.format(
            model=self.backend_id._name, backend_id=self.backend_id.id)

        checkpoints = self.env['connector.checkpoint'].search([
            ('backend_id', '=', backend),
            ('state', '=', 'need_review')
        ])
        if checkpoints:
            self.message = 'Please check and update products info'
        else:
            self.message = ''

    @api.model
    def import_batch(self, backend, model, filters=None):
        """ Prepare the import of multiple records from external table"""
        filters = filters or {}
        with backend.work_on(model) as work:
            importer = work.component(usage='batch.importer')
            return importer.run(filters=filters)

    # @api.model
    # def import_record(self, backend, external_id, row_data, force=False):
    #     """ Import an order """
    #     with backend.work_on(self._name) as work:
    #         importer = work.component(usage='record.importer')
    #         importer._row_data = row_data
    #         return importer.run(external_id, force=force)

    @api.multi
    def action_run_import(self):
        table = self.name
        binding_model = self.name
        messages = self.import_batch(self.backend_id, binding_model)
        if messages:
            message = '\n<br/>'.join(messages)
        else:
            message = '{} Imported'.format(table)
            self.imported = True

        database = self.backend_id.database
        self.message_post(
            subject=f'{database} : {table} import',
            body=message,
            message_type='notification'
        )
        return True
