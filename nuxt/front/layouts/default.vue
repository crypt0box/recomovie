<template>
  <v-app dark>
    <v-toolbar
      class="fill-width"
      max-height="50"
      dense
    >
      <v-toolbar-title>recomovie</v-toolbar-title>
    </v-toolbar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <v-footer absolute>
      <div>&copy; {{ new Date().getFullYear() }}</div>
    </v-footer>
  </v-app>
</template>

<style scoped>
.fill-width {
  width: 100%;
}
</style>
