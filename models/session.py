# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api, _
from datetime import datetime
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = "session"
    _description = "c'est une session looool"


    name = fields.Char()
    nb_participant = fields.Integer()
    date_debut = fields.Date()
    date_fin = fields.Date()
    duree = fields.Char(string='Duree', compute='compute_duree')
    state = fields.Selection([('a', 'A'), ('b', 'B')])
    formationId = fields.Many2one('formation.formation', ondelete="cascade")
    categorie = fields.Char(string='categorie',compute='_onchange_formation')
    salle_ids = fields.Many2many('formation.salle', 'session_salle', 'session_id', 'salle_id')
    candidat_ids = fields.Many2many('formation.candidat', 'session_candidat', 'session_id', 'candidat_id')
    formateur_ids = fields.Many2many('formation.formateur', 'session_formateur', 'session_id', 'formateur_id')

    @api.one
    @api.depends('date_debut', 'date_fin')
    def compute_duree(self):
        if self.date_debut and self.date_fin:
            date_debut = datetime.strptime(self.date_debut, "%Y-%m-%d")
            date_fin = datetime.strptime(self.date_fin, "%Y-%m-%d")
            self.duree = date_fin - date_debut
        else:
            self.duree = False

    @api.one
    @api.depends('formationId')
    def _onchange_formation(self):
        self.categorie = self.formationId.categorie



    @api.one
    @api.constrains('date_debut', 'date_fin')
    def verif(self):
        date_debut = datetime.strptime(self.date_debut, "%Y-%m-%d")
        date_fin = datetime.strptime(self.date_fin, "%Y-%m-%d")
        if date_debut > date_fin:
            raise ValidationError("erreur date fin superieur")
