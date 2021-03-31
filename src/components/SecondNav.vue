<template>
  <div>
    <ul class="mb-4 list-group">
      <router-link
        class="border-0 list-group-item px-2 pointer"
        :class="{ active: activeTab === 'Course' }"
        to="/course"
        aria-current="page"
        >Courses</router-link
      ><router-link
        class="border-0 list-group-item px-2 pointer"
        :class="{ active: activeTab === 'Project' }"
        to="/project"
        >Projects</router-link
      ><router-link
        class="border-0 list-group-item px-2 pointer"
        :class="{ active: activeTab === 'Blog' }"
        to="/blog"
        >Posts</router-link
      >
    </ul>
    <ul class="mb-4 list-group">
      <router-link
        class="border-0 list-group-item px-2 pointer"
        :class="{ active: activeTab === 'Topic' }"
        to="/topic"
        >Topic</router-link
      >
      <router-link
        class="border-0 list-group-item px-2 pointer"
        :class="{ active: activeTab === 'Question' }"
        to="/questions"
        >Questions</router-link
      >
    </ul>
  </div>
</template>
<script>
export default {
  name: "SecondNav",
  props: ["activeTab"],
};
</script>