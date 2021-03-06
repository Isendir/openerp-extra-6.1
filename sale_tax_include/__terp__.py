##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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

{
    "name" : "Invoices and prices with taxes included",
    "version" : "1.0",
#    "depends" : ["sale","account_tax_include"],
    "depends" : ["sale","account"],
    "author" : "Tiny",
    "website" : "http://www.openerp.com",
    "category" : "Generic Modules/Sales & Purchases",
    "description": """Allow the user to work tax included prices.
Especially useful for b2c businesses.
    
This module implement the modification on the sale order form.
""",
    "init_xml" : [ ],
    "demo_xml" : [ ],
    "update_xml" : [ 'sale_tax_incl.xml' ],
    "active": False,
    "installable": True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
