# -- coding: utf-8 --
{
    'name': 'Laminate Works: Credit Limit',

    'summary': 'Laminate Works: Credit Limit',

    'description': """
    task id: 2447397

     1 - Contacts App (res.partner):
            New “Credit Hold” checkbox.
            New “Credit Hold Override” checkbox. 
            New “Allotted Days Past Due” integer field.

    2 - Sales App (sale.order):
        Related field to “credit hold” checkbox of the customer. This field is invisible when the checkbox is unchecked.
        Sales order “confirm” button: Throw blocking message “Customer is under credit hold” if “credit hold” checkbox is checked. 
        Do not throw blocking message if “credit hold override” on the customer is checked, regardless of “credit hold” checkbox status. 



    3 - Inventory App (stock.picking): Delivery Orders (operation type = Delivery, stock.picking.type)
        1. Related field to “credit hold” checkbox of customer. This field is invisible when checkbox is unchecked, and when the transfer operation type is not “delivery”
        Delivery Order “validate” button: Throw blocking message “Customer is under credit hold” if “credit hold” checkbox is checked. 
        Do not throw blocking message if “credit hold override” on customer is checked, regardless of “credit hold” checkbox status. 



    4 - Calculation of Credit Hold checkbox:
        “Credit hold” in res.partner model is checked if (record.credit > record.credit_limit) or if (“allotted days past due”  < the age of that customer’s oldest unpaid invoice).
        Credit hold override automation:
        Background: This checkbox is to be checked by sales managers to temporarily override a customer’s credit hold. 
        Function: all contacts “credit hold override” checkboxes are set to unchecked once per day
    
    """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OEEL-1',

    # any module necessary for this one to work correctly
    'depends': ['account','stock','sale'],

    # always loaded
    'data': [
        'views/res_partner_inherit.xml',
        'views/sale_order_inherit.xml',
        'views/stock_picking_inherit.xml',
        'actions/action.xml'
    ],

    'application': False,
}