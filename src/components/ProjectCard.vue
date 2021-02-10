<template>
  <div class="col-12 col-md-6 col-lg-4 mb-3">
    <div class="card border-0 false">
      <a href="#"
        ><img
          :src="imageUrl"
          class="card-img-top"
          :alt="title"
      /></a>
      <div class="card-body">
        <h4 class="card-title">
          <a href="#">{{ title }}</a>
        </h4>
        <div class="undefined markdown-preview jm-markdown">
          <div v-html="description" ></div>
          <p>
            <a
              target="_self"
              href="#"
              >Code Reference</a
            >
          </p>
        </div>
        <a class="btn btn-cfe mt-2" href="#">View</a>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "projectCard",
  props:{
    title:String,
    description:String,
    imageUrl:String
  }
};
</script>
<style scoped>
.markdown-preview {
    min-height: 0!important;
    max-height: 150px!important;
    overflow-y: scroll;
}
.btn-cfe {
    background-color: #007cae;
    color: #fff;
}
</style>