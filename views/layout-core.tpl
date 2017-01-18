<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- -->
    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    <!-- TODO: Fill this in somehow. -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link href="/static/bootstrap.min.css" rel="stylesheet">
    <link href="/static/custom.css" rel="stylesheet">
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
      </div>
    </nav>

    {{!base}}
    <!-- Apparently, placing scripts down here gets HTML onto the screen faster. -->
    <script src="/static/jquery.min.js"></script>
    <script src="/static/bootstrap.min.js"></script>
  </body>
</html>
