export const state = () => ({
  idToken: '',
})

export const mutations = {
  setIdToken(state, idToken) {
    state.idToken = idToken
  }
}

export const actions = {
  register({ commit }, idToken)  {
    commit('setIdToken', idToken)
  } 
}

export const getters = {
  getIdToken(state) {
    return state.idToken
  }
}