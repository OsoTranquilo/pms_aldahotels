# Copyright 2019  Pablo Q. Barriuso
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class MigrateLog(models.Model):
    _name = "migrated.log"

    name = fields.Char("Message")
    date_time = fields.Datetime()
    migrated_hotel_id = fields.Many2one("migrated.hotel")
    model = fields.Selection(
        [
            ("partner", "res.partner"),
            ("product", "product.product"),
            ("folio", "hotel.folio"),
            ("reservation", "hotel.reservation"),
            ("service", "hotel.service"),
            ("payment", "account.payment"),
            ("return", "payment.return"),
            ("invoice", "account.invoice"),
            ("journal", "account.journal"),
        ]
    )
    remote_id = fields.Integer(
        copy=False,
        readonly=True,
        help="ID of the remote record in the previous version",
    )

    _order = "date_time desc"
