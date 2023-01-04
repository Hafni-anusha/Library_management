# Copyright (c) 2023, hafni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RendingRequest(Document):
	def validate(self):
        # check if a valid membership exist for this library member
		valid_membership = frappe.db.exists(
            'Library Membership',
            {
                'member': self.member,
				'paid':1
                # # 'docstatus': 1,
                # 'from_date': ('<', self.from_date),
                # 'to_date': ('>', self.to_date),
            },
        )
		if not valid_membership:
			frappe.throw('You are not an active member')
