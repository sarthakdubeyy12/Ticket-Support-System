import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    tickets: []
  },
  mutations: {
    setUser(state, user) {
      state.user = user
    },
    setTickets(state, tickets) {
      state.tickets = tickets
    }
  },
  actions: {
    async fetchTickets({ commit }) {
      try {
        const response = await Vue.prototype.$http.get('/tickets/', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        })
        commit('setTickets', response.data)
      } catch (error) {
        console.error('Failed to fetch tickets:', error)
      }
    }
  }
})
