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

<h2>Example 1: A Typical 1-Day, 3-Round, In-Person Competition</h2>
<p>This competition will run as follows:</p>
<ul>
    <li>All competitors will fly three rounds of the same schedule.</li>
    <li>Each round will be normalised to 1000, based on the best raw-score in the round.</li>
    <li>The best two rounds for each competitor will count to the competition result.</li>
</ul>
<p>In FCScore, the competition will look like this:</p>
<img src="{base}/figure1.png">

<h3>Create the Competition</h3>
<ul>
    <li>On the menu ribbon, click on the trophy icon to bring up the competition menu.</li>
    <li>Select Create Competition.</li>
</ul>
<img src="{base}/figure2.png">

<ul>
    <li>A new pop-up will appear to create the competition.</li>
    <li>Enter the competition name and select the category from the pulldown.</li>
    <li>For this example, we do not want competitors to register themselves, and we only need normalisation for the rounds.</li>
    <li>Optionally add a description, and enter the planned start and end dates.</li>
</ul>
<img src="{base}/figure3.png">

<ul>
    <li>Click the Create button.</li>
</ul>

<p>Your new competition is shown:</p>
<img src="{base}/figure4.png">

<h3>Add a Stage</h3>
<ul>
    <li>Click on the bar containing the name of your competition to bring up the competition pop-up.</li>
    <li>Select Add New Stage</li>
</ul>

<img src="{base}/figure5.png">

<ul>
    <li>This brings up the stage pop-up.</li>
    <li>Only the best two-from-three rounds count, so we add the Use top n rule with a value of 2.</li>
</ul>
<img src="{base}/figure6.png">

<ul>
    <li>Click the Create button.</li>
</ul>
<p>Your competition now has the stage:</p>
 <img src="{base}/figure7.png">

<h3>Add Three Rounds</h3>
<ul>
    <li>Click on Stage 1 to bring up the stage options pop-up.</li>
    <li>Select Add New Round</li>
</ul>
 <img src="{base}/figure8.png">

 <ul>
    <li>This will bring up the New Round pop-up.</li>
    <li>Select the schedule for the round.</li>
    <li>For this example, we want the best raw-score normalised to 1000.  Select Best Score in the normalisation pull-down, and enter 1000 in the Normalise to box.</li>
 </ul>
 <img src="{base}/figure9.png">

<ul>
    <li>Click the Create button.</li>
    <li>Repeat the above to add rounds 2 and 3.</li>
</ul>
<p>Your competition now has three rounds:</p>
 <img src="{base}/figure10.png">

<h3>Add the Competitors</h3> 

<ul>
    <li>At the bottom left of your competition, click the + button.  This will bring up the User Search pop-up.</li>
</ul>
<img src="{base}/figure11.png">

<ul>
    <li>Enter the name or email address of the FCScore user and click Search.</li>
</ul>
<img src="{base}/figure12.png">

<ul>
    <li>FCScore users who match the search (if any) will be shown in the search results:</li>
</ul>
<img src="{base}/figure13.png">

<ul>
    <li>If your competitor is already an FCScore User, click on them in the search results and then click Add.</li>
    <li>If your competitor is not an FCScore User, click on Can't find your user? Create a new one here to bring up the new user pop-up.</li>
</ul>
<img src="{base}/figure14.png">

<ul>
    <li>Enter the competitors name and select their country.</li>
    <li>It is preferable to enter their email address - this will allow them to claim the account as their own (including their flights) in the future.</li>
    <li>Click Add.</li>
    <li>Repeat for all of your competitors.</li>
</ul>

<p>Your competition now has competitors.  In this example, I have added ten competitors:</p>
<img src="{base}/figure15.png">

<h3>Changing the Running Order</h3>
<ul>
    <li>In the menu ribbon, you will see that Results is highlighted.</li>
    <li>To change the running order, click instead on Running Order.  To begin, each competitor has the same default running order in each round:</li>
</ul>
<img src="{base}/figure16.png">

<ul>
    <li>Click on Stage 1 and select Running Order in the pop-up.</li>
</ul>
<img src="{base}/figure17.png">

<ul>
    <li>Since there are ten competitors, we rotate the running order by three competitors each round.</li>
    <li>Click Apply.</li>
</ul>
<img src="{base}/figure18.png">

<p>The running order is updated:</p>
<img src="{base}/figure19.png">

<h3>Run the Competition</h3>

<h4>Start Round 1</h4>
<ul>
    <li>Click on Round 1 to bring up the Round pop-up.</li>
    <li>Select Open.</li>
</ul>
<img src="{base}/figure20.png">

<p>The colouring will change to show that the round is open:</p>
<img src="{base}/figure21.png">

<h4>Upload a Flight</h4>
 <ul>
    <li>Create and score the flight as you would normally.</li>
    <li>Before uploading, select the Link to competition after upload checkbox.</li>
 </ul>
 <img src="{base}/figure22.png">
 
 <ul>
    <li>Click the Select Competition button.  A pop-up appears with the competitions you can upload to.  Click Select on the correct competition:</li>
 </ul>
 <img src="{base}/figure23.png">

 <ul>
    <li>You can now select the round and competitor for the flight, and click Upload.</li>
 </ul>
 <img src="{base}/figure24.png">

 <ul>
    <li>The flight is uploaded and the updated competition is shown:</li>
 </ul>
 <img src="{base}/figure25.png">

<h4>Assign an Already Uploaded Flight</h4> 
 <p>If you or a competitor has already uploaded a flight to the database, you can directly add it to the competition for that competitor for a round.</p>
 <ul>
    <li>Click on the … for competitor and round you want to assign a flight for.  Select Link Flight from DB.</li>
 </ul>
 <img src="{base}/figure26.png">

 <ul>
    <li>A list of flights is shown for the competitor.  Click Link for the desired flight.</li>
 </ul>
 <img src="{base}/figure27.png">

 <ul>
    <li>The flight is added to the competition.</li>
 </ul>

<h4>Close the Round</h4>
 <p>Once you have added flights for the competitors, you should close the round.</p>
 <ul>
    <li>Click on the Round heading and click Close in the pop-up.</li>
 </ul>
 <img src="{base}/figure28.png">

<h4>Finish your Competition</h4>
 <p>Once all of the flights are flown and uploaded, your competition is complete. FCScore automatically applies the competition rules you have configured, such as normalisation and dropping rounds.</p>
 <img src="{base}/figure29.png">
	
 
<h2>Example 2 - An In-Person Competition with Preliminary and Final Stages</h2>

 <p>This competition will run as follows:</p>

 <ul>
    <li>It starts with a Preliminary stage:</li>
    <ul>
        <li>All competitors will fly three rounds of the preliminary schedule.</li>
        <li>Each round will be normalised to 1000, based on the best raw-score in the round.</li>
        <li>The best two rounds will count to the Preliminary stage result.</li>
        <li>The Preliminary stage result will be normalised to 1000 based on the best stage score.</li>
    </ul>
    <li>The top five competitors will then progress to Final stage.</li>
    <ul>
        <li>The Final competitors will fly two rounds of the final schedule.</li>
        <li>Each flown round will be normalised to 1000, based on the best raw-score in the round.</li>
        <li>The result from the preliminary stage will be included as a third round.</li>
        <li>The best two of the three scores will count to the final result.</li>
    </ul>
 </ul>
 
 <p>Most of the steps to create and run the competition are the same as Example 1, but with more use of the features of FCScore competitions.  We will focus on the differences.</p>
 <p>In FCScore, the competition will look like this:</p>
 <img src="{base}/figure30.png">

<h3>Create the Competition</h3>
 <p>Follow the same process as example 1, with the following settings:</p>
 <img src="{base}/figure31.png">

<h3>Create the Preliminary Stage</h3>
 <p>The preliminary stage has the following features:</p>
 <ul>
    <li>The stage results are normalised to 1000; for this we set the normalisation to Best Score.</li>
    <li>Only the best two rounds for each competitor shall count to the stage result.  For this we set Use top n to 2.</li>
    <li>Only the top five pilots will progress at the end of this stage. For this we use the Progress top n feature and set it to 5.</li>
 </ul>

 <p>The resulting stage configuration is:</p>
 <img src="{base}/figure32.png">

<h3>Create the Preliminary Rounds</h3>
 <p>This step is the same as for example 1.  The flights in each round are P25 schedule and the rounds have their best flight normalised to 1000.  For each of the three rounds, the configuration is:</p>
 <img src="{base}/figure33.png">
	
<h3>Create the Final Stage</h3>
 <p>The final stage has the following features:</p>
 <ul>
    <li>It has three rounds; two flown F25 rounds and one round containing the scores from the Preliminary Stage.</li>
    <li>For the competitors progressing to this stage, the scores from the Preliminary Stage are not accumulated into the result (instead, they are included as the first round). For this, we select Restart scoring from this stage.</li>
    <li>Only the best two rounds count towards the result, so we use the Use top n feature set to 2.</li>
 </ul>

 <p>The stage configuration is:</p> 
 <img src="{base}/figure34.png">

<h3>Create the Final Rounds</h3>
<h4>Round 1</h4>
 <p>This round is not a flown round, instead it contains the scores from the Preliminary Stage.  For this, we use the Score from previous stage feature, selecting the Preliminary Stage:</p>
 <img src="{base}/figure35.png">

<h4>Rounds 2 and 3</h4>
 <p>These rounds are flown F25 rounds, with normalisation to 1000.  Their configuration is:</p>
 <img src="{base}/figure36.png">

<h3>Add Competitors and Run the Competition</h3>
 <p>This follows the same steps as Example 1. The completed competition is shown below.</p>
 <img src="{base}/figure37.png">
 

<h2>Example 3 - An Open Online Competition</h2>
<p>This competition will run as follows:</p>
 <ul>
    <li>The competition will have one round of schedule F3A P27.</li>
    <li>Competitors can add themselves to the competition.</li>
    <li>Competitors must upload and link their chosen flight within 24 hours of flying it.  Only flights flown whilst the competition round is open are allowed.</li>
    <li>Each competitor may upload only flight.</li>
    <li>The result will be normalised by best score to 1000 points.</li>
 </ul>

<h3>Create the Competition</h3>
 <p>Following the same steps as Example 1, create a new competition.</p>
 <ul>
    <li>To allow pilots to enter themselves, we select Allow pilots to enter.</li>
    <li>To allow pilots to add their own flight, we select Allow pilots to link their own flights.</li>
 </ul>
 <img src="{base}/figure38.png">

<h3>Add a Stage</h3> 
 <p>Following the same steps as example 1, create a stage.</p>
 <ul>
    <li>To ensure competitors fly whilst the round is open, select Must boot whilst round is open.</li>
    <li>To ensure that the competitors upload whilst the comp is open and with 24 hours of flying, we:</li>
    <ul>
        <li>Select Must upload whilst round is open</li>
        <li>Set upload within (hours from boot) to 24</li>
    </ul>
    <li>To ensure that each competitor can only upload one flight, select Prevent flight overwrite.</li>
 </ul>
 <img src="{base}/figure39.png">

<h3>Add a Round</h3>
 <p>Following the same steps as Example 1, add a Round.  The only setting to be made here is the normalisation, which we set to Best Score to 1000.</p>
 <img src="{base}/figure40.png">

<h3>Run the Competition</h3>
 <p>This is as simple as opening the round by clicking on it and selecting Open.</p>
 <img src="{base}/figure41.png">

 <p>Your competition will appear in the competitions list, and Competitors can now add themselves by clicking the Enter button. </p>
 <img src="{base}/figure42.png">

 <p>They will then appear in the competition.</p>
 <img src="{base}/figure43.png">

 <p>To add a flight, they can link it as they upload it, or click the ellipsis (…) by their name in the round to link an already uploaded flight (see Example 1).</p>
 <p>Once you are ready to finish the competition, simply close the round by clicking it and selecting close.</p>
 

<h1>Cheat Sheet</h1>	
	
<table class="minimalistBlack">
<thead>
    <tr>
        <th colspan="2">Competition Options</th>
    </tr>
</thead>
  <tr>
    <td>Allow Pilots to Enter</td>
    <td>Allows pilots to add themselves to the competition.  Otherwise, only CDs can add competitors.</td>
  </tr>
  <tr>
    <td>Allow Pilots to Link Their Own Flights</td>
    <td>Allows pilots to upload-and-link or link their own flights.  Otherwise, only CDs can link flights.</td>
  </tr>
  <tr>
    <td>Start Date and End Date</td>
    <td>These are planning dates.  The actual dates and times in the database are calculated from when you open and close rounds.</td>
  </tr>

<thead>
    <tr>
        <th colspan="2">Stage Options</th>
    </tr>
</thead>
  <tr>
    <td>Progress Top N</td>
    <td>Only the best N competitors will be progressed from this stage to the next stage.</td>
  </tr>
  <tr>
    <td>Use Top N</td>
    <td>For each competitor, their best N round scores count (other scores are “dropped”).</td>
  </tr>
  <tr>
    <td>Restart Scoring From this Stage</td>
    <td>For competitors in this stage, all previous stage scores are dropped.  An example is a FINAL stage where, for those making the FINAL, only the scores from the FINAL decide the result.</td>
  </tr>

<thead>
    <tr>
        <th colspan="2">Round Options</th>
    </tr>
</thead>
  <tr>
    <td>Must Boot whilst Round is Open</td>
    <td>Flights will only be accepted if their log file start time is from when the round is open.</td>
  </tr>
  <tr>
    <td>Must upload whilst Round is Open</td>
    <td>Flights will only be accepted if they are linked when the round is open.</td>
  </tr>
  <tr>
    <td>Upload within (N hours)</td>
    <td>Flight will only be accepted if it is uploaded and linked within N hours of the log file start time.</td>
  </tr>
  <tr>
    <td>Prevent Flight Overwrite</td>
    <td>Competitors may only link one flight to a round.  If they subsequently try to link another (probably better!) flight, it will be rejected.</td>
  </tr>
  <tr>
    <td>Score from Previous Stage</td>
    <td>Takes the scores from a previous stage and uses them as the Raw Scores in this round.</td>
  </tr>

<thead>
    <tr>
        <th colspan="2">Normalisation Options (Applies to Competition, Stages and Rounds)</th>
    </tr>
</thead>
  <tr>
    <td>Raw Score</td>
    <td>No normalisation is applied; the raw flight scores are used.</td>
  </tr>
  <tr>
    <td>Best Score N</td>
    <td>Normalisation is applied such that the best score is normalised to N.</td>
  </tr>
  <tr>
    <td>Average Score N</td>
    <td>Normalisation is applied such that a raw score equal to the average of all scores would be normalised to N.</td>
  </tr>
</table>
