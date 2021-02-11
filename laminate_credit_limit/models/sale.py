# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime,timedelta
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    credit_hold = fields.Boolean(string="Credit Hold", related="partner_id.credit_hold")

    def action_confirm(self):
        for rec in self:
            if rec.credit_hold ==True and rec.partner_id.credit_override == False:
                raise ValidationError(_('Customer is under credit hold'))
            super(SaleOrder, self).action_confirm()