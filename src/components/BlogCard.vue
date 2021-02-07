<template>
  <div class="mb-2 false card border-0">
    <a href="#"
      ><img
        class="card-img-top"
        src="@/assets/blogcard.jpg"
        alt="But what are Django signals? logo"
    /></a>
    <div class="">
      <h1>
        <a href="#">But what are Django signals?</a>
      </h1>
      <div>
        <p class="mb-2 pb-0">
          <span format="ll">Jan 27, 2021</span><span class="mx-1">·</span
          ><a href="#">Justin Mitchel</a><span class="mx-1">·</span
          ><a class="text-muted mr-1" href="#"
            >Common Questions</a
          ><span class="mx-1">·</span
          ><a class="text-muted mr-1" href="#">Django</a
          ><span class="mx-1">·</span
          ><a class="text-muted mr-1" href="#">Django Signals</a
          ><span class="mx-1">·</span
          ><a class="text-muted mr-1" href="#">Python</a
          ><span class="mx-1">·</span
          ><a class="text-muted mr-1" href="#">signals</a>
        </p>
      </div>
      <hr />
      <div>
        <div class="post-inline-preview">
          <div class="undefined">
            <div class="embed-responsive embed-responsive-16by9 mb-3">
              <iframe
                src="https://www.youtube.com/embed/rEX50LJrFuU"
                title="https://www.youtube.com/embed/rEX50LJrFuU"
                class="embed-responsive-item"
                width="560"
                height="315"
                allow="autoplay; encrypted-media"
                allowfullscreen=""
                frameborder="0"
                controls=""
              ></iframe>
            </div>
          </div>
        </div>
        <a
          class="btn btn-sm btn-cfe my-4"
          href="#"
          >View Post</a
        >
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "blogCard",
};
</script>
<style scoped>
.btn-cfe {
  background-color: #007cae;
  color: #fff;
}
.post-inline-preview {
    height: 250px;
    overflow: hidden;
}
.embed-responsive {
    position: relative;
    display: block;
    width: 100%;
    padding: 0;
    overflow: hidden;
}
</style>