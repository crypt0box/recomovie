<template>
  <div>
    <v-card
      :tile="$vuetify.breakpoint.sm || $vuetify.breakpoint.xs"
      class="mx-auto fill-width"
      max-width="400"
    >
      <v-card-title class="text-center pa-8">
        <h4 class="fill-width">ログイン</h4>
      </v-card-title>
      <v-divider> </v-divider>
      <div class="px-6 py-8">
        <div style="max-width:344px" class="mx-auto">
          <div>
            <v-text-field
              v-model="email"
              autofocus
              dense
              height="48px"
              outlined
              placeholder="メールアドレス"
            ></v-text-field>

            <v-text-field
              v-model="password"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              :type="showPassword ? 'text' : 'password'"
              dense
              height="48px"
              name="input-password"
              outlined
              placeholder="パスワード"
              @click:append="showPassword = !showPassword"
            ></v-text-field>
          </div>
          <div class="login-btn pb-8">
            <v-btn
              class="fill-width"
              color="#FFCB00"
              depressed
              height="48px"
              tile
              @click="login"
            >
              ログイン
            </v-btn>
          </div>
          <div class="separator separator_login_page">
            <div class="middle_separator">または</div>
          </div>
          <div class="pt-6">
            <div>
              <v-btn
                class="fill-width mb-5 text-capitalize"
                height="48px"
                outlined
                style="border-color:#979797;"
                tile
              >
                <img
                  class="button-logo-img mr-4"
                  src="https://madeby.google.com/static/images/google_g_logo.svg"
                  style="height:24px;"
                />
                Googleでログイン
              </v-btn>
            <v-divider></v-divider>
            <div class="pt-8 pb-4">
              <span>アカウントをお持ちでない方はこちら</span>
              <nuxt-link to="/register">新規会員登録</nuxt-link>
            </div>
            </div>
          </div>
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
import axios from '../axios-auth'
export default {
  data() {
    return {
      email: '',
      password: '',
      showPassword: false,
    }
  },
  methods: {
    login() {
      axios.post('/accounts:signInWithPassword?key=AIzaSyBKwaAN9FoKSNznMaONL9cte9CA5I_zEmY',
      {
        email: this.email,
        password: this.password,
        returnSecureToken: true
      }).then(response => {
        console.log('ログインに成功したよ')
        localStorage.setItem('idToken', response.data.idToken)
      });
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
.fill-width {
  width: 100%;
}
.link-caption {
  text-decoration: none;
  color: #666 !important;
  font-size: .75rem;
}
.separator {
  margin-top: 30px;
  margin-bottom: 30px;
  height: 0;
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #fff;
  position: relative;
}
.middle_separator {
  position: absolute;
  padding: 0 16px;
  color: #ccc;
  background: #fff;
  font-size: 11px;
  text-shadow: 0 1px 0 #fff;
  text-transform: uppercase;
  top: -7px;
  left: 30%;
}
.middle_separator {
  color: #777;
  font-size: 13px;
  top: -9px;
  left: 41%;
}
</style>