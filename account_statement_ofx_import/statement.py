# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Pedro Manuel Baeza Romero
#    Copyright 2013 Servicios Tecnológicos Avanzados
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.tools.translate import _
from openerp.osv import fields, orm

class AccountStatementProfil(orm.Model):
    _inherit = "account.statement.profile"

    def get_import_type_selection(self, cr, uid, context=None):
        """
        Inherited from parent to add parser.
        """
        selection = super(AccountStatementProfil, self
                          ).get_import_type_selection(cr, uid,
                                                      context=context)
        selection.append(('ofx_so', _('OFX - Open Financial Exchange')))
        return selection

    _columns = {
        'import_type': fields.selection(
            get_import_type_selection,
            'Type of import',
            required=True,
            help="Choose here the method by which you want to import bank"
                 "statement for this profile."),

    }

