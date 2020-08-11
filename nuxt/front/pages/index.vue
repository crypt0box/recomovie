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
          @click="skip(); counter()"
        >
          スキップ
        </v-col>
        <v-col 
          cols="10"
        >
          メイン
          <div class="text-center">
            {{ rating }}
            <v-rating
              v-model="rating"
              size=64
              color="orange"
              close-delay=10
              half-increments
            /> 
            <v-btn
              class="mb-3"
              color="orange"
              outlined
              @click="submit(); counter()"
            >
            評価する
            </v-btn>
          </div>
          <v-row justify="center">
            <v-img 
              :src="'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + poster_path[cnt]"
              max-width="300"
              max-height="424"
              width="300"
              height="424"
            />
          </v-row>
          <v-row 
            class="mt-3"
            justify="center"
          >
            <h1>{{ title[cnt] }}</h1>
          </v-row>
        </v-col>
        <v-col 
          class="color-blue"
          cols="1"
          @click="myList(); counter()"
        >
          気になる
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
      cnt: 0,
      rating: 0,
      results: [],
      title: [],
      poster_path: [],
    }
  },
  async mounted(){
    const url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=b94cb735cf0f288b14e0cde950ecea98&language=ja&page=1'
    await this.$axios.get(url)
    .then(response => {
      this.results = response.data.results
      this.results.forEach(element => {
        this.title.push(element.title)
        this.poster_path.push(element.poster_path)
      });
      console.log('res:', this.results)
    }).catch(err => {
      console.log('err:', err);
    });
  },
  methods: {
    submit() {
      console.log("評価したよ！")
      this.rating = 0
    },
    skip() {
      console.log('sikipをクリックしたよ')
    },
    myList() {
      console.log('「気になる」をクリックしたよ')
    },
    counter() {
      this.cnt += 1
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