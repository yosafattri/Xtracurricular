# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Xtracurricular(models.Model):
    _name = 'xtracurricular.xtracurricular'
 
    name = fields.Char(string="Nama", required=True)
    description = fields.Text()

class Role(models.Model):
    _name = 'xtracurricular.role'
 
    role_name = fields.Char(string="Role Name", required=True)
    parent_role = fields.Char(string="Parent Role", required=False)
    responsibilities = fields.Text()

class Session(models.Model):
    _name = 'xtracurricular.session'

    _sql_constraints = [
                     ('field_unique', 
                      'unique(name)',
                      'Choose another value - it has to be unique!')
]

    name = fields.Char(required=True)
    start = fields.Float(string="Mulai", required=True)
    end = fields.Float(string="Selesai", required=True)
    duration = fields.Float(digits=(6, 2), required=True)