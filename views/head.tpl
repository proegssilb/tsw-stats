% title = setdefault('title', 'Index')
% description = setdefault('description', None)
% author = setdefault('author', None)
% extranav = setdefault('extranav', ())
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- -->
    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    <link href="/static/bootstrap.min.css" type="text/css" rel="stylesheet">
    <link href="/static/custom.css" type="text/css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/static/footable.bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="/static/dataTables.bootstrap.css">
    <link rel="stylesheet" type="text/css" href="/static/responsive.bootstrap.css">
    <link rel="stylesheet" type="text/css" href="/static/dygraph.min.css">
    % if description is not None:
    <meta name="description" content="{{description}}">
    % end
    % if author is not None:
    <meta name="author" content="{{author}}">
    % end
    <title>TSW Combat Stats - {{title}}</title>
  </head>
  <body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">TSW Combat Stats</a>
        </div>
        <!-- TODO: Allow more content to be added to navbar. Don't need it for index. -->
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a href="/encounter">Encounters</a></li>
            <li><a href="/character">Characters</a></li>
            <li><a href="/ability">Abilities</a></li>
          </ul>
        </div>
      </div>
    </nav>
