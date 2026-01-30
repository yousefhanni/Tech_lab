from odoo import models,fields , api
import logging
_logger = logging.getLogger(__name__)


class demo_inventory(models.Model):
    _name = 'demo.inventory'
    _description = 'Demo Inventory'

    #Data[ Fields + methods ]
    #Fields:
    name = fields.Char(string='Product Name', required=True)
    price= fields.Float(string='Price')
    quantity = fields.Integer(string='Quantity')
    total_price= fields.Float(string='Total Price',compute='_compute_total_price')

    status = fields.Selection([
        ('draft','Draft'),
        ('confirmed','Confirmed'),
    ],default='draft',string='Status')

    #computed method
    @api.depends('price','quantity')
    def _compute_total_price(self):
        for record in self:
            record.total_price=record.price*record.quantity


    def action_upgrade(self):

        vip_products=[]

        for record in self:

            new_price = record.price * 1.1

            if new_price>5000:
                vip_products.append(record.name)

            vals={
                'price': new_price,
                'status': "confirmed",
            }


            record.write(vals)

            #?????????????????????????

            _logger.info("VIP Products List (Over 5000) %s",vip_products)

        return True






# new_price = price * 1.1 ==>  price * (1 + 0.1 )
#                 new_price =   price + 10 % from price











