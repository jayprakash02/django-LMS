<template>
  <div>
    <nav class="bg-cfe navbar-dark d-flex navbar navbar-expand-md">
      <a aria-current="page" class="navbar-brand mr-2 active" href="/"
        ><img
          src="@/assets/logo.svg"
          class="d-inline-block align-top mr-1"
          width="30"
          height="30"
          alt="Coding for Entrepreneurs nav logo"
      /></a>
      <form class="my-0 form d-none d-md-inline w-25">
        <input
          class="border-0 form-control mr-md-2 bg-black text-light"
          type="text"
          name="q"
          placeholder="Search"
          aria-label="Search"
          value=""
        />
      </form>
      <button type="button" class="navbar-toggler">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" style="">
        <ul class="ml-auto text-center navbar-nav">
          <li class="nav-item">
            <a aria-current="page" class="nav-link active" href="/">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/courses">Courses</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/projects">Projects</a>
          </li>
          <li class="nav-item"><a class="nav-link" href="/login">Login</a></li>
          <li class="nav-item">
            <a class="nav-link bg-warning text-dark rounded" href="/enroll"
              >Enroll</a
            >
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
