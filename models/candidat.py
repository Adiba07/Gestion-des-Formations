# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class Candidat(models.Model):
    _name = "formation.candidat"
    _description = "candidat"
    _sql_constraints = [
        ('num_ins_unique', 'unique(num_ins)', 'numero d\' inscription existe  deja!')
    ]


    name = fields.Char(string='nom')
    num_ins = fields.Integer(string='numero d\'inscription')
    #session = fields.Many2many('session')
