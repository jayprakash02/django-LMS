<template>
  <div>
    <Navbar />
    <div class="col-10 col-md-3 mx-auto text-center mt-4">
      <h1>Login</h1>
      <div>
        <p v-if="incorrectAuth">
          Incorrect username or password entered - please try again
        </p>
        <form class="mt-4" v-on:submit.prevent="login">
          <div class="my-2 position-relative form-group">
            <label for="username" class="undefined">Username/Email</label
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
          <div class="my-2 undefined position-relative form-group">
            <label for="passowrd" class="">Password</label
            ><input
              v-model="password"
              required=""
              name="password"
              id="password"
              placeholder="************"
              type="password"
              class="undefined form-control"
              value=""
            /><span></span>
          </div>
          <p><button type="submit" class="btn btn-cfe">Login</button></p>
          <p></p>
        </form>
        <div>
          <p class="lead mt-5"><a class="" href="/signup">Sign up</a></p>
          <p class="lead mt-3">
            <a class="" href="/password/reset">Reset Password</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
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
      password: "",
      incorrectAuth: false,
    };
  },
  components: {
    Navbar,
  },
  methods: {
    login() {
      this.$store
        .dispatch("auth/userLogin", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          this.$router.push({ name: "home" });
        })
        .catch(() => {
          this.incorrectAuth = true;
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