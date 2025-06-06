#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author:Cybrosys Techno Solutions(odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import json

from odoo import http
from odoo.http import content_disposition, request
from odoo.tools import html_escape

dict_dec = {"type": "http", "auth": "user", "methods": ["POST"], "csrf": False}


class XLSXReportController(http.Controller):
    @http.route("/xlsx_reports", **dict_dec)
    def get_report_xlsx(self, model, options, output_format, *elts, **kw):
        uid = request.session.uid
        report_obj = request.env[model].with_user(uid)
        options = json.loads(options)
        # token = kw.get("token", None)
        token = kw.get("csrf_token", None)
        report_name = kw.get("report_name", None)
        try:
            if output_format == "xlsx":
                response = request.make_response(
                    None,
                    headers=[
                        ("Content-Type", "application/vnd.ms-excel"),
                        (
                            "Content-Disposition",
                            content_disposition(report_name + ".xlsx"),
                        ),
                    ],
                )
                report_obj.get_xlsx_report(options, response)
            response.set_cookie("fileToken", token)
            return response
        except Exception as e:
            se = http.serialize_exception(e)
            error = {"code": 200, "message": "Odoo Server Error", "data": se}
            return request.make_response(html_escape(json.dumps(error)))
