# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class Facturation(models.Model):
    _inherit = 'res.partner'

    numero_registre = fields.Char(string="numero de registre de comerce")

    '''
    nif : numero identificatuon fiscal : taille =15 charaactere 
     = nis : numero identification statique .char taille 15 
     numero article : cahr condition 11 carachtere 
     numero_registre 
    la date de derniere modif type date :
    capitale sociale : float 
    '''