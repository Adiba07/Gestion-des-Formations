# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class Formateur(models.Model):
	_name="formation.formateur"
	_description="formateur"
	_sql_constraints = [
		('matricule_unique', 'unique(matricule)', 'numero de matricule existe  deja!')
	]

	name = fields.Char()
	matricule = fields.Integer()
	diplome = fields.Char()
	#session = fields.Many2many('session')
