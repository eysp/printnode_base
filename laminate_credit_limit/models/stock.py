# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime,timedelta
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError

class StockPicking(models.Model):
    _inherit = "stock.picking"

    credit_hold = fields.Boolean(string="Credit Hold", related="partner_id.credit_hold")

    def button_validate(self):
        for rec in self:
            if rec.credit_hold == True and rec.partner_id.credit_override == False and rec.picking_type_id.code == "outgoing":
                raise ValidationError(_('Customer is under credit hold'))
        return super(StockPicking, self).button_validate()