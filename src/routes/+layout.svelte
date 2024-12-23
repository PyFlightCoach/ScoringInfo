<script lang="ts">
  import "bootstrap/dist/css/bootstrap.min.css";
  import "bootstrap/dist/js/bootstrap.min.js";
</script>

<div
  class="container justify-content-center min-vh-100 d-flex flex-column"
>
  <div class="row flex-grow-1 justify-content-center">

    <div class="col-md-10 col-lg-9 px-0 justify-content-center">
      <div style="position:relative; height: 100%;">
        <div
          class="overflow-auto pt-3"
          style="position: absolute; top: 0; left: 0; bottom: 0; right: 0;"
        >
          <slot />
        </div>
      </div>
    </div>
  </div>
</div>
