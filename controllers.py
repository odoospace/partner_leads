# -*- coding: utf-8 -*-
from openerp import http

# class PartnerCrmLeadExtra(http.Controller):
#     @http.route('/partner_crm_lead_extra/partner_crm_lead_extra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_crm_lead_extra/partner_crm_lead_extra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_crm_lead_extra.listing', {
#             'root': '/partner_crm_lead_extra/partner_crm_lead_extra',
#             'objects': http.request.env['partner_crm_lead_extra.partner_crm_lead_extra'].search([]),
#         })

#     @http.route('/partner_crm_lead_extra/partner_crm_lead_extra/objects/<model("partner_crm_lead_extra.partner_crm_lead_extra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_crm_lead_extra.object', {
#             'object': obj
#         })