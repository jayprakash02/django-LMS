<template>
    <div class="log"></div>
</template>
<script>
export default {
    created () {
      this.$store.dispatch('auth/userLogout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    }
}
</script>