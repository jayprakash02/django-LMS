<template>
  <div>
    <div
      class="card mb-5 pt-3 pb-5 rounded-0 border-top-0 border-right-0 border-left-0"
    >
      <div class="col-md-4">
        <a class="mr-2" href="/courses/ecommerce"
          ><img
            src="@/assets/card.jpg"
            class="w-100"
            alt="course eCommerce thumbnail"
        /></a>
      </div>
      <div class="col-md-8 px-3">
        <div class="card-block px-3">
          <h4 class="card-title undefined">
            <a class="mr-2" href="/courses/ecommerce">eCommerce</a>
          </h4>
          <div class="markdown-preview jm-markdown">
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum
              non error impedit totam natus ex quo tempora blanditiis,
              cupiditate mollitia.
            </p>
          </div>
          <a class="mr-2 btn btn-outline-cfe" href="/courses/ecommerce">View</a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "courseCard",
};
</script>