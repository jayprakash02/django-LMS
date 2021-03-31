<template>
  <div>
    <Navbar />
    <div class="container-fluid bg-white text-dark">
      <div class="row">
        <div
          class="order-1 order-md-1 col-12 col-md-2 col-lg-2 py-3 bg-sidebar-light border-right"
        >
          <SecondNav activeTab="Topic" />
        </div>
        <div
          class="order-2 order-md-2 col-12 col-md-10 col-lg-10 min-height min-page-height py-3"
        >
          <div class="">
            <nav class="d-md-block d-none">
              <ol class="breadcrumb false">
                <li class="undefined breadcrumb-item">Topics</li>
              </ol>
            </nav>
            <div class="row text-center">
              <div class="col-12 mb-3">
                <input
                  type="text"
                  class="form-control border false"
                  placeholder="Filter..."
                  value=""
                />
              </div>
            </div>
            <div class="row">
              <topicCard />
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
import topicCard from "@/components/TopicCard.vue";
export default {
  name: "topic",
  components: {
    Navbar,
    SecondNav,
    topicCard,
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