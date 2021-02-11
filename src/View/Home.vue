<template>
  <div>
    <Navbar />
    <h1>Hello, {{ username }}</h1>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import { mapState} from 'vuex'
export default {
    name: "Home",
    computed: mapState({
      username:(state)=>state.auth.username
    }),
  components: {
    Navbar,
    },
}
</script>
<style scoped>

</style>