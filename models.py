# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Lead(models.Model):
    _inherit = 'res.partner' 

    lead_count = fields.Integer(compute='_lead_count', string='# of leads')

    @api.one
    def _lead_count(self):
        self.lead_count = self.env['crm.lead'].search_count([
            ('partner_id', '=', self.id),
            ('type','=','lead')])
        



