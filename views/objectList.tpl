% objects = setdefault('objects', ())
% ajaxurl = setdefault('ajaxurl', '')
% columns = setdefault('columns', ())
% urlgen = setdefault('urlgen', None)
% urlcol = setdefault('urlcol', '')
% from sqlalchemy.inspection import inspect
% include('head', title='Index')

<div class="container-fluid">
  <div class="row">
    <div class="col-xs-12">
      <table id="listing-table" class="table table-hover" width="100%">
        <thead>
          <tr>
            % for col in columns:
            <th class="{{col.get('class', '')}}">
              {{col['name']}}
            </th>
            %end
          </tr>
        </thead>
        <tbody>
          % for obj in objects:
          <tr>
            % for col in columns:
            % v = inspect(obj).attrs[col['attr']].value
            <td data-sort="{{v}}">
              {{! '<a href="{}">'.format(urlgen(obj)) if col['attr'] in urlcol else ''}}
              {{col['formatter'](v) if col.get('formatter', None) else v}}
              {{! '</a>' if col['attr'] in urlcol else ''}}
            </td>
            % end
          </tr>
          % end
        </tbody>
      </table>
    </div>
  </div>
</div>

% include('js-bottom')

<script type="text/javascript">
$(document).ready( function () {
    $('#listing-table').DataTable({
      "pageLength": 25,
      "serverSide": true,
      "ajax": {
        "url": "{{ajaxurl}}",
        "type": "POST",
        "contentType": "application/json",
        "data": function ( d ) {
          return JSON.stringify( d );
        }
      },
      "columns": [
        % for col in columns:
        { "data": "{{col['attr']}}" },
        % end
      ],
      "responsive": {
        "breakpoints": [
          { "name": "xs", "width": 767 },
          { "name": "sm", "width": 991 },
          { "name": "md", "width": 1199 },
          { "name": "lg", "width": Infinity }
        ]
      }
    });
} );
</script>

% include('endhtml')
