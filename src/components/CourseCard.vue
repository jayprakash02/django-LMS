<template>
  <div>
    <div
      class="card mb-5 pt-3 pb-5 rounded-0 border-top-0 border-right-0 border-left-0"
    >
      <div class="row">
        <div class="col-md-4">
          <a class="mr-2" href="#"
            ><img
              :src="imageUrl"
              class="w-100"
              :alt="title"
          /></a>
        </div>
        <div class="col-md-8 px-3">
          <div class="card-block px-3">
            <h4 class="card-title undefined">
              <a class="mr-2" href="#">{{ title }}</a>
            </h4>
            <div class="markdown-preview jm-markdown">
              <p>
                {{ description }}
              </p>
            </div>
            <a class="mr-2 btn btn-outline-cfe" href="#"
              >View</a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "courseCard",
  props:{
    title:String,
    description:String,
    imageUrl:String
  }
};
</script>
<style scoped>
.btn-outline-cfe {
    color: #007cae!important;
    background-color: initial;
    background-image: none;
    border-color: #007cae!important;
}
</style>