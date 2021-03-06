# Copyright 2021 Dario Lodeiros
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class MigrateRoom(models.Model):
    _name = "migrated.room"

    last_sync = fields.Datetime("Last syncronization")
    migrated_hotel_id = fields.Many2one("migrated.hotel", readonly=True)
    remote_id = fields.Integer(
        copy=False,
        readonly=True,
        help="ID of the remote record in the previous version",
    )
    remote_name = fields.Char("Remote Name", readonly=True)
    pms_room_id = fields.Many2one(
        string="Current Room",
        comodel_name="pms.room",
    )
