# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class formation(models.Model):
	_name="formation.formation"

	name = fields.Char()
	prix = fields.Float()
	categorie = fields.Char()
	#sessionId = fields.One2many('session' , 'formationId' , "refernece des session")