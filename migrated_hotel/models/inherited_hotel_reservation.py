# Copyright 2019  Pablo Q. Barriuso
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PmsReservation(models.Model):

    _inherit = "pms.reservation"

    remote_id = fields.Integer(
        copy=False,
        readonly=True,
        help="ID of the target record in the previous version",
    )

    def confirm(self):
        if self._context.get("tracking_disable"):
            return True
        return super().confirm()
