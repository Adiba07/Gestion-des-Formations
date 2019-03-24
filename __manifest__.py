# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Gestion de formation',
    'version': '0.1',
    'author': 'Adiba  Boufeldja',
    'category': 'premier module',
    'description': "Ceci est mon prmier module du tp n_3",
    'depends': [
                'project'
                #'account_invoicing'
                ],
    'installable': True,
    'application': True,
    'data': [
             'security/users.xml',
             'security/ir.model.access.csv',
             'views/formation.xml',
             'wizard/wizard_attestation.xml',
             'views/session.xml',
             'views/salle.xml',
             'views/formateur.xml',
             'views/candidat.xml',
             'report/attestation_report.xml',
             #'views/facturation.xml',
             'views/attestation.xml'
             ],
    'website' :'www.modulen1.com',
    'license' : 'GPL-2',
}
