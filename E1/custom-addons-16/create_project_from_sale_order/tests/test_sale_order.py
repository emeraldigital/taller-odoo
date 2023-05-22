# -*- coding: utf-8 -*-

import logging
from odoo.tests.common import TransactionCase

_logger = logging.getLogger('test_sale_order')

class TestSaleOrder(TransactionCase): #Test Driven Deveploment
    # CONTEXT
    # =======
    # For a dummy sale order (initial state = draft), we change its state field value,
    # so expected results are:
    # 
    # test 1: At draft, project won't be generated.
    # test 2: At sent, project won't be generated.
    # test 3: At sale, project will be generated.
    # test 4: At done, project won't be generated.
    # test 5: At cancel, project won't be generated.
    # test 6: Through all state long, project will be starting at 'sale' state.
    # test 7: When quotation is canceled, it doesn't generate project.

    # Configuration for all tests.
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

        # User for tests
        user_admin = self.env.ref("base.user_admin")
        self.env = self.env(user=user_admin)

        # Sale order to do tests
        customer = self.env['res.partner'].create({
            'name': 'Valid Lelitre',
            'email': 'valid.lelitre@agrolait.com'
        })

        free_product = self.env['product.product'].create({
            'name': 'Free product',
            'list_price': 0.0,
        })

        self.sale_order = self.env['sale.order'].create({
            'partner_id': customer.id,
            'user_id': user_admin.id
        })

        self.env['sale.order.line'].create({
            'order_id': self.sale_order.id,
            'name': free_product.name,
            'product_id': free_product.id
        })


    def test_1_draft_state_does_not_generate_project(self):
        """Test 1. When sale.order is created."""
        _logger.info('%s\nsale_order.state = %s' % ('*' * 50, self.sale_order.state))

        projects_from_sale = self.env['project.project'].search_count([
            ('id', '=', self.sale_order.related_project_id.id)
        ])

        self.assertEqual(projects_from_sale, 0)
        _logger.info('OK!')

    def test_2_sent_state_does_not_generate_project(self):
        """Test 2. When sale.order changes to 'sent quotation' state ..."""
        _logger.info('%s\nsale_order.state = %s' % ('*' * 50, self.sale_order.state))

        self.sale_order.action_quotation_sent()

        projects_from_sale = self.env['project.project'].search_count([
            ('id', '=', self.sale_order.related_project_id.id)
        ])

        self.assertEqual(projects_from_sale, 0)
        _logger.info('OK!')

    def test_3_sale_state_generate_project(self):
        """Test 3. When sale.order changes to 'sale' state ..."""
        _logger.info('%s\nsale_order.state = %s' % ('*' * 50, self.sale_order.state))
        
        self.sale_order.action_confirm()

        projects_from_sale = self.env['project.project'].search_count([
            ('id', '=', self.sale_order.related_project_id.id)
        ])

        self.assertEqual(projects_from_sale, 1)
        _logger.info('OK!')

    def test_4_done_state_does_not_generate_project(self):
        """Test 4. When sale.order changes to 'done' state ..."""
        _logger.info('%s\nsale_order.state = %s' % ('*' * 50, self.sale_order.state))
        
        self.sale_order.action_done()

        projects_from_sale = self.env['project.project'].search_count([
            ('id', '=', self.sale_order.related_project_id.id)
        ])

        self.assertEqual(projects_from_sale, 0)
        _logger.info('OK!')

    def test_5_cancel_state_does_not_generate_project(self):
        """Test 5. When sale.order changes to 'cancel' state ..."""
        _logger.info('%s\nsale_order.state = %s' % ('*' * 50, self.sale_order.state))
        
        self.sale_order._action_cancel()

        projects_from_sale = self.env['project.project'].search_count([
            ('id', '=', self.sale_order.related_project_id.id)
        ])

        self.assertEqual(projects_from_sale, 0)
        _logger.info('OK!')

    def test_6_walkthrough_all_states_only_sale_generates_project(self):
        """Test 6. When state change along all sale stateS, only 'sale' generates a project ..."""
        _logger.info('*' * 50)
        
        project_obj = self.env['project.project']
        states = {
            'draft': None,
            'sent': 'action_quotation_sent()',
            'sale': 'action_confirm()',
            'done': 'action_done()',
            'cancel': '_action_cancel()'
        }

        for key, value in states.items():
            _logger.info("Next state to evaluate: %s (%s), current state: %s ..." % (key, value, self.sale_order.state))

            if key != 'draft':
                eval('self.sale_order.%s' % value)

            projects_from_sale = project_obj.search_count([
                ('id', '=', self.sale_order.related_project_id.id)
            ])
            
            self.assertEqual(
                projects_from_sale,
                1 if self.sale_order.state in ('sale', 'done', 'cancel') else 0
            )

            _logger.info("OK!: %s ..." % key)

    def test_7_quotation_canceled_does_not_generate_project(self):
        """Test 6. When state change along all sale stateS, only 'sale' generates a project ..."""
        _logger.info('*' * 50)
        
        project_obj = self.env['project.project']
        states = {
            'draft': None,
            'sent': 'action_quotation_sent()',
            'cancel': '_action_cancel()'
        }

        for key, value in states.items():
            _logger.info("Next state to evaluate: %s (%s), current state: %s ..." % (key, value, self.sale_order.state))

            if key != 'draft':
                eval('self.sale_order.%s' % value)

            projects_from_sale = project_obj.search_count([
                ('id', '=', self.sale_order.related_project_id.id)
            ])
            
            self.assertEqual(projects_from_sale, 0)

            _logger.info("OK!: %s ..." % key)
