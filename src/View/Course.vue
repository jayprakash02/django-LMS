<template>
  <div>
    <Navbar />
    <div class="container-fluid bg-white text-dark">
      <div class="row d-flex">
        <div
          class="order-1 order-md-1 col-12 col-md-2 col-lg-2 py-3 bg-sidebar-light border-right"
        >
          <SecondNav activeTab="Course" />
        </div>
        <div
          class="order-2 order-md-2 col-12 col-md-10 col-lg-10 min-height min-page-height py-3"
        >
          <div class="">
            <div class="d-block">
              <div class="flex-grow-1"><h1>Course</h1></div>
            </div>
            <div class="row text-center">
              <div class="col-12 mb-3">
                <input
                  v-model="search"
                  type="text"
                  class="form-control border false"
                  placeholder="Search..."
                  @change="searchCourses(search)"
                />
              </div>
            </div>
            <div class="col-md-10">
              <div class="row">
                <p v-if="courses.length === 0">No Courses</p>
                <div v-for="(course, index) in courses" :key="index">
                  <courseCard
                    :title="course.title"
                    :description="course.desc"
                    :imageUrl="course.image"
                  />
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
import courseCard from "@/components/CourseCard.vue";

import { mapState, mapActions } from "vuex";

export default {
  name: "course",
  data() {
    return {
      search: "",
    };
  },
  components: {
    Navbar,
    SecondNav,
    courseCard,
  },
  computed: mapState({
    courses: (state) => state.courses.courses,
  }),
  methods: mapActions("courses", ["searchCourses"]),
  created() {
    this.$store.dispatch("courses/getCourses");
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