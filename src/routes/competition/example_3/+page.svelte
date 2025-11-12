<script lang="ts">
  import {base} from '$app/paths';
</script>



<h2>Example 3 - An Open Online Competition</h2>
<p>This competition will run as follows:</p>
 <ul>
    <li>The competition will have one round of schedule F3A P27.</li>
    <li>Competitors can add themselves to the competition.</li>
    <li>Competitors must upload and link their chosen flight within 24 hours of flying it.  Only flights flown whilst the competition round is open are allowed.</li>
    <li>Each competitor may upload only one flight and may not subsequently replace that flight.</li>
    <li>The result will be normalised by best score to 1000 points.</li>
 </ul>

<h3>Create the Competition</h3>
 <p>Following the same steps as Example 1, create a new competition.</p>
 <ul>
    <li>To allow pilots to enter themselves, we select <b>Allow pilots to enter</b>.</li>
    <li>To allow pilots to add their own flight, we select <b>Allow pilots to link their own flights</b>.</li>
 </ul>
 <img src="{base}/figure38.png">

<h3>Add a Stage</h3> 
 <p>Following the same steps as example 1, create a stage.</p>
 <ul>
    <li>To ensure competitors fly whilst the round is open, select <b>Must boot whilst round is open</b>.</li>
    <li>To ensure that the competitors upload whilst the comp is open and with 24 hours of flying, we:</li>
    <ul>
        <li>Select <b>Must upload whilst round is open</b></li>
        <li>Set <b>upload within (hours from boot)</b> to 24</li>
    </ul>
    <li>To ensure that each competitor can only upload one flight, select <b>Prevent flight overwrite</b>.</li>
 </ul>
 <img src="{base}/figure39.png">

<h3>Add a Round</h3>
 <p>Following the same steps as Example 1, add a Round.  The only setting to be made here is the normalisation, which we set to <b>Best Score</b> to 1000.</p>
 <img src="{base}/figure40.png">

<h3>Run the Competition</h3>
 <p>This is as simple as opening the round by clicking on it and selecting <b>Open</b>.</p>
 <img src="{base}/figure41.png">

 <p>Your competition will appear in the competitions list, and Competitors can now add themselves by clicking the <b>Enter</b> button. </p>
 <img src="{base}/figure42.png">

 <p>They will then appear in the competition.</p>
 <img src="{base}/figure43.png">

 <p>To add a flight, they can link it as they upload it, or click the ellipsis (<b>…</b>) by their name in the round to link an already uploaded flight (see Example 1).</p>
 <p>Once you are ready to finish the competition, simply close the round by clicking it and selecting <b>Close</b>.</p>
 