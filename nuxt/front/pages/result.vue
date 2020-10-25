<template>
<div>
  <v-row justify="center">
    <h1>あなへのおすすめ</h1>
  </v-row>
  <v-row justify="center">
    <v-btn 
      color="orange"
      outlined
      @click="getResults"
    >結果を見る</v-btn>
  </v-row>
  <v-row>
    <v-col v-for="n in 3" :key="n">
      <v-row justify="center">
        <v-img 
          :src="'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + poster_path[n]"
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
        <h1>{{ title[n] }}</h1>
      </v-row>
    </v-col>
  </v-row>
</div>
</template>

<script>
export default {
  data() {
    return {
      results: [],
      rank: [],
      title: [],
      poster_path: []
    }
  },
  created() {
    this.getResults()
  },
  methods: {
    // おすすめ映画のIDをバックエンドから受け取る
    async getResults() {
      const backendUrl = '/api/reco/' //バックエンド側のURL
      const tmdbUrl = 'https://api.themoviedb.org/3/movie/'
      const apiKey = '?api_key=b94cb735cf0f288b14e0cde950ecea98&language=ja'
      // バックエンドと通信
      await this.$axios.get(backendUrl)
      .then(response => {
        this.rank = [
          response.data.RankId[0].rank1, // おすすめランク1の情報
          response.data.RankId[0].rank2,
          response.data.RankId[0].rank3,
        ]
        this.rank.forEach(element => {
          // データが少なくオススメがない場合処理をスキップ
          if (element != 0) {
            let movieId = `${element}`
            const getUrl = tmdbUrl + movieId + apiKey
            // バックエンドから受け取ったmovie_idでapiと通信->映画情報を取得
            this.$axios.get(getUrl)
            .then(response => {
              this.title.push(response.data.title)
              this.poster_path.push(response.data.poster_path)
            })
          }
        });
      }).catch(err => {
        console.log('err:', err);
      });
    }
  }
}
</script>