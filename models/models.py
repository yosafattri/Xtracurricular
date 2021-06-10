# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Xtracurricular(models.Model):
    _name = 'xtracurricular.xtracurricular'
 
    name = fields.Char(string="Nama", required=True)
    description = fields.Text()
    member_id = fields.Many2many('res.partner', string="Member")
    session_id = fields.Many2many('xtracurricular.session', string="Session")

class Role(models.Model):
    _name = 'xtracurricular.role'
 
    role_name = fields.Char(string="Role Name", required=True)
    parent_role = fields.Char(string="Parent Role", required=False)
    member_id = fields.Many2many('res.partner', string="Member")
    responsibilities = fields.Text()

class Session(models.Model):
    _name = 'xtracurricular.session'

    _sql_constraints = [
                     ('field_unique', 
                      'unique(name)',
                      'Session with that name already exist!')
]

    name = fields.Char(required=True)
    start = fields.Float(string="Mulai", required=True)
    end = fields.Float(string="Selesai", required=True)
    duration = fields.Float(digits=(6, 2), required=True)
    xtracurricular_id = fields.Many2many('xtracurricular.xtracurricular', string="Xtracurricular")

class Partner(models.Model):
    _inherit = 'res.partner'
    # _name = 'xtracurricular.member'

    extracurricular_id = fields.Many2many('xtracurricular.xtracurricular', string="Extracurricular")
    role_id = fields.Many2many('xtracurricular.role', string="Role")