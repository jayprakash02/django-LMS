<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info" class="bg">
      <b-navbar-brand to="/"
        ><img
          src="@/assets/logo.svg"
          class="d-inline-block align-top mr-1"
          width="30"
          height="30"
          alt="Coding for Entrepreneurs nav logo"
      /></b-navbar-brand>

      <b-navbar-toggle class="text" target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-nav-form class="center">
          <b-form-input
            size="sm"
            class="mr-sm-2"
            placeholder="Search"
          ></b-form-input>
        </b-nav-form>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item to="/course" class="center" Right>Course</b-nav-item>
          <b-nav-item to="/project" class="center" Right>Project</b-nav-item>
          <b-nav-item to="/login" v-if="!log" class="center" Right
            >Login</b-nav-item
          >
          <b-nav-item to="/logout" v-if="log" class="center" Right
            >Logout</b-nav-item
          >
          <b-nav-item to="/enroll" Right class="bg-warning rounded center"
            >Enroll</b-nav-item
          >
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "Navbar",
  data() {
    return {
      log: false,
    };
  },
  created() {
    this.$store.dispatch("auth/getCredential");
    if (this.$store.getters["auth/loggedIn"]) this.log = true;
    mapState({
      username: (state) => state.auth.username,
    });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.bg {
  background-color: #007cae !important;
  color: #fff !important;
}
.center {
  text-align: center;
  justify-content: center;
}
</style>
