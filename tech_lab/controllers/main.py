import json
import logging
import pdb

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class ProductPriceController(http.Controller):

    @http.route('/api/product_price', type='http', auth='public',
                methods=['POST'], csrf=False)
    def get_price(self, **kwargs):
        try:
            # --- Read JSON body ---
            payload = json.loads(request.httprequest.data or b'{}')
            product_id = payload.get('product_id')

            # --- LOG ---
            _logger.info("Request product_id=%s", product_id)

            # --- DEBUG ---
            pdb.set_trace()  # Breakpoint 1

            if not product_id:
                return request.make_json_response(
                    {"status": "fail", "message": "product_id required"}
                )

            product = request.env['product.product'].sudo().browse(int(product_id))

            pdb.set_trace()
            if not product.exists():
                return request.make_json_response(
                    {"status": "fail", "message": "Product not found"}
                )

            _logger.info(
                "Loaded product %s - price %s",
                product.display_name,
                product.lst_price,
            )

            pdb.set_trace()  # Breakpoint 2

            return request.make_json_response({
                "status": "success",
                "id": product.id,
                "name": product.display_name,
                "price": product.lst_price,
            })

        except Exception:
            _logger.exception("Error in /api/product_price")
            return request.make_json_response(
                {"status": "fail", "message": "Internal error"}
            )
