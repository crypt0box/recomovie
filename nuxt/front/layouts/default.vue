<template>
  <v-app dark>
    <header class="header">
      <v-row justify="center">
        <v-btn text to="/">
          HOME
        </v-btn>
        <v-btn text to="/result">
          RESULT
        </v-btn>
        <v-btn text>
          LOGIN
        </v-btn>
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

<style scoped>
.header {
  padding: 1%;
}
.fill-width {
  width: 100%;
}
</style>
