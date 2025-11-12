<script lang="ts">
  import {base} from '$app/paths';
 
</script>



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

  <p><a class="link"  href="{base}/competition">Competition Home</a></p>
  <p><a class="link" data-sveltekit-noscroll href="{base}/competition/cheat_sheet">Cheat Sheet</a></p>
  <p><a class="link" data-sveltekit-noscroll href="{base}/competition/example_1">Example: Creating a Competition</a></p>
  <p><a class="link" data-sveltekit-noscroll href="{base}/competition/example_2">Example: A Competition with Preliminary and Final Stages</a></p>
  <p><a class="link" data-sveltekit-noscroll href="{base}/competition/example_3">Example: An Open Online Competition</a></p>

<slot/>