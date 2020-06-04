# © 2020 Andrei Levin - Didotech srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
"""
This is a component that orchestrate the import

Connector uses termin "record" to refer to a single row
and "batch" to refer to multiple rows
"""

from odoo.addons.component.core import AbstractComponent
from odoo.addons.component.core import Component


class BatchImporter(AbstractComponent):
    """ The role of a BatchImporter is to search for a list of
    items to import, then it can either import them directly or delay
    the import of each item separately.
    """

    _name = 'minimal.batch.importer'
    _inherit = [
        'base.importer',  # provided by connector module
        'base.data.connector'
    ]
    _usage = 'batch.importer'

    def run(self, filters=None):
        """ Run the synchronization """
        # this one knows how to read data from external database
        for record_id in self.backend_adapter.search(filters):
            self._import_record(record_id)

    def _import_record(self, external_id):
        """ Import a record directly or delay the import of the record.

        Method to implement in sub-classes.
        """
        raise NotImplementedError


# class PartnerRecordImporter(Component):
#     _name = 'minimal.partner.importer'
#     _inherit = 'minimal.record.importer'  # parent component omitted for brevity
#     _apply_on = [
#         'minimal.res.partner'  # binder tables to which this importer applies
#     ]
#     _usage = 'record.importer'
#
#     def run(self, external_id):
#         # get the components we need for the sync
#
#         # this one knows how to speak to magento
#         backend_adapter = self.component(usage='backend.adapter')
#         # this one knows how to convert magento data to odoo data
#         mapper = self.component(usage='import.mapper')
#         # this one knows how to link magento/odoo records
#         binder = self.component(usage='binder')
#
#         # read external data from magento
#         external_data = backend_adapter.read(external_id)
#         # convert to odoo data
#         internal_data = mapper.map_record(external_data).values()
#         # find if the magento id already exists in odoo
#         binding = binder.to_internal(external_id)
#         if binding:
#             # if yes, we update it
#             binding.write(internal_data)
#         else:
#             # or we create it
#             binding = self.model.create(internal_data)
#         # finally, we bind both, so the next time we import
#         # the record, we'll update the same record instead of
#         # creating a new one
#         binder.bind(external_id, binding)


class PartnerBatchImporter(Component):
    _name = 'minimal.partner.importer'
    _inherit = 'minimal.batch.importer'
    _apply_on = [
        'minimal.res.partner'  # binding tables to which this importer applies
    ]
    _usage = 'batch.importer'
    _collection = 'minimal.backend'

    def _import_record(self, external_id):
        # get the components we need for the sync

        # this one knows how to speak to external system
        backend_adapter = self.component(usage='backend.adapter')
        # this one knows how to convert external data to odoo data
        mapper = self.component(usage='import.mapper')
        # this one knows how to link external/odoo records
        binder = self.component(usage='binder')

        # read data from external system
        external_data = backend_adapter.read(external_id)
        # convert to odoo data
        internal_data = mapper.map_record(external_data).values()
        # find if the external id already exists in odoo
        binding = binder.to_internal(external_id, unwrap=False)
        if binding:
            # if yes, we update it
            binding.write(internal_data)
        else:
            # or we create it
            binding = self.model.create(internal_data)
        # finally, we bind both, so the next time we import
        # the record, we'll update the same record instead of
        # creating a new one
        binder.bind(external_id, binding)

