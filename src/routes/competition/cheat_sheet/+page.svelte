


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

<h1>Cheat Sheet</h1>	
	
<table class="minimalistBlack">
<thead>
    <tr>
        <th colspan="2">Competition Options</th>
    </tr>
</thead>
<tbody>
  <tr>
    <td><b>Allow Pilots to Enter</b></td>
    <td>Allows pilots to add themselves to the competition.  Otherwise, only CDs can add competitors.</td>
  </tr>
  <tr>
    <td><b>Allow Pilots to Link Their Own Flights</b></td>
    <td>Allows pilots to upload-and-link or link their own flights.  Otherwise, only CDs can link flights.</td>
  </tr>
  <tr>
    <td><b>Start Date</b> and <b>End Date</b></td>
    <td>These are planning dates.  The actual dates and times in the database are calculated from when you open and close rounds.</td>
  </tr>
</tbody>
<thead>
    <tr>
        <th colspan="2">Stage Options</th>
    </tr>
</thead>
<tbody>
  <tr>
    <td><b>Progress Top N</b></td>
    <td>Only the best N competitors will be progressed from this stage to the next stage.</td>
  </tr>
  <tr>
    <td><b>Use Top N</b></td>
    <td>For each competitor, their best N round scores count (other scores are “dropped”).</td>
  </tr>
  <tr>
    <td><b>Restart Scoring From this Stage</b></td>
    <td>For competitors in this stage, all previous stage scores are dropped.  An example is a FINAL stage where, for those making the FINAL, only the scores from the FINAL decide the result.</td>
  </tr>
</tbody>
<thead>
    <tr>
        <th colspan="2">Round Options</th>
    </tr>
</thead>
<tbody>
  <tr>
    <td><b>Must Boot whilst Round is Open</b></td>
    <td>Flights will only be accepted if their log file start time is from when the round is open.</td>
  </tr>
  <tr>
    <td><b>Must upload whilst Round is Open</b></td>
    <td>Flights will only be accepted if they are linked when the round is open.</td>
  </tr>
  <tr>
    <td><b>Upload within (N hours)</b></td>
    <td>Flight will only be accepted if it is uploaded and linked within N hours of the log file start time.</td>
  </tr>
  <tr>
    <td><b>Prevent Flight Overwrite</b></td>
    <td>Competitors may only link one flight to a round.  If they subsequently try to link another (probably better!) flight, it will be rejected.</td>
  </tr>
  <tr>
    <td><b>Score from Previous Stage</b></td>
    <td>Takes the scores from a previous stage and uses them as the Raw Scores in this round.</td>
  </tr>
</tbody>
<thead>
    <tr>
        <th colspan="2">Normalisation Options (Applies to Competition, Stages and Rounds)</th>
    </tr>
</thead>
<tbody>
  <tr>
    <td><b>Raw Score</b></td>
    <td>No normalisation is applied; the raw flight scores are used.</td>
  </tr>
  <tr>
    <td><b>Best Score N</b></td>
    <td>Normalisation is applied such that the best score is normalised to N.</td>
  </tr>
  <tr>
    <td><b>Average Score N</b></td>
    <td>Normalisation is applied such that a raw score equal to the average of all scores would be normalised to N.</td>
  </tr>
</tbody>
<thead>
    <tr>
        <th colspan="2">Running Order Rotation Options</th>
    </tr>
</thead>
<tbody>
  <tr>
    <td><b>Continue from previous stage</b></td>
    <td>The first round of this stage will be taken from the last round of the previous stage (with rotation applied).</td>
  </tr>
  <tr>
    <td><b>Randomise first round</b></td>
    <td>The first round of this stage will have a random running order applied.</td>
  </tr>
  <tr>
    <td><b>Rotate by N</b></td>
    <td>The running order will be shifted down by N pilots between rounds.</td>
  </tr>
</tbody>
</table>