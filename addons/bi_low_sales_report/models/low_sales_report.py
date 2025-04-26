from odoo import fields, models, tools

class LowSalesReport(models.Model):
	_name = 'low.sales.report.pivot'
	_auto = False
	_description = 'Low Sales Report'
	_rec_name = 'product_id'


	product_id = fields.Many2one('product.product', string='Product', readonly=True)
	total_qty_sold = fields.Float(string='Total Quantity Sold', readonly=True)
	total_revenue = fields.Float('Revenue', readonly=True)
	unit_price = fields.Float('Unit Price', readonly=True)

	def _select_sale(self, fields=None):
		if not fields:
			fields = {}
		select_ = """
			min(l.id) as id,
			count(*) as nbr,
			l.product_id as product_id,
			CASE WHEN l.product_id IS NOT NULL THEN sum(l.product_uom_qty) ELSE 0 END as total_qty_sold,
			CASE WHEN l.product_id IS NOT NULL THEN sum(l.price_unit) ELSE 0 END as unit_price,
			CASE WHEN l.product_id IS NOT NULL THEN sum(l.product_uom_qty * l.price_unit)  ELSE 0 END as total_revenue,
			s.id as order_id
		"""

		for field in fields.values():
			select_ += field
		return select_

	def _from_sale(self, from_clause=''):
		from_ = """
				sale_order_line l
				left join sale_order s on (s.id=l.order_id)
				left join product_product p on (l.product_id=p.id)
				left join product_template t on (p.product_tmpl_id=t.id)
				%s
		""" % from_clause
		return from_

	def _group_by_sale(self, groupby=''):
		groupby_ = """
			l.product_id,
			l.order_id,
			p.product_tmpl_id,
			s.id %s
		""" % (groupby)
		return groupby_


	def _select_additional_fields(self, fields):
		"""Hook to return additional fields SQL specification for select part of the table query.

		:param dict fields: additional fields info provided by _query overrides (old API), prefer overriding
			_select_additional_fields instead.
		:returns: mapping field -> SQL computation of the field
		:rtype: dict
		"""
		return fields

	def _query(self, with_clause='', fields=None, groupby='', from_clause=''):
		if not fields:
			fields = {}
		sale_report_fields = self._select_additional_fields(fields)
		with_ = ("WITH %s" % with_clause) if with_clause else ""
		return '%s (SELECT %s FROM %s WHERE l.display_type IS NULL GROUP BY %s)' % \
			   (with_, self._select_sale(sale_report_fields), self._from_sale(from_clause), self._group_by_sale(groupby))


	def init(self):
		# self._table = sale_report
		tools.drop_view_if_exists(self.env.cr, self._table)
		self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))


