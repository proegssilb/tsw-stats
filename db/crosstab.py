from sqlalchemy.sql import FromClause, column, ColumnElement
from sqlalchemy.orm import Query
from sqlalchemy.ext.compiler import compiles

"""
Copyright (c) 2016, Mehmet Ali "Mali" Akmanalp
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of sqlalchemy-crosstab-postgresql nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

class crosstab(FromClause):
    def __init__(self, stmt, return_def, categories=None, auto_order=True):
        if not (isinstance(return_def, (list, tuple))
                or return_def.is_selectable):
            raise TypeError('return_def must be a selectable or tuple/list')
        self.stmt = stmt
        self.columns = return_def if isinstance(return_def, (list, tuple)) \
            else return_def.columns
        self.categories = categories
        if hasattr(return_def, 'name'):
            self.name = return_def.name
        else:
            self.name = None

        if isinstance(self.stmt, Query):
            self.stmt = self.stmt.selectable
        if isinstance(self.categories, Query):
            self.categories = self.categories.selectable

        #Don't rely on the user to order their stuff
        if auto_order:
            self.stmt = self.stmt.order_by('1,2')
            if self.categories is not None:
                self.categories = self.categories.order_by('1')

    def _populate_column_collection(self):
        self._columns.update(
            column(name, type=type_)
            for name, type_ in self.names
        )

@compiles(crosstab, 'postgresql')
def visit_element(element, compiler, **kw):
    if element.categories is not None:
        return """crosstab($$%s$$, $$%s$$) AS (%s)""" % (
            compiler.visit_select(element.stmt),
            compiler.visit_select(element.categories),
            ", ".join(
                "\"%s\" %s" % (c.name, compiler.visit_typeclause(c))
                for c in element.c
                )
            )
    else:
        return """crosstab($$%s$$) AS (%s)""" % (
            compiler.visit_select(element.stmt),
            ", ".join(
                "%s %s" % (c.name, compiler.visit_typeclause(c))
                for c in element.c
                )
            )

from operator import add
from sqlalchemy import func, INTEGER

class row_total(ColumnElement):
    type = INTEGER()
    def __init__(self, cols):
        self.cols = cols

@compiles(row_total)
def compile_row_total(element, compiler, **kw):
    #coalesce_columns = [func.coalesce("'%s'" % x.name, 0) for x in element.cols]
    coalesce_columns = ['coalesce("%s", 0)' % x.name for x in element.cols]
    return "+".join(coalesce_columns)
