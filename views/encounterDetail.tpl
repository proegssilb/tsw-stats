% allies = setdefault('allies', ())
% foes = setdefault('foes', ())
% alliedHits = setdefault('alliedHits', ())
% alliedHeals = setdefault('alliedHeals', ())
% foeHits = setdefault('foeHits', ())
% foeHeals = setdefault('foeHeals', ())
% include('head', title='Index')

<div class="container-fluid"> <!-- Quick Encounter List -->

  <div class="row encounter-listing">
    <ul class="combatant-list">
      % for ally in allies:
      <li class="combatant col-sm-4 col-xs-12">
        <p class="combatant-name">{{ally.name}}</p>
        <p>{{'{:,.2f}'.format(ally.encdps)}} dps &bull; {{'{:,.2f}'.format(ally.enchps)}} hps &bull; took {{'{:,.0f}'.format(ally.damagetaken)}}</p>
      </li>
      % end
    </ul>
    <div class="col-xs-12 hcenter">
      <h1>-vs-</h1>
    </div>
    <ul class="combatant-list">
      % for foe in foes:
      <li class="combatant col-sm-4 col-xs-12">
        <p class="combatant-name">{{foe.name}}</p>
        <p>{{'{:,.2f}'.format(foe.encdps)}} dps &bull; {{'{:,.2f}'.format(foe.enchps)}} hps &bull; took {{'{:,.0f}'.format(foe.damagetaken)}}</p>
      </li>
      % end
    </ul>
  </div>

  <div class="row">
    <div class="col-xs-12 col-md-6">
      <p>Allied Stacked Line Damage Over Time Graph goes here.</p>
    </div>
    <div class="col-xs-12 col-md-6">
      <p>Allied Stacked Line Heal Over Time Graph goes here.</p>
    </div>
  </div>

  <div class="row">
    <div class="col-xs-12 col-md-6">
      <p>Foe Stacked Line Damage Over Time Graph goes here.</p>
    </div>
    <div class="col-xs-12 col-md-6">
      <p>Foe Stacked Line Heal Over Time Graph goes here.</p>
    </div>
  </div>

  <div>
    <div class="col-xs-12">
      <table id="encounterSummary" class="table table-hover">
        <caption>Per-Character encounter summaries</caption>
        <thead>
          <tr>
            <th>Name</th>
            <th>Duration (s)</th>
            <th data-breakpoints="xs sm md">Damage Dealt</th>
            <th>Encounter DPS</th>
            <th>Damage Crit Rate</th>
            <th data-breakpoints="xs sm">Damage Taken</th>
            <th data-breakpoints="xs">Percent of Total Damage</th>
            <th data-breakpoints="xs sm md">Healing dealt</th>
            <th>Encounter HPS</th>
            <th>Heal Crit Rate</th>
            <th data-breakpoints="xs">Percent of Total Heal</th>
            <th data-breakpoints="xs sm">Heal Taken</th>
            <th data-breakpoints="xs">Deaths</th>
          </tr>
        </thead>
        <tbody>
          % for ally in allies:
          <tr>
            <td>{{ally.name}}</td>
            <td>{{ally.duration}}</td>
            <td>{{'{:,.0f}'.format(ally.damage)}}</td>
            <td>{{'{:,.2f}'.format(ally.encdps)}}</td>
            <td>{{ally.critdamperc}}</td>
            <td>{{'{:,.0f}'.format(ally.damagetaken)}}</td>
            <td>{{ally.damageperc}}</td>
            <td>{{'{:,.0f}'.format(ally.healed)}}</td>
            <td>{{'{:,.2f}'.format(ally.enchps)}}</td>
            <td>{{ally.crithealperc}}</td>
            <td>{{ally.healedperc}}</td>
            <td>{{'{:,.0f}'.format(ally.healstaken)}}</td>
            <td>{{ally.deaths}}</td>
          </tr>
          % end
          % for foe in foes:
          <tr>
            <td>{{foe.name}}</td>
            <td>{{foe.duration}}</td>
            <td>{{'{:,.0f}'.format(foe.damage)}}</td>
            <td>{{'{:,.2f}'.format(foe.encdps)}}</td>
            <td>{{foe.critdamperc}}</td>
            <td>{{'{:,.0f}'.format(foe.damagetaken)}}</td>
            <td>{{foe.damageperc}}</td>
            <td>{{'{:,.0f}'.format(foe.healed)}}</td>
            <td>{{'{:,.2f}'.format(foe.enchps)}}</td>
            <td>{{foe.crithealperc}}</td>
            <td>{{foe.healedperc}}</td>
            <td>{{'{:,.0f}'.format(foe.healstaken)}}</td>
            <td>{{foe.deaths}}</td>
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
    $('#encounterSummary').footable();
} );
</script>

% include('endhtml')
