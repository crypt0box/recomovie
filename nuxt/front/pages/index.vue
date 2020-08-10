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
          cols="10"
        >
          メイン
          <div class="text-center">
            <v-rating 
              v-model="rating"
              size=64
              color="orange"
              half-increments
              @input="next"
            />
            {{ rating }}
          </div>
          <div>
            <v-btn @click="getMovieList">映画情報の取得！</v-btn>
          </div>
          <v-row>
            <v-col
              cols="6"
              v-for="result in results"
              :key=result.id
            >
              <v-img :src="'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + result.poster_path" />
              {{ result.title }}
            </v-col>
          </v-row>
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
      rating: 0,
      results: [],
    }
  },
  async mounted(){
    const url = "/api/get_person/" 
    const response = await this.$axios.get(url)
    this.dat = response.data
  },
  methods: {
    next() {
      console.log("評価したよ！")
    },
    async getMovieList(){
      const url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=b94cb735cf0f288b14e0cde950ecea98&language=ja&page=1'
      await this.$axios.get(url)
      .then(response => {
        this.results = response.data.results
        console.log(this.results)
      }).catch(err => {
        console.log('err:', err);
      });
    }
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