# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class Salle(models.Model):
    _name = "formation.salle"
    _description = "salle"

    name = fields.Char()
    libre = fields.Boolean()
    nb_place = fields.Integer(default=20)
    #session = fields.Many2many('session')