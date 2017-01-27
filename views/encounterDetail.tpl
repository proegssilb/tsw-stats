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
      <div class="graph" id="allyDPS"></div>
    </div>
    <div class="col-xs-12 col-md-6">
      <div class="graph" id="allyHPS"></div>
    </div>
  </div>

  <div class="row">
    <div class="col-xs-12 col-md-6">
      <div class="graph" id="foeDPS"></div>
    </div>
    <div class="col-xs-12 col-md-6">
      <div class="graph" id="foeHPS"></div>
    </div>
  </div>

  <div class="row">
    <div class="col-xs-12">
      <table id="encounterSummary" class="table table-hover" data-sorting="true">
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
            <td data-sort-value="{{ally.name}}"><a href="/encounter/{{ally.encid}}/c/{{ally.name}}">{{ally.name}}</a></td>
            <td>{{ally.duration}}</td>
            <td data-sort-value="{{ally.damage}}">{{'{:,.0f}'.format(ally.damage)}}</td>
            <td data-sort-value="{{ally.encdps}}">{{'{:,.2f}'.format(ally.encdps)}}</td>
            <td>{{ally.critdamperc}}</td>
            <td data-sort-value="{{ally.damagetaken}}">{{'{:,.0f}'.format(ally.damagetaken)}}</td>
            <td>{{ally.damageperc}}</td>
            <td data-sort-value="{{ally.healed}}">{{'{:,.0f}'.format(ally.healed)}}</td>
            <td data-sort-value="{{ally.enchps}}">{{'{:,.2f}'.format(ally.enchps)}}</td>
            <td>{{ally.crithealperc}}</td>
            <td>{{ally.healedperc}}</td>
            <td data-sort-value="{{ally.healstaken}}">{{'{:,.0f}'.format(ally.healstaken)}}</td>
            <td>{{ally.deaths}}</td>
          </tr>
          % end
          % for foe in foes:
          <tr>
            <td><a href="/encounter/{{foe.encid}}/c/{{foe.name}}">{{foe.name}}</a></td>
            <td>{{foe.duration}}</td>
            <td data-sort-value="{{foe.damage}}">{{'{:,.0f}'.format(foe.damage)}}</td>
            <td data-sort-value="{{foe.encdps}}">{{'{:,.2f}'.format(foe.encdps)}}</td>
            <td>{{foe.critdamperc}}</td>
            <td data-sort-value="{{foe.damagetaken}}">{{'{:,.0f}'.format(foe.damagetaken)}}</td>
            <td>{{foe.damageperc}}</td>
            <td data-sort-value="{{foe.healed}}">{{'{:,.0f}'.format(foe.healed)}}</td>
            <td data-sort-value="{{foe.enchps}}">{{'{:,.2f}'.format(foe.enchps)}}</td>
            <td>{{foe.crithealperc}}</td>
            <td>{{foe.healedperc}}</td>
            <td data-sort-value="{{foe.healstaken}}">{{'{:,.0f}'.format(foe.healstaken)}}</td>
            <td>{{foe.deaths}}</td>
          </tr>
          % end
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="row">
  <div class="col-md-6">
    <h2>Ally's Most-Damaging Hits</h2>
    <table id="topHits" class="table table-hover">
      <thead>
        <tr>
          <th>Attacker</th>
          <th>Ability Name</th>
          <th>Damage</th>
          <th>Modifiers</th>
          <th>Victim</th>
        </tr>
      </thead>
      <tbody>
        % for hit in alliedHits:
        <tr>
          <td><a href="/encounter/{{hit.encid}}/c/{{hit.attackerName}}">{{hit.attackerName}}</a></td>
          <td><a href="/encounter/{{hit.encid}}/a/{{hit.attackSummary.attackTypeId}}">{{hit.attacktype}}</a></td>
          <td>{{hit.damage}}</td>
          <td>{{hit.specialTags()}}</td>
          <td><a href="/encounter/{{hit.encid}}/c/{{hit.victimName}}">{{hit.victimName}}</a></td>
        </tr>
        % end
      </tbody>
    </table>
  </div>
  <div class="col-md-6">
    <h2>Ally's Most-Healing Hits</h2>
    <table id="topHeals" class="table table-hover">
      <thead>
        <tr>
          <th>Healer</th>
          <th>Ability Name</th>
          <th>Healing</th>
          <th>Modifiers</th>
          <th>Recipient</th>
        </tr>
      </thead>
      <tbody>
        % for hit in alliedHeals:
        <tr>
          <td><a href="/encounter/{{hit.encid}}/c/{{hit.attackerName}}">{{hit.attackerName}}</a></td>
          <td><a href="/encounter/{{hit.encid}}/a/{{hit.attackSummary.attackTypeId}}">{{hit.attacktype}}</a></td>
          <td>{{hit.damage}}</td>
          <td>{{hit.specialTags()}}</td>
          <td><a href="/encounter/{{hit.encid}}/c/{{hit.victimName}}">{{hit.victimName}}</a></td>
        </tr>
        % end
      </tbody>
    </table>
  </div>
</div>

<div class="row">
  <div class="col-md-6">
    <h2>Enemy's Most-Damaging Hits</h2>
    <table id="topFoeHits" class="table table-hover">
      <thead>
        <th>Attacker</th>
        <th>Ability Name</th>
        <th>Damage</th>
        <th>Modifiers</th>
        <th>Victim</th>
      </thead>
      <tbody>
        <tbody>
          % for hit in foeHits:
          <tr>
            <td><a href="/encounter/{{hit.encid}}/c/{{hit.attackerName}}">{{hit.attackerName}}</a></td>
            <td><a href="/encounter/{{hit.encid}}/a/{{hit.attackSummary.attackTypeId}}">{{hit.attacktype}}</a></td>
            <td>{{hit.damage}}</td>
            <td>{{hit.specialTags()}}</td>
            <td><a href="/encounter/{{hit.encid}}/c/{{hit.victimName}}">{{hit.victimName}}</a></td>
          </tr>
          % end
        </tbody>
      </tbody>
    </table>
  </div>
  <div class="col-md-6">
    <h2>Enemy's Most-Healing Hits</h2>
    <table id="topFoeHeals" class="table table-hover">
      <thead>
        <th>Healer</th>
        <th>Ability Name</th>
        <th>Healing</th>
        <th>Modifiers</th>
        <th>Recipient</th>
      </thead>
      <tbody>
        <tbody>
          % for hit in foeHeals:
          <tr>
            <td><a href="/encounter/{{hit.encid}}/c/{{hit.attackerName}}">{{hit.attackerName}}</a></td>
            <td><a href="/encounter/{{hit.encid}}/a/{{hit.attackSummary.attackTypeId}}">{{hit.attacktype}}</a></td>
            <td>{{hit.damage}}</td>
            <td>{{hit.specialTags()}}</td>
            <td><a href="/encounter/{{hit.encid}}/c/{{hit.victimName}}">{{hit.victimName}}</a></td>
          </tr>
          % end
        </tbody>
      </tbody>
    </table>
  </div>
</div>

% include('js-bottom')

<script type="text/javascript">
$(document).ready( function () {
    $('#encounterSummary').DataTable({ "order": [[4, "desc"]] });
    new Dygraph(
      document.getElementById("allyDPS"),
      "/encounter/{{encounter.encid}}/graph?allied=T&attackTypeId=1",
      {
        connectSeparatedPoints: true,
        stackedGraph: true,
        stackedGraphNaNFill: "inside",
        title: "Allied Damage Over Time"
      }
    );
    new Dygraph(
      document.getElementById("foeDPS"),
      "/encounter/{{encounter.encid}}/graph?allied=F&attackTypeId=1",
      {
        connectSeparatedPoints: true,
        stackedGraph: true,
        stackedGraphNaNFill: "inside",
        title: "Foe Damage Over Time"
      }
    );
    new Dygraph(
      document.getElementById("allyHPS"),
      "/encounter/{{encounter.encid}}/graph?allied=T&attackTypeId=3",
      {
        connectSeparatedPoints: true,
        stackedGraph: true,
        stackedGraphNaNFill: "inside",
        title: "Allied Healing Over Time"
      }
    );
    new Dygraph(
      document.getElementById("foeHPS"),
      "/encounter/{{encounter.encid}}/graph?allied=F&attackTypeId=3",
      {
        connectSeparatedPoints: true,
        stackedGraph: true,
        stackedGraphNaNFill: "inside",
        title: "Foe Healing Over Time"
      }
    );
} );
</script>

% include('endhtml')
