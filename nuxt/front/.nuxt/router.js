import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _6d54dd98 = () => interopDefault(import('../pages/inspire.vue' /* webpackChunkName: "pages/inspire" */))
const _0ae68c27 = () => interopDefault(import('../pages/login.vue' /* webpackChunkName: "pages/login" */))
const _4160c755 = () => interopDefault(import('../pages/register.vue' /* webpackChunkName: "pages/register" */))
const _413ee910 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/inspire",
    component: _6d54dd98,
    name: "inspire"
  }, {
    path: "/login",
    component: _0ae68c27,
    name: "login"
  }, {
    path: "/register",
    component: _4160c755,
    name: "register"
  }, {
    path: "/",
    component: _413ee910,
    name: "index"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
