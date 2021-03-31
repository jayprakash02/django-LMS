<template>
  <div class="col-md-4 col-sm-6 mb-3">
    <div class="card border-0">
      <div class="card-body p-0 border-0">
        <a class="btn btn-cfe px-5 py-5 btn-block" href="#"
          ><span class="lead">Production</span></a
        >
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "topicCard",
};
</script>
<style scoped>
.btn-cfe, .list-group-item.active {
    color: #fff!important;
    background-color: #007cae!important;
    border-color: #007cae!important;
}
.btn-cfe {
    background-color: #007cae;
    color: #fff;
}
</style>