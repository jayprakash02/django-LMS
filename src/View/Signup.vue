<template>
  <div>
    <Navbar />
    <div class="col-10 col-md-3 mx-auto text-center mt-4">
      <h1>Signup</h1>
      <div>
        <p v-if="incorrectAuth">
          Server Not Responding try again later.
        </p>
        <form class="mt-4" v-on:submit.prevent="userSignup">
          <div class="my-2 position-relative form-group">
            <label for="username" class="undefined">Username</label
            ><input
              v-model="username"
              required=""
              name="username"
              id="username"
              placeholder="stark@teamcfe.com"
              type="text"
              class="undefined form-control"
              value=""
            /><span></span>
          </div>
          <div class="my-2 position-relative form-group">
            <label for="username" class="undefined">Email</label
            ><input
              v-model="email"
              required=""
              name="email"
              id="email"
              placeholder="stark@teamcfe.com"
              type="text"
              class="undefined form-control"
              value=""
            /><span></span>
          </div>
          <div class="my-2 position-relative form-group">
            <label for="username" class="undefined">Password</label
            ><input
              v-model="password1"
              required=""
              name="password"
              id="password"
              placeholder="************"
              type="password"
              class="undefined form-control"
              value=""
            /><span></span>
          </div>
          <div class="my-2 undefined position-relative form-group">
            <label for="passowrd" class="">Enter Password Again</label
            ><input
              v-model="password2"
              required=""
              name="password"
              id="password"
              placeholder="************"
              type="password"
              class="undefined form-control"
              value=""
            /><span></span>
          </div>
          <p><button type="submit" class="btn btn-cfe">Sign up</button></p>
          <p></p>
        </form>
        <div>
          <p class="lead mt-5"><a class="" to="/login">Login</a></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";
import Navbar from "@/components/Navbar.vue";
export default {
  name: "login",
  created() {
    if (this.$store.getters["auth/loggedIn"])
      this.$router.push({ name: "home" });
  },
  data() {
    return {
      username: "",
      password1: "",
      password2: "",
      email: "",
      incorrectAuth: false,
    };
  },
  components: {
    Navbar,
  },
  methods: {
    userSignup() {
      api
        .post("rest-auth/registration/", {
          username: this.username,
          password1: this.password1,
          password2: this.password2,
          email: this.email,
        })
        .catch(() => {
          this.incorrectAuth = true;
        })
        .then(() => {
          this.$router.push({ name: "login" });
        });
    },
  },
};
</script>
<style scoped>
.btn-cfe {
  background-color: #007cae;
  color: #fff;
}
</style>