from odoo import api,fields,models, _
from datetime import datetime


class Wizard_attestation(models.TransientModel):
    _name="foramtion.wizard_attestation"

    @api.multi
    def candidats(self):
        session_id = self.env.context.get('active_id')
        session = self.env['session'].browse(session_id)
        return  session.candidat_ids

    @api.multi
    def action_done(self):
        session_id = self.env.context.get('active_id')
        session = self.env['session'].browse(session_id)
        for candidat in self.candidat_ids:
            self.env['formation.attestation'].create({
                'date': self.date,
                'description': self.description,
                'candidat': candidat.id,
                'formation': session.formationId.id,
            })


    date=fields.Date()
    description=fields.Text()
    candidat_ids = fields.Many2many('formation.candidat','attestation_candidat','attestation_id','candidat_id',default=candidats)


