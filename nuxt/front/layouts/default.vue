<template>
  <v-app dark>
    <header class="header">
      <v-row justify="center">
        <div v-if="isLogin">
          <v-btn text to="/">
            HOME
          </v-btn>
          <v-btn text to="/result">
            RESULT
          </v-btn>
          <v-btn text @click="logout">
            LOGOUT
          </v-btn>
        </div>
        <div v-else>
          <v-btn text to="/register">
            REGISTER
          </v-btn>
          <v-btn text to="/login">
            LOGIN
          </v-btn>
        </div>
      </v-row>
    </header>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <v-footer>
      <div>&copy; {{ new Date().getFullYear() }}</div>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      isLogin: localStorage.getItem('idToken') ? true : false
    }
  },
  methods: {
    logout({ redirect }) {
      localStorage.removeItem('idToken')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.header {
  padding: 1%;
}
.fill-width {
  width: 100%;
}
</style>
