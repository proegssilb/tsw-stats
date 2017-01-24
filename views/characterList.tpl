% characters = setdefault('characters', ())

<%
jsNumberRender = "function (data, type, row, meta) {return type === 'display' ? new Intl.NumberFormat().format(data) : data}"
jsDateRender = "function (data, type, row, meta) {return type === 'display' ? new Date(data).toLocaleString() : data}"
jsLinkRender = "function (data, type, row, meta) {return type === 'display' ? $('<a>').html(data).attr('href', '/character/' + row['name']).get(0).outerHTML : data}"
colConfig = [
      {'attr': 'name', 'name': 'Nick', 'class': 'all', 'js_data': '"name"',
       'js_render': jsLinkRender},
      {'attr': 'firstSeen', 'name': 'First Seen', 'class': 'min-sm',
       'js_data': '"firstSeen"', 'js_render': jsDateRender},
      {'attr': 'lastSeen', 'name': 'Last Seen', 'class': 'all',
       'js_data': '"lastSeen"', 'js_render': jsDateRender},
      {'attr': 'seenTime', 'name': 'Seen Duration (s)', 'class': 'min-md',
       'js_data': '"seenTime"'},
      {'attr': 'damage', 'name': 'Total Damage', 'formatter': '{:,.2f}'.format,
      'class': 'min-sm', 'js_data': '"damage"', 'js_render': jsNumberRender},
      {'attr': 'healed', 'name': 'Total Healed', 'formatter': '{:,.2f}'.format,
      'class': 'min-sm', 'js_data': '"healed"', 'js_render': jsNumberRender},
      {'attr': 'kills', 'name': 'Kills', 'formatter': '{:,.0f}'.format,
       'class': 'min-md', 'js_data': '"kills"', 'js_render': jsNumberRender}
  ]
defOrder = '[[2, "desc"]]'
 %>

% include('objectList', title='Character List', objects=characters, columns=colConfig, urlgen=(lambda obj: 'character/{}'.format(obj.name)), urlcol='name', ajaxurl='/data/character', defaultOrder=defOrder)
<!-- Testing. -->
