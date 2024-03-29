# -*- coding: utf8 -*-
#
# Copyright (C) 2014 NDP Systèmes (<http://www.ndp-systemes.fr>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

{
    'name': 'MRP Scheduling on Working Days',
    'version': '0.1',
    'author': 'NDP Systèmes',
    'maintainer': 'NDP Systèmes',
    'category': 'Manufacture',
    'depends': ['resource', 'procurement', 'mrp', 'stock_working_days'],
    'description': """
MRP Scheduling on Working Days
==============================
This modules enables scheduling of production orders on working days defined by resources and associated calendars.

Each warehouse can have its own resource and associated calendar representing its opening days. If a warehouse is not
given a resource, then the system falls back to a company default calendar.
When a procurement needs to be scheduled by production, it counts only opened days defined by the applicable calendar.

Notes:
------

- When no applicable calendar is found, the module's default calendar is used which sets working days from Monday to
  Friday. This default calendar can be changed by authorized users.

- For a given procurement, the applicable warehouse is the warehouse of the location of the procurement. It falls back
  on the warehouse of the procurement itself only if no location is defined. This is to handle correctly
  inter-warehouse procurement with chained moves where the warehouse of the procurement is the warehouse of the end of
  the chain.

""",
    'website': 'http://www.ndp-systemes.fr',
    'data': [],
    'demo': [
        'mrp_working_days_demo.xml',
    ],
    'test': [],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
    'application': False,
}
