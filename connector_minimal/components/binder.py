# -*- coding: utf-8 -*-
# © 2020 Andrei Levin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
"""
Binders are components that know how to find the external ID for an Odoo ID,
how to find the Odoo ID for an external ID and how to create the binding between them
"""

from odoo.addons.component.core import Component
from odoo.addons.component.core import AbstractComponent


class MinimalGenericBinder(AbstractComponent):
    _name = 'minimal.data.binder'
    _inherit = [
        'base.binder',  # provided by connector module
        'base.data.connector'
    ]
    # _usage is used for lookups of components
    _usage = 'binder'


class PartnerBinder(Component):
    _name = 'mimimal.partner.binder'
    _inherit = 'minimal.data.binder'  # parent component common for all binders
    _apply_on = [
        'minimal.res.partner'
    ]
    _usage = 'binder'
