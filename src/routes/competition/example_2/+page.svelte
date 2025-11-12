<script>
  import { base } from '$app/paths';
</script>

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
        <li>The result from the preliminary stage will be included as the first round.</li>
        <li>The Final competitors will fly two rounds of the final schedule.</li>
        <li>Each flown round will be normalised to 1000, based on the best raw-score in the round.</li>
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
    <li>The stage results are normalised to 1000; for this we set the normalisation to <b>Best Score</b>.</li>
    <li>Only the best two rounds for each competitor shall count to the stage result.  For this we set <b>Use top n</b> to 2.</li>
    <li>Only the top five pilots will progress at the end of this stage. For this we use the <b>Progress top n</b> feature and set it to 5.</li>
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
    <li>For the competitors progressing to this stage, the scores from the Preliminary Stage are not accumulated into the result (instead, they are included as the first round). For this, we select <b>Restart scoring from this stage</b>.</li>
    <li>Only the best two rounds count towards the result, so we use the <b>Use top n</b> feature set to 2.</li>
 </ul>

 <p>The stage configuration is:</p> 
 <img src="{base}/figure34.png">

<h3>Create the Final Rounds</h3>
<h4>Round 1</h4>
 <p>This round is not a flown round, instead it contains the scores from the Preliminary Stage.  For this, we use the <b>Score from previous stage</b> feature, selecting the Preliminary Stage:</p>
 <img src="{base}/figure35.png">

<h4>Rounds 2 and 3</h4>
 <p>These rounds are flown F25 rounds, with normalisation to 1000.  Their configuration is:</p>
 <img src="{base}/figure36.png">

<h3>Add Competitors and Run the Competition</h3>
 <p>This follows the same steps as Example 1. The completed competition is shown below.</p>
 <img src="{base}/figure37.png">