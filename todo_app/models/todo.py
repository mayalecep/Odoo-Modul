from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task'

    name = fields.Char('Task Name', required=True)
    description = fields.Text('Description')
    is_done = fields.Boolean('Done?', default=False)
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High')
    ], default='1', string='Priority')
    deadline = fields.Date('Deadline')
