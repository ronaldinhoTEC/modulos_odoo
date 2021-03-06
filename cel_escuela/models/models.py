# -*- coding: utf-8 -*-

from odoo import models, fields

class Escuela(models.Model):
    _name = 'test.escuela'
    
    name = fields.Char("Nombre")
    ie_type = fields.Selection([('nivel1','Inicial'),('nivel2', 'Primaria'),('primaria', 'Secundaria')],'Nivel Educativo') 
    ie_entry_time = fields.Datetime('Hora de entrada', default=fields.Datetime.now, required=False, readonly=False, select=True)
    ie_students = fields.Integer("Cantidad de estudiante")
    ie_turno = fields.Selection([('turno1','Mañana'),('turno2','Tarde'),('turno3','Noche')],'Nivel Educativo')