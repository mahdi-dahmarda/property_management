from odoo import fields, models, api


class Property(models.Model):
    _name = "property"
    _description = "Property"

    name = fields.Char('Name', required=True)
    display_name = fields.Char(compute='_compute_display_name', recursive=True, store=True, index=True)
    active = fields.Boolean(default=True)
    is_root = fields.Boolean(default=True)
    type = fields.Selection([
        ('property', 'Property'),
        ('site', 'Site')
    ], string='Type', default='property')

    property_type = fields.Selection([
        ('building', 'Building'),
        ('land', 'Land'),
        ('yard', 'Yard')
    ], string='Property Type')
    building_type = fields.Selection([
        ('floor', 'Floor'),
        ('room', 'Room'),
        ('bathroom', 'Bathroom'),
        ('hall', 'Hall')
    ], string='Building Type')

    parent_id = fields.Many2one('property', string='Parent', index=True)
    child_ids = fields.One2many('property', 'parent_id', string='Children')

    @api.depends('name', 'parent_id.display_name')
    def _compute_display_name(self):
        for prop in self:
            if prop.parent_id:
                prop.display_name = '%s/%s' % (prop.parent_id.display_name, prop.name)
            else:
                prop.display_name = prop.name
