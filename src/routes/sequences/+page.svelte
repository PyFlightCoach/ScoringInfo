<script lang="ts">
  import {base} from '$app/paths';

</script>
<h1>Aerobatic Sequence Definition</h1>

<p>
Developing a computer model of an aerobatic sequence and the associated judging criteria is a fundamental part of the judging process. 
</p>

<h2>Principal Elements</h2>
<p>
  An aerobatic manoeuvre is formed from a group of principal elements flown sequentially. A principal element is a basic building block and may be a loop, line (or roll), snap, spin or stallturn. We will add support for tailslides in a future release. All of these elements have a set of parameters that can be used to scale them, or adjust their geometry in other ways. For example, a line element has a length, a speed and a roll angle to integrate along its length. 
</p>
<div class="row">
  <img src='{base}/line_1.png' class="col-md-2" alt="Line 1">
  <img src='{base}/line_2.png' class="col-md-2" alt="line_2">
  <img src='{base}/loop_1.png' class="col-md-2" alt="loop_1">
  <img src='{base}/loop_2.png' class="col-md-2" alt="loop_2">
  <img src='{base}/loop_3.png' class="col-md-2" alt="loop_3">
  <img src='{base}/snap_1.png' class="col-md-2" alt="snap_1">
  <img src='{base}/spin_1.png' class="col-md-2" alt="spin_1">
  <img src='{base}/stallturn_1.png' class="col-md-2" alt="stallturn_1">
</div>  
<p>
  As part of the judging process we have developed a method of automatically generating flight data to represent the principal elements and you have been able to view these template flights in the Flight Coach plotter for quite a while. The template generation process also creates all the downgrades applicable to the manoeuvre based on the rules of the aerobatic category the sequence is defined for. 
</p>

<h2>Available Sequences</h2>
<p>The definition of new sequences is not trivial. Eventually we hope to introduce a user interface to allow you to create your own sequences and to parse <a href="https://openaero.net/">olan</a> strings. Until then the sequences available in FCScore can be viewed <a href="https://www.flightcoach.org/fcscore/schedule/browse/">here</a> and we will try to keep up to date with the known sequences for most aerobatic categories.</p>
