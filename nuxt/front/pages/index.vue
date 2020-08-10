<template>
  <v-layout
    column
  >
    <v-flex
      xs12
      sm8
      md6
    >
      <v-row>
        <v-col 
          class="color-red"
          cols="1"
        >
          スキップ
        </v-col>
        <v-col 
          class="color-green"
          cols="10"
        >
          メイン
        </v-col>
        <v-col 
          class="color-blue"
          cols="1"
        >
          気になる
        </v-col>
      </v-row>
      <v-row style="height: 10%;">
        <v-col
          class="color-white"
        >
          bottom
        </v-col>
      </v-row>
    </v-flex>
  </v-layout>
</template>

<script>
import Logo from '~/components/Logo.vue'
import VuetifyLogo from '~/components/VuetifyLogo.vue'

export default {
  components: {
    Logo,
    VuetifyLogo
  },
  data() {
    return {
      dat: []
    }
  },
  async mounted(){
    const url = "/api/get_person/" 
    const response = await this.$axios.get(url)
    this.dat = response.data
  }
}
</script>

<style scoped>
.color-red {
  background-color: red;
}
.color-green {
  background-color: green;
}
.color-blue {
  background-color: blue;
}
.color-white {
  background-color: white;
}
.fullheight {
    height: 100%;
}
</style>