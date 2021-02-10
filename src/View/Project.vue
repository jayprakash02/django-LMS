<template>
  <div>
    <Navbar />
    <div class="container-fluid bg-white text-dark">
      <div class="row">
        <div
          class="order-1 order-md-1 col-12 col-md-2 col-lg-2 py-3 bg-sidebar-light border-right"
        >
          <SecondNav activeTab="Project" />
        </div>
        <div
          class="order-2 order-md-2 col-12 col-md-10 col-lg-10 min-height min-page-height py-3"
        >
          <div class="">
            <div class="d-flex">
              <div class="flex-grow-1"><h1>Projects</h1></div>
            </div>
            <div class="row">
              <p v-if="projects.length === 0">No Projects</p>
              <div v-for="(project, index) in projects" :key="index">
                <projectCard
                  :title="project.title"
                  :description="project.desc"
                  :imageUrl="project.image"
                />
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
import projectCard from "@/components/ProjectCard.vue";

import { mapState } from "vuex";

export default {
  name: "project",
  components: {
    Navbar,
    SecondNav,
    projectCard,
  },
  computed: mapState({
    projects: (state) => state.projects.projects,
  }),
  created() {
    this.$store.dispatch("projects/getProjects");
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
.btn-outline-secondary {
  color: #6c757d;
  background-color: transparent;
  background-image: none;
  border-color: #6c757d;
}
</style>