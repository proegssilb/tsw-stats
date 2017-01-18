    % rebase('layout-core.tpl', title='Index')
    % recent = setdefault('recent', ())
    % dmg = setdefault('dmg', ())
    % hard = setdefault('hard', ())

    <div class="container-fluid"> <!-- Quick Encounter List -->

      <div class="jumbotron">
        <h1>Combat Stats</h1>
        <p>Pick an encounter below, and get some data.</p>
      </div>

      <div class="row">
        <div class="col-md-1 spacer"></div>
        % if len(recent) > 0:
        <div class="col-sm-4 col-md-3 content-col">
          <h2>Latest Encounters</h2>
          <ol>
            % for enc in recent:
            <li><a href="/encounter/{{enc.encid}}">{{enc.title}} - {{enc.starttime}}</a></li>
            % end
          </ol>
          <a href="#">More...</a>
        </div>
        % end
        % if len(dmg) > 0:
        <div class="col-sm-4 col-md-3 content-col">
          <h2>Highest-dps Encounters</h2>
          <ol>
            % for enc in dmg:
            <li><a href="/encounter/{{enc.encid}}">{{'{} - {:,.2f}/s'.format(enc.title, enc.encdps)}}</a></li>
            % end
          </ol>
          <a href="#">More...</a>
        </div>
        % end
        % if len(hard) > 0:
        <div class="col-sm-4 col-md-3 content-col">
          <h2>Hardest Encounters</h2>
          <ol>
            % for enc in hard:
            <li><a href="/encounter/{{enc.encid}}">{{'{} - {:,.2f}/s'.format(enc.title, enc.encdps)}}, {{enc.deaths}} deaths</a></li>
            % end
          </ol>
          <a href="#">More...</a>
        </div>
        % end
        <div class="col-md-1 spacer"></div>
      </div>
    </div> <!-- Quick Encounter List -->
