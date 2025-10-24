from odoo import models, fields, api
from odoo.exceptions import ValidationError

class UserTask(models.model):
    _name = 'user.task' 
    _description = 'User Task'
    _order = 'deadline asc'

    name = fields.Char(string='Titulo', required=True)
    description = fields.Text(string='Descripcion')
    priority = fields.Selection(
        [('0', 'Baja'), ('1', 'Media'), ('2', 'Alta')],
        string='Prioridad',
        default='1'
    )
    state = fields.Selection(
        [('draft', 'Borrador'), ('in_progress', 'En Progreso'), ('done', 'Completda')],
        string='Estado',
        default='draft'
    )