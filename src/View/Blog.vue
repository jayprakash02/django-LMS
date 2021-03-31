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
            <div class="d-flex">
              <div class="flex-grow-1"><h1>Blog</h1></div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-9">
              <p v-if="videos.length === 0">No Videos</p>
              <div v-for="(video, index) in videos" :key="index">
                <BlogCard
                  :title="video.title"
                  :description="video.desc"
                  :imageUrl="video.image"
                  :timestamp="video.timestamp"
                  :videoUrl="video.video"
                />
              </div>
            </div>
            <div class="col-md-3">
              <div>
                <div class="mb-3">
                  <div class="false card">
                    <div class="card-header">Trending</div>
                    <div class="list-group list-group-flush">
                      <a class="list-group-item" href="#"
                        >Lorem ipsum dolor sit amet consectetur adipisicing
                        elit. Corporis, error.</a
                      >
                    </div>
                  </div>
                </div>
                <div class="mb-3">
                  <div class="false card">
                    <div class="card-header">Discover</div>
                    <div class="list-group list-group-flush">
                      <a class="list-group-item" href="#"
                        >Lorem ipsum dolor sit amet consectetur adipisicing
                        elit. Aliquid, corrupti.</a
                      >
                    </div>
                  </div>
                </div>
                <div class="mb-3">
                  <div class="false card">
                    <div class="card-header">Featured</div>
                    <div class="list-group list-group-flush">
                      <a class="list-group-item" href="#"
                        >Lorem ipsum dolor sit amet consectetur adipisicing
                        elit. Perferendis, corporis.</a
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

import { mapState } from "vuex";

export default {
  name: "blog",
  components: {
    Navbar,
    SecondNav,
    BlogCard,
  },
  computed: mapState({
    videos: (state) => state.videos.videos,
  }),
  created() {
    this.$store.dispatch("videos/getVideos");
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