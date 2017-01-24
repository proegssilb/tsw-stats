% encounters = setdefault('encounters', ())

<%
jsNumberRender = "function (data, type, row, meta) {return type === 'display' ? new Intl.NumberFormat().format(data) : data}"
jsDateRender = "function (data, type, row, meta) {return type === 'display' ? new Date(data).toLocaleString() : data}"
jsLinkRender = "function (data, type, row, meta) {return type === 'display' ? $('<a>').html(data).attr('href', '/encounter/' + row['encid']).get(0).outerHTML : data}"
colConfig = [
      {'attr': 'zone', 'name': 'Zone', 'class': 'all', 'js_data': '"zone"'},
      {'attr': 'title', 'name': 'Encounter', 'class': 'all',
       'js_data': '"title"', 'js_render': jsLinkRender},
      {'attr': 'starttime', 'name': 'Start Time', 'class': 'all',
       'js_data': '"starttime"', 'js_render': jsDateRender},
      {'attr': 'duration', 'name': 'Duration (s)', 'class': 'min-md',
       'js_data': '"duration"'},
      {'attr': 'damage', 'name': 'Total Damage', 'formatter': '{:,.2f}'.format,
      'class': 'min-sm', 'js_data': '"damage"', 'js_render': jsNumberRender},
      {'attr': 'encdps', 'name': 'Encounter DPS', 'formatter': '{:,.2f}'.format,
      'class': 'all', 'js_data': '"encdps"', 'js_render': jsNumberRender},
      {'attr': 'kills', 'name': 'Kills', 'formatter': '{:,.0f}'.format,
       'class': 'min-md', 'js_data': '"kills"', 'js_render': jsNumberRender},
      {'attr': 'deaths', 'name': 'Deaths', 'class': 'min-md', 'js_data': '"deaths"'},
      {'attr': 'aegisdmg', 'name': 'AEGIS Damage', 'formatter': '{:,.0f}'.format,
       'class': 'min-lg', 'js_data': '"aegisdmg"', 'js_render': jsNumberRender}
  ]
defOrder = '[[2, "desc"]]'
 %>

% include('objectList', title='Encounter List', objects=encounters, columns=colConfig, urlgen=(lambda obj: 'encounter/{}'.format(obj.encid)), urlcol='title', ajaxurl='/data/encounter', defaultOrder=defOrder)
<!-- Testing. -->
