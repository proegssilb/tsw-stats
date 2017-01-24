% include('head', title='Index')

<div class="fluid-container">
  <div class="row">
    <div class="col-cs-12 hcenter">
      <h1>{{character.name}}</h1>
    </div>
  </div>
  <div class="jumbotron">
    <div class="row">
      <div class="hidden-xs hidden-sm col-md-1"></div> <!--Spacer.-->
      <div class="col-sm-4 col-md-3 hcenter">
        <p>Total Damage Dealt</p>
        <p>{{'{:,.0f}'.format(character.damage)}}</p>
      </div>
      <div class="col-sm-4 col-md-4 hcenter">
        <p>Total Healing Given</p>
        <p>{{'{:,.0f}'.format(character.healed)}}</p>
      </div>
      <div class="col-sm-4 col-md-3 hcenter">
        <p>Total Damage Received</p>
        <p>{{'{:,.0f}'.format(character.damageTaken)}}</p>
      </div>
      <div class="hidden-xs hidden-sm col-md-1"></div> <!--Spacer.-->
    </div>
  </div>
  <div class="row">
    <div class="col-xs-12 hcenter">
      <h3>Some kind of combatant-related data table should go here.</h3>
    </div>
  </div>
</div>

% include('js-bottom')

% include('endhtml')
