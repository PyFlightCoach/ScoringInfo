<script>
  import { base } from '$app/paths';
</script>



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
    <li>Select <b>Create Competition</b>.</li>
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
    <li>Click the <b>Create</b> button.</li>
</ul>

<p>Your new competition is shown:</p>
<img src="{base}/figure4.png">

<h3>Add a Stage</h3>
<ul>
    <li>Click on the bar containing the name of your competition to bring up the competition pop-up.</li>
    <li>Select <b>Add New Stage</b></li>
</ul>

<img src="{base}/figure5.png">

<ul>
    <li>This brings up the stage pop-up.</li>
    <li>Only the best two-from-three rounds count, so we add the <b>Use top n</b> rule with a value of 2.</li>
</ul>
<img src="{base}/figure6.png">

<ul>
    <li>Click the <b>Create</b> button.</li>
</ul>
<p>Your competition now has the stage:</p>
 <img src="{base}/figure7.png">

<h3>Add Three Rounds</h3>
<ul>
    <li>Click on Stage 1 to bring up the stage options pop-up.</li>
    <li>Select <b>Add New Round</b></li>
</ul>
 <img src="{base}/figure8.png">

 <ul>
    <li>This will bring up the New Round pop-up.</li>
    <li>Select the schedule for the round.</li>
    <li>For this example, we want the best raw-score normalised to 1000.  Select <b>Best Score</b> in the normalisation pull-down, and enter 1000 in the <b>Normalise to</b> box.</li>
 </ul>
 <img src="{base}/figure9.png">

<ul>
    <li>Click the <b>Create</b> button.</li>
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
    <li>Enter the name or email address of the FCScore user and click <b>Search</b>.</li>
</ul>
<img src="{base}/figure12.png">

<ul>
    <li>FCScore users who match the search (if any) will be shown in the search results:</li>
</ul>
<img src="{base}/figure13.png">

<ul>
    <li>If your competitor is already an FCScore User, click on them in the search results and then click <b>Add</b>.</li>
    <li>If your competitor is not an FCScore User, click on <b>Can't find your user? Create a new one here</b> to bring up the new user pop-up.</li>
</ul>
<img src="{base}/figure14.png">

<ul>
    <li>Enter the competitors name and select their country.</li>
    <li>It is preferable to enter their email address - this will allow them to claim the account as their own (including their flights) in the future.</li>
    <li>Click <b>Add</b>.</li>
    <li>Repeat for all of your competitors.</li>
</ul>

<p>Your competition now has competitors.  In this example, I have added ten competitors:</p>
<img src="{base}/figure15.png">

<h3>Changing the Running Order</h3>
<ul>
    <li>In the menu ribbon, you will see that Results is highlighted.</li>
    <li>To change the running order, click instead on <b>Running Order</b>.  To begin, each competitor has the same default running order in each round:</li>
</ul>
<img src="{base}/figure16.png">

<ul>
    <li>Click on Stage 1 and select <b>Running Order</b> in the pop-up.</li>
</ul>
<img src="{base}/figure17.png">

<ul>
    <li>Since there are ten competitors, we rotate the running order by three competitors each round.</li>
    <li>Click <b>Apply</b>.</li>
</ul>
<img src="{base}/figure18.png">

<p>The running order is updated:</p>
<img src="{base}/figure19.png">

<h3>Run the Competition</h3>

<h4>Start Round 1</h4>
<ul>
    <li>Click on Round 1 to bring up the Round pop-up.</li>
    <li>Select <b>Open</b>.</li>
</ul>
<img src="{base}/figure20.png">

<p>The colouring will change to show that the round is open:</p>
<img src="{base}/figure21.png">

<h4>Upload a Flight</h4>
 <ul>
    <li>Create and score the flight as you would normally.</li>
    <li>Before uploading, select the <b>Link to competition after upload</b> checkbox.</li>
 </ul>
 <img src="{base}/figure22.png">
 
 <ul>
    <li>Click the <b>Select Competition</b> button.  A pop-up appears with the competitions you can upload to.  Click <b>Select</b> on the correct competition:</li>
 </ul>
 <img src="{base}/figure23.png">

 <ul>
    <li>You can now select the round and competitor for the flight, and click <b>Upload</b>.</li>
 </ul>
 <img src="{base}/figure24.png">

 <ul>
    <li>The flight is uploaded and the updated competition is shown:</li>
 </ul>
 <img src="{base}/figure25.png">

<h4>Assign an Already Uploaded Flight</h4> 
 <p>If you or a competitor has already uploaded a flight to the database, you can directly add it to the competition for that competitor for a round.</p>
 <ul>
    <li>Click on the <b>…</b> for competitor and round you want to assign a flight for.  Select <b>Link Flight from DB</b>.</li>
 </ul>
 <img src="{base}/figure26.png">

 <ul>
    <li>A list of flights is shown for the competitor.  Click <b>Link</b> for the desired flight.</li>
 </ul>
 <img src="{base}/figure27.png">

 <ul>
    <li>The flight is added to the competition.</li>
 </ul>

<h4>Close the Round</h4>
 <p>Once you have added flights for the competitors, you should close the round.</p>
 <ul>
    <li>Click on the Round heading and click <b>Close</b> in the pop-up.</li>
 </ul>
 <img src="{base}/figure28.png">

<h4>Finish your Competition</h4>
 <p>Once all of the flights are flown and uploaded, your competition is complete. FCScore automatically applies the competition rules you have configured, such as normalisation and dropping rounds.</p>
 <img src="{base}/figure29.png">