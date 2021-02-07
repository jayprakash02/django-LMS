<template>
  <div>
    <Navbar />
    <div class="container-fluid bg-white text-dark">
      <div class="row d-flex">
        <div
          class="order-1 order-md-1 col-12 col-md-2 col-lg-2 py-3 bg-sidebar-light border-right"
        >
          <SecondNav activeTab="Blog" />
        </div>
        <div
          class="order-2 order-md-2 col-12 col-md-10 col-lg-10 min-height min-page-height py-3"
        >
          <div class="">
            <h1 class="d-block">Blog</h1>
          </div>
          <div class="row">
            <div class="col-md-9">
              <BlogCard />
            </div>
            <div class="col-md-3">
              <div>
                <div class="mb-3">
                  <div class="false card">
                    <div class="card-header">Trending</div>
                    <div class="list-group list-group-flush">
                      <a
                        class="list-group-item"
                        href="#"
                        >Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis, error.</a
                      >
                    </div>
                  </div>
                </div>
                <div class="mb-3">
                  <div class="false card">
                    <div class="card-header">Discover</div>
                    <div class="list-group list-group-flush">
                      <a
                        class="list-group-item"
                        href="#"
                        >Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid, corrupti.</a
                      >
                    </div>
                  </div>
                </div>
                <div class="mb-3">
                  <div class="false card">
                    <div class="card-header">Featured</div>
                    <div class="list-group list-group-flush">
                      <a
                        class="list-group-item"
                        href="#"
                        >Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis, corporis.</a
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import SecondNav from "@/components/SecondNav.vue";
import BlogCard from "@/components/BlogCard.vue";
export default {
  name: "blog",
  components: {
    Navbar,
    SecondNav,
    BlogCard,
  },
};
</script>
<style scoped>
.d-block {
  display: block;
}
.bg-sidebar-light {
  background-color: #e9ecef !important;
}
.border-right {
  border-right: 1px solid #dee2e6 !important;
}
.pb-3,
.py-3 {
  padding-bottom: 1rem !important;
}
.pt-3,
.py-3 {
  padding-top: 1rem !important;
}
</style>