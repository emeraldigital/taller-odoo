# -*- coding: utf-8 -*-

import logging
from datetime import date
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    related_project_id = fields.Many2one(
        comodel_name="project.project",
        string="Related Project"
    )

    def write(self, values):
        # write ORM method is used to set "values" to all records contained into self,
        # so we check that arrives 1 record onto this overrided write. Because "state"
        # field is readonly doesn't apply onchange manner.
        if len(self) == 1 and 'state' in values and values.get('state') == 'sale':
            _logger.info("Starting project creation after confirmed sale order ...")
            project_obj = self.env['project.project']
            sale_order = self
            
            # Looking for project with sale order name.
            _logger.info("Test if a project with sale.order name has been created for ...")
            project = project_obj.search([
                ('name', '=', sale_order.name)
            ], limit=1)

            if not project:
                _logger.info("Project to create: %s" % sale_order.name)
                project = project_obj.create({
                    'name': sale_order.name,
                    'related_sale_order_id': sale_order.id,
                    'user_id': sale_order.user_id.id
                })

                # Creating / Linking task stages to project.
                _logger.info("Creating / Linking task stages for %s ...", project.name)
                task_stage_obj = self.env['project.task.type']
                task_stages = ('New', 'In Progress', 'Done', 'Canceled')
                for stage in task_stages:
                    # If there's any stage with specified name that's NOT personal for any user.
                    task_stage = task_stage_obj.search([
                        ('name', '=', stage),
                        ('user_id', '=', False)
                    ], limit=1)
                    
                    if not task_stage:
                        task_stage = task_stage_obj.create({
                            'name': stage,
                            'project_ids': [(4, project.id)]
                        })
                    else:
                        if project.id not in [t.id for t in task_stage.project_ids]:
                            task_stage.write({'project_ids': [(4, project.id)]})

            # Create 1st task at sale project.
            _logger.info("Creating first task for %s ..." % project.name)
            confirm_sale_task = self.env['project.task'].create({
                'name': 'Report to customer project for post-sale activities',
                'project_id': project.id,
                'partner_id': sale_order.partner_id.id,
                'date_deadline': date.today(),
                'user_ids': [(4, sale_order.user_id.id)]
            })

            # Set new chatter activity to created task.
            _logger.info("Scheduling first activity for '%s' ..." % confirm_sale_task.name)
            confirm_sale_task.activity_schedule(
                act_type_xmlid='mail.mail_activity_data_email',
                summary='Confirm to %s project for post-sale activities.' % sale_order.partner_id.name,
                note='Report to %s the project for post-sale activities via email.' % sale_order.partner_id.name,
                date_deadline=date.today(),
                user_id=sale_order.user_id.id
            )                    
            
            # Set newly created project to sale order values dictionary,
            # returning code flow control to Odoo.
            values['related_project_id'] = project.id
            _logger.info("%s ~ %s link created." % (sale_order, project))
        
        return super().write(values)
