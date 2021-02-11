# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime,timedelta

class Partner(models.Model):
    _inherit = "res.partner"

    credit_hold = fields.Boolean(string="Credit Hold", compute="_compute_credit")
    credit_override = fields.Boolean(string="Credit Hold Override", store=True)
    allotted_past_due = fields.Integer(string="Allotted Days Past Due", store=True)


    def _compute_credit(self):
        for rec in self:
            credit = False
            if rec.credit > rec.credit_limit:
                credit = True 
            last_inv = self.env['account.move'].search([('id','in',rec.invoice_ids.ids),('payment_state','in',['not_paid'])], order="invoice_date_due ASC", limit=1)
            
            if last_inv:
                print(last_inv.id,'\n\n\n')
                inv_date = datetime.strptime(datetime.strftime(last_inv.invoice_date_due, '%Y-%m-%d'),'%Y-%m-%d')
                diff = datetime.today().date() - inv_date.date()
                print(diff.days,'\n\n\n')
                if rec.allotted_past_due < diff.days:
                    credit = True
            rec.credit_hold = credit