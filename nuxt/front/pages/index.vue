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
            {{ movie_review_data.rate }}
            <v-rating
              v-model="movie_review_data.rate"
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
      page: 1,
      results: [],
      title: [],
      poster_path: [],
      movie_review_data: {
        user_id: 0,
        movie_id: 0,
        rate: 0,
      }
    }
  },
  async mounted(){
    const baseUrl = 'https://api.themoviedb.org/3/movie/now_playing?api_key=b94cb735cf0f288b14e0cde950ecea98&language=ja&page='
    let page = `${this.page}`
    const getUrl = baseUrl + page
    await this.$axios.get(getUrl)
    .then(response => {
      this.results = response.data.results
      this.results.forEach(element => {
        this.title.push(element.title)
        this.poster_path.push(element.poster_path)
      });
      this.movie_review_data.movie_id = this.results[0].id
      console.log('res:', this.results)
    }).catch(err => {
      console.log('err:', err);
    });
  },
  methods: {
    async submit() {
      console.log("評価したよ！")
      const url = "/api/movie_review/" 
      const config = {
        headers: { 'content-type': 'multipart/form-data' }
      }
      const formData = new FormData()
      for (const data in this.movie_review_data) {
        formData.append(data, this.movie_review_data[data])
      }
      await this.$axios.$post(url, formData, config)
      .then(response => {
        console.log(response)
      })
      this.movie_review_data.rate = 0
    },
    skip() {
      console.log('sikipをクリックしたよ')
    },
    myList() {
      console.log('「気になる」をクリックしたよ')
    },
    counter() {
      this.cnt += 1
      this.movie_review_data.movie_id = this.results[this.cnt].id
      console.log(this.movie_review_data)
      if (this.cnt >= 20) {
        this.page += 1
        this.cnt = 0
        this.title = []
        this.poster_path = []
        this.getMovieList()
        console.log(this.page)
      }
    },
    async getMovieList() {
      const baseUrl = 'https://api.themoviedb.org/3/movie/now_playing?api_key=b94cb735cf0f288b14e0cde950ecea98&language=ja&page='
      let page = `${this.page}`
      const getUrl = baseUrl + page
      await this.$axios.get(getUrl)
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