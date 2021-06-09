# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class xtracurricular(models.Model):
#     _name = 'xtracurricular.xtracurricular'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class Xtracurricular(models.Model):
    _name = 'xtracurricular.xtracurricular'
 
    name = fields.Char(string="Nama", required=True)
    description = fields.Text()

class Role(models.Model):
    _name = 'xtracurricular.role'
 
    role_name = fields.Char(string="Role Name", required=True)
    parent_role = fields.Char(string="Parent Role", required=False)
    responsibilities = fields.Text()