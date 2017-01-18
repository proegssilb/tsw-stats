    % rebase('layout-core.tpl', title='Index')
    % recent = setdefault('recent', ())
    % dmg = setdefault('dmg', ())
    % hard = setdefault('hard', ())

    <div class="jumbotron">
      <div class="container">
        <h1>Combat Stats</h1>
        <p>Pick an encounter below, and get some data.</p>
      </div>
    </div>

    <div class="container"> <!-- Quick Encounter List -->
      <div class="row">
        % if len(recent) > 0:
        <div class="col-sm-4">
          <h3>Latest Encounters</h3>
          <ol>
            % for enc in recent:
            <li><a href="#">{{enc.title}} - {{enc.starttime}}</a></li>
            % end
          </ol>
          <a href="#">More...</a>
        </div>
        % end
        % if len(dmg) > 0:
        <div class="col-sm-4">
          <h3>Highest-DPS Encounters</h3>
          <ol>
            % for enc in dmg:
            <li><a href="#">{{'{} - {:,.2f}/s'.format(enc.title, enc.encdps)}}</a></li>
            % end
          </ol>
          <a href="#">More...</a>
        </div>
        % end
        % if len(hard) > 0:
        <div class="col-sm-4">
          <h3>Hardest Encounters</h3>
          <ol>
            % for enc in hard:
            <li><a href="#">{{'{} - {:,.2f}/s'.format(enc.title, enc.encdps)}}, {{enc.deaths}} deaths</a></li>
            % end
          </ol>
          <a href="#">More...</a>
        </div>
        % end
      </div>
    </div> <!-- Quick Encounter List -->
