# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models,fields


class attestation(models.Model):
    _name = "formation.attestation"
    _description = "une attestation"

    candidat = fields.Many2one('formation.candidat')
    description = fields.Char()
    date = fields.Date()
    formation = fields.Many2one('formation.formation')
