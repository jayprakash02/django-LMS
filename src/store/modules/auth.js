import api from '../../services/api'

const state = {
    key: null
}
const getters = {
    loggedIn(state) {
        return state.key != null
    }
}
const actions = {
    userLogout(context) {
        if (context.getters.loggedIn) {
            context.commit('destroyToken')
        }
    },
    userLogin(context, usercredentials) {
        return new Promise((resolve, reject) => {
            api.post('rest-auth/login/', {
                username: usercredentials.username,
                password: usercredentials.password
            })
                .then(response => {
                    context.commit('updateStorage', { key: response.data.key })
                    resolve()
                })
                .catch(err => {
                    reject(err)
                })
        })
    }
}
const mutations = {
    updateStorage(state, { key }) {
        state.key = key
    },
    destroyToken(state) {
        state.key = null
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}