<script lang="ts">
  import {base} from '$app/paths';

</script>

<style>

table.minimalistBlack {
  border: 3px solid #000000;
  width: 100%;
  text-align: left;
  border-collapse: collapse;
}
table.minimalistBlack td, table.minimalistBlack th {
  border: 1px solid #000000;
  padding: 5px 4px;
}
table.minimalistBlack tbody td {
  font-size: 13px;
}
table.minimalistBlack thead {
  background: #CFCFCF;
  background: -moz-linear-gradient(top, #dbdbdb 0%, #d3d3d3 66%, #CFCFCF 100%);
  background: -webkit-linear-gradient(top, #dbdbdb 0%, #d3d3d3 66%, #CFCFCF 100%);
  background: linear-gradient(to bottom, #dbdbdb 0%, #d3d3d3 66%, #CFCFCF 100%);
  border-bottom: 3px solid #000000;
}
table.minimalistBlack thead th {
  font-size: 15px;
  font-weight: bold;
  color: #000000;
  text-align: left;
}
table.minimalistBlack tfoot {
  font-size: 14px;
  font-weight: bold;
  color: #000000;
  border-top: 3px solid #000000;
}
table.minimalistBlack tfoot td {
  font-size: 14px;
}

</style>

<h1>FCScore Competitions</h1>
<h2>Introduction</h2>
<h3>What is a Competition?</h3>
<p>
FCScore supports the running of both in-person and online competitions.
</p>
<p>
Each competition consists of one or more stages, with each stage containing one or more rounds.    
</p>
<ul>
    <li>The stages contain information about how to combine rounds into a stage result, what flights are valid for entry, and how competitors progress to the next stage.</li>
    <li>The rounds are where flights are added for competitors and scores are automatically recorded.  Rounds also define how flight scores are normalised.</li>
</ul>
<p>
Once the competition is created and configured, you only need to upload flights to it; FCScore will automatically find the results of rounds, stages and the competition.
</p>

<h3>Who Can Run and Enter a Competition?</h3>
<p>
Competitions are run by one or more Competition Directors (CD).  FCScore CDs can create, configure and run competitions, including uploading flights for competitors.  Contact FCScore admin to be assigned CD status in FCScore.
</p>
<p>
When creating a competition, a CD decides whether only they can add competitors and flights (typical for an in-person competition) or competitors can add themselves and/or their flights (useful for an online competition).
Competitors can be existing FCScore users, or the CD can create a temporary user account for competitors not registered with FCScore.  (If the competitor desires, they can claim the account and their flights after the competition to become an FCScore user.)
</p>

<h3>This Guide</h3>
<p>
The rest of this guide comprises some worked examples introducing how to create and run a competition. Following that is a cheat-sheet of all the available options.    
</p>
<ul>
    <li>The first example covers, in detail, the basics of how to create, configure and run a competition.</li>
    <li>The second example covers some of the FCScore features for running complex, multi-stage competitions.</li>
    <li>The third example covers setting up an online competition.</li>
</ul>

 

 
